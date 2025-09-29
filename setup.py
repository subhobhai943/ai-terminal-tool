#!/usr/bin/env python3
"""
Setup script for AI Terminal Tool
"""
import os
from setuptools import setup, find_packages

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="ai-terminal-tool",
    version="1.0.0",
    author="AI Terminal Tool Developer",
    author_email="developer@example.com",
    description="Easy-to-use GUI terminal tool for multiple AI providers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/subhobhai943/ai-terminal-tool",
    packages=find_packages(),
    py_modules=["ai_terminal_tool"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "ai-terminal-tool=ai_terminal_tool:main",
            "ait=ai_terminal_tool:main",  # Short alias
        ],
    },
    keywords=[
        "ai", "terminal", "gui", "openai", "anthropic", "claude", 
        "gemini", "perplexity", "chatgpt", "artificial intelligence", 
        "tui", "textual", "command-line"
    ],
    project_urls={
        "Bug Reports": "https://github.com/subhobhai943/ai-terminal-tool/issues",
        "Source": "https://github.com/subhobhai943/ai-terminal-tool",
        "Documentation": "https://github.com/subhobhai943/ai-terminal-tool#readme",
    },
)
