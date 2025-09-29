#!/usr/bin/env python3
"""
AI Terminal Tool - Easy-to-use GUI for multiple AI providers
A simple terminal GUI application for using various AI services.
"""

import os
import asyncio
import json
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    Header, Footer, Select, Input, Button, TextArea, 
    Static, Label, LoadingIndicator, Markdown
)
from textual.binding import Binding

# API Clients
try:
    import openai
except ImportError:
    openai = None

try:
    import anthropic
except ImportError:
    anthropic = None

try:
    from google.generativeai import configure, GenerativeModel
    import google.generativeai as genai
except ImportError:
    genai = None

try:
    import requests
except ImportError:
    requests = None


@dataclass
class AIProvider:
    """Data class for AI provider configuration"""
    name: str
    models: list
    requires_api_key: bool = True
    base_url: Optional[str] = None


class ConfigManager:
    """Manages application configuration and API keys"""
    
    def __init__(self):
        self.config_dir = Path.home() / ".ai-terminal-tool"
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(exist_ok=True)
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {}
    
    def save_config(self):
        """Save configuration to file"""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except IOError:
            pass
    
    def get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for provider"""
        return self.config.get('api_keys', {}).get(provider)
    
    def set_api_key(self, provider: str, api_key: str):
        """Set API key for provider"""
        if 'api_keys' not in self.config:
            self.config['api_keys'] = {}
        self.config['api_keys'][provider] = api_key
        self.save_config()


class AIClient:
    """Unified client for different AI providers"""
    
    def __init__(self, config_manager: ConfigManager):
        self.config_manager = config_manager
        self.providers = {
            'OpenAI': AIProvider('OpenAI', ['gpt-4o', 'gpt-4o-mini', 'gpt-3.5-turbo']),
            'Claude': AIProvider('Claude', ['claude-3-5-sonnet-20241022', 'claude-3-5-haiku-20241022', 'claude-3-opus-20240229']),
            'Gemini': AIProvider('Gemini', ['gemini-2.0-flash-exp', 'gemini-1.5-pro', 'gemini-1.5-flash']),
            'Perplexity': AIProvider('Perplexity', ['llama-3.1-sonar-small-128k-online', 'llama-3.1-sonar-large-128k-online'], base_url="https://api.perplexity.ai")
        }
    
    async def get_response(self, provider: str, model: str, message: str) -> str:
        """Get response from specified AI provider"""
        api_key = self.config_manager.get_api_key(provider.lower())
        if not api_key:
            return f"Error: No API key configured for {provider}"
        
        try:
            if provider == 'OpenAI':
                return await self._openai_request(api_key, model, message)
            elif provider == 'Claude':
                return await self._claude_request(api_key, model, message)
            elif provider == 'Gemini':
                return await self._gemini_request(api_key, model, message)
            elif provider == 'Perplexity':
                return await self._perplexity_request(api_key, model, message)
            else:
                return f"Error: Unsupported provider {provider}"
        except Exception as e:
            return f"Error: {str(e)}"
    
    async def _openai_request(self, api_key: str, model: str, message: str) -> str:
        """Make request to OpenAI API"""
        if not openai:
            return "Error: OpenAI library not installed. Run: pip install openai"
        
        client = openai.OpenAI(api_key=api_key)
        response = await asyncio.to_thread(
            client.chat.completions.create,
            model=model,
            messages=[{"role": "user", "content": message}],
            max_tokens=1000
        )
        return response.choices[0].message.content
    
    async def _claude_request(self, api_key: str, model: str, message: str) -> str:
        """Make request to Claude API"""
        if not anthropic:
            return "Error: Anthropic library not installed. Run: pip install anthropic"
        
        client = anthropic.Anthropic(api_key=api_key)
        response = await asyncio.to_thread(
            client.messages.create,
            model=model,
            max_tokens=1000,
            messages=[{"role": "user", "content": message}]
        )
        return response.content[0].text
    
    async def _gemini_request(self, api_key: str, model: str, message: str) -> str:
        """Make request to Gemini API"""
        if not genai:
            return "Error: Google AI library not installed. Run: pip install google-generativeai"
        
        genai.configure(api_key=api_key)
        model_instance = genai.GenerativeModel(model)
        response = await asyncio.to_thread(model_instance.generate_content, message)
        return response.text
    
    async def _perplexity_request(self, api_key: str, model: str, message: str) -> str:
        """Make request to Perplexity API"""
        if not requests:
            return "Error: Requests library not installed. Run: pip install requests"
        
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": model,
            "messages": [{"role": "user", "content": message}],
            "max_tokens": 1000
        }
        
        response = await asyncio.to_thread(
            requests.post,
            "https://api.perplexity.ai/chat/completions",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"


class AITerminalApp(App):
    """Main application class"""
    
    CSS = """
    .container {
        height: 100%;
    }
    
    .sidebar {
        width: 30%;
        background: $surface;
        border-right: solid $primary;
    }
    
    .main-content {
        width: 70%;
        padding: 1;
    }
    
    .input-container {
        height: 6;
        border: solid $primary;
        margin-bottom: 1;
    }
    
    .output-container {
        height: 1fr;
        border: solid $accent;
    }
    
    .config-section {
        margin-bottom: 2;
        padding: 1;
        border: solid $secondary;
    }
    
    .status-bar {
        height: 3;
        background: $surface;
        border-top: solid $primary;
    }
    """
    
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit"),
        Binding("ctrl+c", "clear_output", "Clear"),
        Binding("enter", "send_message", "Send", priority=True),
    ]
    
    def __init__(self):
        super().__init__()
        self.config_manager = ConfigManager()
        self.ai_client = AIClient(self.config_manager)
        self.selected_provider = "OpenAI"
        self.selected_model = "gpt-4o"
    
    def compose(self) -> ComposeResult:
        """Create the application layout"""
        yield Header(show_clock=True)
        
        with Horizontal(classes="container"):
            with Vertical(classes="sidebar"):
                with Vertical(classes="config-section"):
                    yield Label("AI Provider:")
                    yield Select(
                        [(name, name) for name in self.ai_client.providers.keys()],
                        value="OpenAI",
                        id="provider_select"
                    )
                    
                    yield Label("Model:")
                    yield Select(
                        [(model, model) for model in self.ai_client.providers["OpenAI"].models],
                        value="gpt-4o",
                        id="model_select"
                    )
                
                with Vertical(classes="config-section"):
                    yield Label("API Key:")
                    yield Input(
                        placeholder="Enter API key...",
                        password=True,
                        id="api_key_input"
                    )
                    yield Button("Save API Key", id="save_key_btn", variant="primary")
                
                with Vertical(classes="config-section"):
                    yield Button("Clear Conversation", id="clear_btn", variant="warning")
                    yield Static(id="status_info")
            
            with Vertical(classes="main-content"):
                with Vertical(classes="input-container"):
                    yield Label("Your Message:")
                    yield TextArea(
                        placeholder="Type your message here...",
                        id="message_input"
                    )
                    yield Button("Send", id="send_btn", variant="success")
                
                with Vertical(classes="output-container"):
                    yield Label("AI Response:")
                    yield Markdown("Welcome! Select an AI provider and enter your API key to get started.", id="output_area")
        
        with Horizontal(classes="status-bar"):
            yield LoadingIndicator(id="loading")
            yield Static("Ready", id="status_text")
        
        yield Footer()
    
    def on_mount(self):
        """Initialize the application"""
        loading = self.query_one("#loading", LoadingIndicator)
        loading.visible = False
        self.update_status_info()
    
    def on_select_changed(self, event: Select.Changed):
        """Handle selection changes"""
        if event.select.id == "provider_select":
            self.selected_provider = event.value
            # Update model select based on provider
            model_select = self.query_one("#model_select", Select)
            models = self.ai_client.providers[self.selected_provider].models
            model_select.set_options([(model, model) for model in models])
            if models:
                model_select.value = models[0]
                self.selected_model = models[0]
            self.update_status_info()
        
        elif event.select.id == "model_select":
            self.selected_model = event.value
            self.update_status_info()
    
    def on_button_pressed(self, event: Button.Pressed):
        """Handle button presses"""
        if event.button.id == "save_key_btn":
            self.save_api_key()
        elif event.button.id == "send_btn":
            self.action_send_message()
        elif event.button.id == "clear_btn":
            self.action_clear_output()
    
    def save_api_key(self):
        """Save the entered API key"""
        api_key_input = self.query_one("#api_key_input", Input)
        if api_key_input.value.strip():
            self.config_manager.set_api_key(
                self.selected_provider.lower(),
                api_key_input.value.strip()
            )
            api_key_input.value = ""
            self.update_status("API key saved successfully!")
            self.update_status_info()
        else:
            self.update_status("Please enter an API key")
    
    def action_send_message(self):
        """Send message to AI provider"""
        message_input = self.query_one("#message_input", TextArea)
        message = message_input.text.strip()
        
        if not message:
            self.update_status("Please enter a message")
            return
        
        if not self.config_manager.get_api_key(self.selected_provider.lower()):
            self.update_status("Please enter and save your API key first")
            return
        
        # Clear input and start processing
        message_input.text = ""
        self.process_message(message)
    
    async def process_message(self, message: str):
        """Process message asynchronously"""
        loading = self.query_one("#loading", LoadingIndicator)
        output_area = self.query_one("#output_area", Markdown)
        
        # Show loading
        loading.visible = True
        self.update_status(f"Sending to {self.selected_provider}...")
        
        try:
            # Get AI response
            response = await self.ai_client.get_response(
                self.selected_provider,
                self.selected_model,
                message
            )
            
            # Update output
            conversation = f"**You:** {message}\n\n**{self.selected_provider}:** {response}\n\n---\n\n"
            current_content = output_area.markdown
            if current_content == "Welcome! Select an AI provider and enter your API key to get started.":
                output_area.update(conversation)
            else:
                output_area.update(conversation + current_content)
            
            self.update_status("Response received!")
            
        except Exception as e:
            self.update_status(f"Error: {str(e)}")
            output_area.update(f"**Error:** {str(e)}\n\n---\n\n" + output_area.markdown)
        
        finally:
            loading.visible = False
    
    def action_clear_output(self):
        """Clear the conversation output"""
        output_area = self.query_one("#output_area", Markdown)
        output_area.update("Conversation cleared.")
        self.update_status("Conversation cleared")
    
    def update_status(self, message: str):
        """Update status bar message"""
        status_text = self.query_one("#status_text", Static)
        status_text.update(message)
    
    def update_status_info(self):
        """Update sidebar status information"""
        status_info = self.query_one("#status_info", Static)
        has_key = bool(self.config_manager.get_api_key(self.selected_provider.lower()))
        key_status = "✓" if has_key else "✗"
        
        info = f"""Provider: {self.selected_provider}
Model: {self.selected_model}
API Key: {key_status} {"Configured" if has_key else "Not set"}"""
        
        status_info.update(info)
    
    def action_quit(self):
        """Quit the application"""
        self.exit()


def main():
    """Main entry point"""
    app = AITerminalApp()
    app.run()


if __name__ == "__main__":
    main()
