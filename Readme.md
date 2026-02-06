# AI Operation Assistance Backend

An agent-based AI backend that plans tasks using an LLM, executes real-world tools (GitHub & Weather APIs), verifies results, and returns clean structured output.

This project demonstrates a **Planner → Executor → Verifier** architecture with strong validation, tool abstraction, alias handling, and robust exception management.

---

## Features

- LLM-driven task planning (Gemini)
- Deterministic tool execution (no hallucinated actions)
- Real API integrations (GitHub Search, OpenWeather)
- Tool alias normalization (LLM-safe)
- Centralized exception handling
- Clean JSON-only responses
- Extensible agent & tool architecture

---

## Architecture Overview

```bash
    Client
       |
       v
 FastAPI (/run-task)
       |
       v
  Orchestrator
       |
       ├── PlannerAgent → LLM (Gemini)
       |
       ├── ExecutorAgent → Tools (GitHub, Weather)
       |
       └── VerifierAgent → Validation + Formatting
```

### Agents

- **PlannerAgent**
  - Converts natural language tasks into a strict JSON execution plan using Gemini
  - Enforces schema validation (`tool`, `action`, `params`)

- **ExecutorAgent**
  - Normalizes tool aliases produced by LLMs
  - Executes real APIs via tool adapters
  - Returns structured, ordered results

- **VerifierAgent**
  - Ensures execution completeness
  - Validates non-empty outputs
  - Produces final user-facing JSON

### Tools

- **GitHubTool**
  - Searches public repositories using GitHub REST API
- **WeatherTool**
  - Fetches live weather data using OpenWeather API

All tools inherit from a common `BaseTool` with retry logic.

---

## Tech Stack

- **Backend**: FastAPI
- **Language**: Python 3.10+
- **LLM**: Google Gemini (`google-genai`)
- **HTTP Client**: `requests`
- **Server**: Uvicorn

---

## Setup Instructions (Localhost)

### 1 Clone the repository

```bash
git clone https://github.com/saurabh-develop/AI-Operation-Assistant.git
cd ai-operation-assistance/backend_ai
```

### 2 Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
# venv\Scripts\activate    # Windows
```

### 3 Install dependencies

```bash
pip install -r requirements.txt
```

### 4 Configure environment variables

```bash
cp .env.example .env
```

### 5 Run the server

```bash
uvicorn main:app --reload
```

Server will be available at:

```bash
http://127.0.0.1:5001
```

---

### Environment Variables (.env.example)

```bash
# Gemini LLM
GEMINI_API_KEY=your_gemini_api_key_here

# GitHub API
GITHUB_TOKEN=your_github_personal_access_token

# OpenWeather API
WEATHER_API_KEY=your_openweather_api_key
```

### 🧪 Example Prompts to Test

```bash
Send a POST request to /run-task with a JSON body:
{
  "task": "Find popular Python repositories and check weather in Bangalore"
}
```

More Examples

1. GitHub only

   ```bash
   Find top React repositories on GitHub
   ```

2. Weather only

   ```bash
   What is the weather in New York today?
   ```

3. Multi-step task

   ```bash
   Search GitHub for FastAPI projects and tell me the weather in London
   ```

4. Alias robustness

   ```bash
   Lookup popular Node.js repos and show weather for Mumbai
   ```

5. Natural phrasing

   ```bash
   Can you check the weather in Paris and also find trending Python repos?
   ```

---

### Known Limitations & Tradeoffs

1. LLM quota limits
   - Gemini free tier has strict rate limits (20 req/min/model)

   - Planner & Verifier calls consume quota

2. No streaming
   - Responses are returned only after full execution

3. Synchronous execution
   - Tools currently run sequentially (can be parallelized)

4. Strict JSON enforcement
   - Planner failures occur if LLM returns malformed JSON

5. Limited tools
   - Only GitHub Search & Weather APIs are integrated (by design)
