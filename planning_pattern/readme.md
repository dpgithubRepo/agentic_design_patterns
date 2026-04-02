# 🧠 Planning Pattern Agent (LangChain + OpenAI)

This project demonstrates the **Planning Agentic Design Pattern** using LangChain and OpenAI.
Instead of directly answering a query, the system first **creates a plan**, then **executes each step sequentially**, and finally combines the results into a structured output.

---

## 🚀 Features

* 🧠 **Planning Pattern**

  * Breaks complex tasks into step-by-step plans

* ⚙️ **Step-by-Step Execution**

  * Executes each step individually using an LLM

* 🔄 **Chain-based Architecture**

  * Uses LangChain prompt chaining (`planner → executor`)

* 📊 **Structured Output**

  * Produces detailed and explainable results

---

## 🏗️ Project Structure

```bash
planning-agent/
│
├── planning_agent.py   # Main script
├── .env                # API key (not committed)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install langchain langchain-openai python-dotenv
```

---

### 2️⃣ Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=sk-your_actual_api_key_here
```

> ⚠️ Do not commit `.env` to version control

---

### 3️⃣ Run the Script

```bash
python planning_agent.py
```

---

## 💻 Usage

Update the input task in `planning_agent.py`:

```python
user_task = "Analyze whether investing in Reliance is a good idea"
```

---

## 🔧 How It Works

### Step 1: Planning

The LLM generates a structured plan:

```text
1. Gather company overview
2. Analyze financial performance
3. Evaluate risks
4. Provide recommendation
```

---

### Step 2: Execution

Each step is executed sequentially using the executor chain:

```text
Step → LLM → Result
```

---

### Step 3: Aggregation

All results are combined into a final structured response.

---

## 🧠 Architecture

```text
User Input
   ↓
Planner (LLM creates steps)
   ↓
Executor (runs each step)
   ↓
Combine results
   ↓
Final Output
```

---

## 📊 Example Output

```text
📋 Plan:
1. Gather company overview
2. Analyze financials
3. Evaluate risks
4. Provide recommendation

📊 Final Output:
Reliance is a large conglomerate...
The company shows strong financial growth...
However, risks include...
Overall, it is a moderate-to-strong investment option.
```

---

## 📌 When to Use This Pattern

Use the Planning Pattern when:

* Tasks are **complex and multi-step**
* Order of execution matters
* You need **structured reasoning**
* Transparency and explainability are important

---

## ⚠️ Limitations

* Depends on correct plan formatting (numbered steps)
* Slower than single prompt (multiple LLM calls)
* May require refinement for edge cases

---

## 🚀 Future Enhancements

* 🔧 Add external tools (stock API, search)
* 🔀 Combine with routing pattern
* 🧠 Add reflection step for improved output
* 📡 Convert into FastAPI service
* 💾 Add memory for multi-turn tasks

---

## 📦 Tech Stack

* Python
* LangChain
* OpenAI API
* python-dotenv

---

## 🔐 Security

* Store API keys in `.env`
* Add `.env` to `.gitignore`

```bash
.env
```

---

## 🧠 Key Concept

> Planning Pattern = Think first, then act step-by-step

This approach improves reasoning, accuracy, and control in AI systems.

---

## 🤝 Contributing

Feel free to fork and improve this project!

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

Built using LangChain and OpenAI to demonstrate the **Planning Agentic Pattern** in real-world AI workflows.
