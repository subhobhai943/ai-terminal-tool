# AI Terminal Tool 🤖

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Termux Compatible](https://img.shields.io/badge/Termux-Compatible-green.svg)](https://termux.dev/)
[![Linux Compatible](https://img.shields.io/badge/Linux-Compatible-blue.svg)](https://www.linux.org/)

A beautiful, user-friendly terminal GUI application for interacting with multiple AI providers including OpenAI GPT, Anthropic Claude, Google Gemini, and Perplexity AI. No complex setup required - just install, configure your API keys, and start chatting!

## ✨ Features

- 🎨 **Beautiful Terminal GUI** - Built with Textual framework for a modern, responsive interface
- 🤖 **Multiple AI Providers** - Support for OpenAI, Claude, Gemini, and Perplexity
- 🔑 **Secure API Key Management** - Encrypted local storage of API keys  
- 🚀 **Easy Installation** - One-command installation with automatic dependency management
- 📱 **Termux Compatible** - Works perfectly on Android devices with Termux
- 🐧 **Linux Ready** - Native support for all Linux distributions
- 🌐 **Model Selection** - Choose from the latest models for each provider
- 💬 **Conversation History** - Keep track of your chat sessions
- ⌨️ **Keyboard Shortcuts** - Efficient navigation and control
- 🎯 **Lightweight** - Minimal resource usage, perfect for low-spec devices

## 🖼️ Screenshots

### Main Interface
The application features a clean, modern terminal interface with:
- Left sidebar for AI provider and model selection
- API key configuration section  
- Main chat area for conversations
- Status indicators and loading animations

### Supported AI Providers

| Provider | Models Available |
|----------|------------------|
| **OpenAI** | GPT-4o, GPT-4o-mini, GPT-3.5-turbo |
| **Anthropic Claude** | Claude 3.5 Sonnet, Claude 3.5 Haiku, Claude 3 Opus |
| **Google Gemini** | Gemini 2.0 Flash, Gemini 1.5 Pro, Gemini 1.5 Flash |
| **Perplexity** | Llama 3.1 Sonar (Small & Large), with web search |

## 🚀 Quick Start

### Option 1: Direct Installation (Recommended)

```bash
# Clone the repository
git clone https://github.com/subhobhai943/ai-terminal-tool.git
cd ai-terminal-tool

# Install dependencies
pip install -r requirements.txt

# Run the application
python ai_terminal_tool.py
```

### Option 2: Package Installation

```bash
# Install as a package
pip install -e .

# Run from anywhere
ai-terminal-tool
# or use the short alias
ait
```

## 📦 Installation on Different Platforms

### 🐧 Linux (Ubuntu/Debian)
```bash
# Update package list
sudo apt update

# Install Python and pip if not already installed
sudo apt install python3 python3-pip git

# Clone and install
git clone https://github.com/subhobhai943/ai-terminal-tool.git
cd ai-terminal-tool
pip3 install -r requirements.txt

# Run the application
python3 ai_terminal_tool.py
```

### 📱 Termux (Android)
```bash
# Update Termux packages
pkg update && pkg upgrade

# Install required packages
pkg install python git

# Clone and install
git clone https://github.com/subhobhai943/ai-terminal-tool.git
cd ai-terminal-tool
pip install -r requirements.txt

# Run the application
python ai_terminal_tool.py
```

### 🎯 Arch Linux
```bash
# Install dependencies
sudo pacman -S python python-pip git

# Clone and install
git clone https://github.com/subhobhai943/ai-terminal-tool.git
cd ai-terminal-tool
pip install -r requirements.txt --user

# Run the application
python ai_terminal_tool.py
```

## ⚙️ Configuration

### Setting up API Keys

The application will guide you through setting up API keys for each provider:

1. **Select your preferred AI provider** from the dropdown
2. **Enter your API key** in the secure input field
3. **Click "Save API Key"** to store it locally (encrypted)
4. **Start chatting!**

### Getting API Keys

| Provider | How to Get API Key |
|----------|-------------------|
| **OpenAI** | Visit [OpenAI Platform](https://platform.openai.com/api-keys) |
| **Anthropic** | Visit [Anthropic Console](https://console.anthropic.com/) |
| **Google** | Visit [Google AI Studio](https://makersuite.google.com/app/apikey) |
| **Perplexity** | Visit [Perplexity AI](https://www.perplexity.ai/settings/api) |

### Configuration Files

API keys are stored in: `~/.ai-terminal-tool/config.json`

## 🎮 Usage Guide

### Basic Usage
1. **Launch** the application: `python ai_terminal_tool.py`
2. **Select** an AI provider from the dropdown menu
3. **Choose** a model variant
4. **Enter** your API key and save it
5. **Type** your message in the text area
6. **Press** Enter or click "Send" to get a response

### Keyboard Shortcuts
- `Ctrl+Q` - Quit application
- `Ctrl+C` - Clear conversation
- `Enter` - Send message (when in input area)

### Advanced Features
- **Provider Switching**: Change AI providers anytime during conversation
- **Model Selection**: Choose different models based on your needs
- **Conversation Management**: Clear conversation history as needed
- **Status Monitoring**: Real-time status updates and error handling

## 🛠️ Development

### Project Structure
```
ai-terminal-tool/
├── ai_terminal_tool.py      # Main application
├── requirements.txt         # Python dependencies  
├── setup.py                # Package configuration
├── README.md               # Documentation
├── LICENSE                 # MIT License
└── .gitignore             # Git ignore rules
```

### Dependencies Explained
- **textual**: Modern terminal UI framework
- **rich**: Advanced terminal formatting
- **openai**: OpenAI API client
- **anthropic**: Anthropic Claude API client
- **google-generativeai**: Google Gemini API client
- **requests**: HTTP requests for Perplexity API

### Contributing
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a Pull Request

## 🔧 Troubleshooting

### Common Issues

**Issue**: "Module not found" error
```bash
# Solution: Install missing dependencies
pip install -r requirements.txt
```

**Issue**: API key not working
- Verify the API key is correct
- Check if your API account has sufficient credits
- Ensure the API key has appropriate permissions

**Issue**: Terminal display problems
```bash
# Solution: Update terminal or try different terminal
# For Termux users:
pkg install ncurses-utils
```

**Issue**: Permission denied on Linux
```bash
# Solution: Install to user directory
pip install -r requirements.txt --user
```

### Termux Specific Tips
- Use a terminal with good Unicode support
- Ensure storage permissions are granted
- Consider using Termux:API for enhanced features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support

- 📫 **Issues**: [GitHub Issues](https://github.com/subhobhai943/ai-terminal-tool/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/subhobhai943/ai-terminal-tool/discussions)
- 📧 **Email**: developer@example.com

## 🌟 Acknowledgments

- Built with [Textual](https://textual.textualize.io/) - Amazing Python TUI framework
- Powered by [Rich](https://rich.readthedocs.io/) - Beautiful terminal formatting
- Inspired by the need for a unified AI interface

## 🔮 Roadmap

- [ ] Support for more AI providers (Cohere, Hugging Face)
- [ ] Chat history persistence
- [ ] Configuration profiles
- [ ] Plugin system
- [ ] Voice input/output support
- [ ] Export conversations
- [ ] Custom themes
- [ ] Multi-language support

---

**⭐ If you find this tool helpful, please star the repository!**

Made with ❤️ for the AI and terminal enthusiast community.
