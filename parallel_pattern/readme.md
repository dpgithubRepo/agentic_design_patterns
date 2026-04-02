# ✈️ Parallel Travel Planner (LangChain + OpenAI)

An AI-powered travel planner built using the **Parallel Design Pattern** with LangChain and OpenAI.
This project demonstrates how multiple independent tasks—like itinerary creation, budget estimation, hotel suggestions, and activity planning—can be executed **simultaneously** to generate a complete travel plan.

---

## 🚀 Features

* ⚡ **Parallel Execution**

  * Runs multiple LLM tasks at the same time using LangChain’s `RunnableParallel`

* 🧠 **Multi-Dimensional Planning**

  * Itinerary generation
  * Budget estimation
  * Hotel recommendations
  * Activity suggestions

* 🔐 **Secure API Handling**

  * Uses `.env` for API keys
  * Centralized configuration

* 🧩 **Modular & Extensible**

  * Easily add new travel components (transport, weather, visa info)

---

## 🏗️ Project Structure

```bash
travel-planner/
│
├── travel_parallel.py     # Main script (parallel execution)
├── .env                   # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/travel-planner.git
cd travel-planner
```

---

### 2️⃣ Install Dependencies

```bash
pip install langchain langchain-openai python-dotenv
```

---

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-your_actual_api_key_here
```

> ⚠️ Never commit your `.env` file

---

### 4️⃣ Run the Application

```bash
python travel_parallel_planer.py
```

---

## 💻 Usage

Modify input inside `travel_parallel.py`:

```python
user_input = {
    "destination": "Goa",
    "days": "3",
    "budget": "₹15000"
}
```

---

## 🧾 Sample Output

```
✈️ Travel Plan

🗺️ Itinerary:
Day 1: Beaches & Forts  
Day 2: Water sports  
Day 3: Markets  

💰 Budget:
Stay: ₹6000  
Food: ₹3000  
Travel: ₹4000  

🏨 Hotels:
Zostel Goa, Treebo Trend  

🎯 Activities:
Baga Beach, Parasailing  
```

---

## ⚡ How Parallel Pattern Works

1. User input is passed to multiple chains
2. Each chain performs a specific task independently
3. All tasks run **simultaneously**
4. Results are combined into a final response

---

## 🧠 Why Parallel Pattern?

* Faster execution compared to sequential workflows
* Better specialization (each task focuses on one goal)
* Scalable for complex real-world applications

---

## 📌 When to Use

Use this pattern when:

* Tasks are independent
* Multiple insights are needed simultaneously
* Performance and speed are critical

---

## 🚀 Future Enhancements

* 🌐 Integrate real APIs (Google Maps, hotel pricing)
* 🧠 Add personalization (user preferences)
* 🔀 Combine with routing pattern
* 💾 Add memory for past trips
* 📱 Build UI (chat-based travel planner)

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

## 🤝 Contributing

Feel free to fork this repo and enhance the planner!

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

Built using LangChain and OpenAI, showcasing the power of the **Parallel Design Pattern** in real-world AI applications.
