# Quick Start Guide 🏁

Get up and running with AI Terminal Tool in less than 5 minutes!

## 🚀 Installation (Choose One)

### Option 1: Automated Installation (Recommended)
```bash
# Clone and auto-install
git clone https://github.com/subhobhai943/ai-terminal-tool.git
cd ai-terminal-tool
chmod +x install.sh
./install.sh
```

### Option 2: Manual Installation
```bash
# Clone repository
git clone https://github.com/subhobhai943/ai-terminal-tool.git
cd ai-terminal-tool

# Install dependencies
pip install -r requirements.txt

# Run directly
python ai_terminal_tool.py
```

### Option 3: Package Installation
```bash
# Install as package
pip install -e .

# Run from anywhere
ai-terminal-tool
# or short alias
ait
```

## 🔑 API Key Setup

### 1. Get your API keys:
- **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Claude**: [console.anthropic.com](https://console.anthropic.com/)
- **Gemini**: [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)
- **Perplexity**: [perplexity.ai/settings/api](https://www.perplexity.ai/settings/api)

### 2. Configure in the app:
1. Launch the application
2. Select your AI provider from dropdown
3. Enter your API key in the secure field
4. Click "Save API Key"
5. Start chatting!

## 💬 Usage Examples

#### Basic Chat
```
You: Explain quantum computing in simple terms
AI: [Response from selected provider]
```

#### Code Help
```
You: Write a Python function to calculate fibonacci numbers
AI: [Code example with explanation]
```

#### Research & Analysis
```
You: What are the latest developments in renewable energy?
AI: [Current information with sources - especially good with Perplexity]
```

## ⌨️ Keyboard Shortcuts

- `Ctrl + Q` - Quit application
- `Ctrl + C` - Clear conversation
- `Enter` - Send message (when in text area)
- `Tab` - Navigate between interface elements

## 🔧 Quick Troubleshooting

**App won't start?**
```bash
pip install --upgrade textual rich
```

**API key not working?**
- Double-check the key format
- Ensure account has credits/access
- Try regenerating the key

**Display issues in Termux?**
```bash
pkg install ncurses-utils
export TERM=xterm-256color
```

**Permission errors?**
```bash
pip install --user -r requirements.txt
```

## 🎨 Interface Overview

```
┌────────────────────────────────────────────────────────────────────────────┐
│ AI Terminal Tool                    [Clock]  │
├────────────────────────────────────────────────────────────────────────────┤
│ ┌─ SETTINGS ──────────────────────────────────────────────────────────────┐ │
│ │ Provider: [OpenAI ▼]        │ ┌─ CHAT ──────────────────────────────────────────────────────────┐ │
│ │ Model: [GPT-4o ▼]            │ │ Your Message:                        │ │
│ │ API Key: [••••••••••••••••]      │ │ [Text input area]                   │ │
│ │ [Save Key]                   │ │ [Send]                              │ │
│ │                              │ ├──────────────────────────────────────────────────────────┤ │
│ │ [Clear Chat]                 │ │ AI Response:                        │ │
│ │                              │ │                                     │ │
│ │ Status: ✓ OpenAI Ready        │ │ [Conversation area with markdown]   │ │
│ └──────────────────────────────┘ │                                     │ │
│                                   └──────────────────────────────────────────────────────────┘ │
├────────────────────────────────────────────────────────────────────────────┤
│ Status: Ready | Loading: ● | Ctrl+Q=Quit       │
└────────────────────────────────────────────────────────────────────────────┘
```

## 🎆 Next Steps

1. **Explore Providers**: Try different AI models to see their strengths
2. **Save Conversations**: Use Clear button to manage chat history
3. **Customize**: Check `config.example.json` for advanced options
4. **Get Help**: See [README.md](README.md) for detailed documentation
5. **Report Issues**: Found a bug? [Create an issue](https://github.com/subhobhai943/ai-terminal-tool/issues)

---

**Happy chatting! 🤖✨**
