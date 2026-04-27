# Voice-Based AI Agent with Memory & Tools

A voice-enabled AI agent that manages To-Do lists using tools and remembers important past interactions. **Runs 100% locally with NO API key required!**

## Features

- 🆓 **100% Free**: No API costs, runs completely on your computer
- 🔒 **Privacy First**: All data stays local, nothing sent to cloud
- ✅ **To-Do Management**: Add, update, delete, and list tasks
- 🧠 **Memory System**: Stores and recalls important user interactions
- 🤖 **Intelligent Agent**: Decides when to use tools vs respond conversationally
- 🦙 **Powered by Ollama**: Uses local Llama 3.2 model

## System Requirements

- Python 3.8+
- Ollama (free local LLM)
- 8GB RAM minimum (16GB recommended)
- 10GB free disk space

## Quick Start (2 Minutes!)

### 1. Install Ollama
Download from: https://ollama.ai

### 2. Download AI Model
```bash
ollama pull llama3.2
```

### 3. Install Python Dependencies
```bash
pip install -r requirements_simple.txt
```

### 4. Run the Agent
```bash
python quick_start_simple.py
```

## Usage Examples

Simple command format:
```
add: Buy groceries tomorrow
list
done: 1
remember: My favorite color is blue
recall
quit
```

See `DEMO_EXAMPLES.md` for complete demo scripts!

## Project Structure

```
voice-ai-agent/
├── quick_start_simple.py   # Main application (START HERE!)
├── agent/
│   ├── core_local.py      # Agent logic with Ollama
│   ├── prompt.py          # System prompt definition
│   └── tools.py           # Tool implementations (CRUD + Memory)
├── memory/
│   └── store.py           # Memory utilities
├── data/
│   ├── todos.json         # To-Do list storage (auto-created)
│   └── memory.json        # Memory storage (auto-created)
├── requirements_simple.txt # Dependencies
├── DEMO_EXAMPLES.md       # Complete demo scripts
└── README.md              # This file
```

## How It Works

### Local LLM (Ollama + Llama 3.2)
- Runs completely on your computer
- No internet required (after initial download)
- Privacy-focused, no data sent to cloud

### Tool System (6 Tools)
- **add_todo**: Add new tasks with optional due dates and priority
- **list_todos**: View all tasks with filtering options
- **update_todo**: Modify existing tasks (mark complete, change priority)
- **delete_todo**: Remove completed or unwanted tasks
- **save_memory**: Store important user information with categories
- **recall_memory**: Retrieve past interactions by query or category

### Memory System
- Categorized storage (personal, preference, event, goal, general)
- Search by content or category
- Persistent JSON storage

### Agent Intelligence
- Analyzes user intent using Llama 3.2
- Decides when to use tools vs respond conversationally
- Maintains conversation context
- Provides natural, helpful responses

## For Your Demo Video

See `QUICK_START_GUIDE.md` for detailed demo instructions including:
- What to show (code + live demo)
- What to say
- Recording tips
- Troubleshooting

## License

MIT License
