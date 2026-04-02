# 📈 Stock Price AI Agent (Tool Use Pattern with OpenAI)

This project demonstrates the **Tool Use Agentic Pattern** using OpenAI APIs and Python.
The agent can **dynamically call a tool (function)** to fetch real-time stock prices using `yfinance`.

---

## 🚀 Features

* 🔧 **Tool Use Pattern**

  * LLM decides when to call a function (`get_stock_price`)

* 📈 **Real-Time Stock Data**

  * Fetches live stock prices using `yfinance`

* 🧠 **OpenAI Tool Calling**

  * Uses function calling via OpenAI API (no LangChain)

* 🛡️ **Error Handling**

  * Gracefully handles API failures (e.g., Yahoo downtime)

* ⚡ **Lightweight Implementation**

  * No external frameworks like LangChain

---

## 🏗️ Project Structure

```bash
tool-use-stock-agent/
│
├── tool_use.py       # Main agent script
├── .env              # API key (not committed)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install openai python-dotenv yfinance
```

---

### 2️⃣ Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=sk-your_actual_api_key_here
```

> ⚠️ Never commit your `.env` file

---

### 3️⃣ Run the Script

```bash
python tool_use.py
```

---

## 💻 Usage

Update the query in `tool_use.py`:

```python
query = "What is the price of RELIANCE.NS?"
```

---

## 🔧 How It Works

1. User sends a query
2. OpenAI model analyzes the query
3. If needed, it calls the tool (`get_stock_price`)
4. Python executes the function
5. Result is sent back to the model
6. Final response is generated

---

## 🧠 Tool Definition

The tool is defined as a function:

```python
def get_stock_price(symbol: str):
```

And exposed to the LLM via:

```python
tools = [
    {
        "type": "function",
        "function": {...}
    }
]
```

---

## 📊 Example Output

```text
📈 Answer:
RELIANCE.NS is trading at 2450.50
```

---

## ⚠️ Notes

* Use `.NS` suffix for Indian stocks:

  * RELIANCE.NS
  * TCS.NS

* `yfinance` depends on Yahoo Finance:

  * May fail if Yahoo is down
  * Fallback handling is included

---

## 🚀 Future Enhancements

* 🔁 Add fallback APIs (Finnhub, Polygon)
* 🌦️ Add more tools (weather, news, portfolio)
* 🔀 Combine with routing pattern
* ⚡ Add parallel analysis (price + sentiment + news)
* 🌐 Build FastAPI backend

---

## 📦 Tech Stack

* Python
* OpenAI API
* yfinance
* python-dotenv

---

## 🔐 Security

* Store secrets in `.env`
* Add `.env` to `.gitignore`

```bash
.env
```

---

## 🧠 Key Concept

> LLM = Decision Maker
> Tool = Execution Layer

This pattern allows AI systems to **interact with real-world data instead of relying only on static knowledge**.

---

## 🤝 Contributing

Feel free to fork and enhance this project!

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

Built using OpenAI APIs demonstrating the **Tool Use Agentic Pattern** in a real-world scenario.
