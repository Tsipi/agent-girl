# agent-girl

A basic OpenAI agent built with Python.

## Quick Setup

### 1. Activate Virtual Environment

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up API Key

1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

   Get your API key from: https://platform.openai.com/api-keys

### 4. Run the Agent

```bash
python agent.py
```

Type your messages and press Enter. Type `exit` to quit.

## Project Structure

```
agent-girl/
├── agent.py          # Main agent code
├── requirements.txt  # Python dependencies
├── .env.example      # Environment variables template
├── .env              # Your actual API keys (not in git)
└── venv/             # Virtual environment (not in git)
```

## What's Installed

- **openai**: Official OpenAI Python library
- **python-dotenv**: Loads environment variables from .env file