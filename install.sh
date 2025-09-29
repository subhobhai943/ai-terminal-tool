#!/bin/bash

# AI Terminal Tool Installation Script
# Compatible with Linux and Termux

set -e

echo "🤖 AI Terminal Tool Installation Script"
echo "======================================"

# Function to detect the system
detect_system() {
    if [ -n "$TERMUX_VERSION" ]; then
        echo "termux"
    elif [ -f /etc/debian_version ]; then
        echo "debian"
    elif [ -f /etc/redhat-release ]; then
        echo "redhat"
    elif [ -f /etc/arch-release ]; then
        echo "arch"
    else
        echo "unknown"
    fi
}

# Function to install dependencies based on system
install_dependencies() {
    local system="$1"
    
    case "$system" in
        "termux")
            echo "📱 Detected Termux environment"
            pkg update
            pkg install -y python git
            ;;
        "debian")
            echo "🐧 Detected Debian/Ubuntu environment"
            sudo apt update
            sudo apt install -y python3 python3-pip git
            ;;
        "arch")
            echo "🏔️ Detected Arch Linux environment"
            sudo pacman -Syu --noconfirm python python-pip git
            ;;
        "redhat")
            echo "🎩 Detected RedHat/CentOS/Fedora environment"
            sudo yum install -y python3 python3-pip git || sudo dnf install -y python3 python3-pip git
            ;;
        *)
            echo "❓ Unknown system. Please install Python 3.8+, pip, and git manually."
            ;;
    esac
}

# Main installation process
main() {
    echo "🔍 Detecting system..."
    local system=$(detect_system)
    echo "System detected: $system"
    
    echo "📦 Installing system dependencies..."
    install_dependencies "$system"
    
    echo "📥 Installing Python dependencies..."
    pip install -r requirements.txt
    
    echo "🔧 Setting up the application..."
    pip install -e .
    
    echo "✅ Installation completed successfully!"
    echo ""
    echo "🚀 To run the application:"
    echo "   ai-terminal-tool"
    echo "   or"
    echo "   ait"
    echo ""
    echo "📖 For more information, see README.md"
}

# Check if requirements.txt exists
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: requirements.txt not found!"
    echo "Please run this script from the ai-terminal-tool directory."
    exit 1
fi

# Run main installation
main
