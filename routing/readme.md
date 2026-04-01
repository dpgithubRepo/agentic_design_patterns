# 🤖 Agentic Routing AI Assistant (OpenAI)

A modular AI assistant built using **agentic design patterns (routing)** with OpenAI APIs.
This project demonstrates how to route user queries dynamically to specialized agents like **code generation, general Q&A, and tool execution**.

---

## 🚀 Features

* 🔀 **LLM-based Routing**

  * Classifies user intent into:

    * `code`
    * `general`
    * `tool`

* 🧠 **Multi-Agent Architecture**

  * Code Agent → handles programming tasks
  * General Agent → handles Q&A
  * Tool Agent → handles external tools (e.g., weather)

* 🔐 **Secure API Key Handling**

  * Uses `.env` + `python-dotenv`
  * Centralized client via `config.py`

* 🧩 **Modular Design**

  * Easy to extend with new agents (RAG, finance, etc.)

---

## 🏗️ Project Structure

```
routing/
│
├── main.py                # Entry point (CLI app)
├── router.py              # LLM-based routing logic
├── config.py              # Centralized OpenAI client
├── .env                   # API keys (not committed)
│
├── agents/
│   ├── __init__.py
│   ├── code_agent.py
│   ├── general_agent.py
│   └── tool_agent.py
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-router.git
cd ai-router
```

---

### 2️⃣ Install Dependencies

```bash
pip install openai python-dotenv
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-your_actual_api_key_here
MODEL=gpt-4.1
```

> ⚠️ Do NOT commit `.env` to version control

---

### 4️⃣ Run the Application

```bash
python main.py
```

---

## 💻 Usage

Example interaction:

```
You: write a python function for fibonacci
→ Routed to: code_agent

You: what is mutual fund
→ Routed to: general_agent

You: what is the weather today
→ Routed to: tool_agent
```

---

## 🔀 How Routing Works

1. User input is passed to **router.py**
2. LLM classifies intent using structured output
3. Based on route:

   * `code` → `code_agent`
   * `general` → `general_agent`
   * `tool` → `tool_agent`
4. Response is returned to user

---

## 🧠 Core Concept: Agentic Routing

Instead of hardcoding logic, the system uses an LLM to:

* Understand intent
* Decide execution path
* Delegate tasks dynamically

This is a foundational pattern in modern AI systems.

---

## 🧩 Agents Overview

### 🧑‍💻 Code Agent

* Writes code
* Debugs issues
* Explains logic

### 💬 General Agent

* Answers questions
* Explains concepts
* Handles conversational queries

### 🔧 Tool Agent

* Executes external functions
* Example: weather API (mock)

---

## 🔐 Security Best Practices

* Use `.env` for secrets
* Never hardcode API keys
* Add `.env` to `.gitignore`

```bash
.env
```

---

## 🚀 Future Enhancements

* 📚 RAG (Retrieval-Augmented Generation)
* 📈 Stock market agent (finance routing)
* 🌐 FastAPI backend
* 💾 Memory (conversation history)
* 🧠 Multi-agent planner (advanced orchestration)

---

## 🧪 Debugging Tips

* Ensure `.env` is loaded correctly
* Verify API key is valid
* Check for accidental hardcoded keys
* Use logging for route decisions

---

## 📦 Tech Stack

* Python
* OpenAI API
* python-dotenv

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork and enhance the system.

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

Built using OpenAI APIs and agentic design patterns.
