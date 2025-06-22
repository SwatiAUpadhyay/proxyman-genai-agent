# Proxyman GenAI CLI Log Agent (Free Version)

## Overview

This tool uses the Proxyman CLI to record network traffic, then filters logs by user prompt keyword.

It does **not** require any paid OpenAI API key or access. Prompt parsing is done with simple local keyword matching.

## Requirements

- macOS with [Proxyman App installed](https://proxyman.io)
- `proxyman-cli` available in your PATH (located inside the Proxyman app bundle)
- Python 3.9+
- `python-dotenv` package

## Setup

1. Clone the repo

2. Create & activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
