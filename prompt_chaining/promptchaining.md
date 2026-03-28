
# 🚀 AI Resume–Job Matcher using Prompt Chaining

## 📌 Overview

This project is an **AI-powered Resume–Job Matching System** built using **LangChain and OpenAI**.
It analyzes a candidate's resume against a job description, identifies skill gaps, and generates a personalized learning plan.

The system uses **prompt chaining**, where multiple LLM steps are executed sequentially to achieve accurate and structured results.

---

## 🧠 How It Works

The pipeline follows a **multi-step AI workflow**:

```
Resume + Job Description
        ↓
Extract Skills (LLM)
        ↓
Normalize Skills (LLM)
        ↓
Compare Skills (LLM)
        ↓
Identify Missing Skills
        ↓
Generate Learning Plan
```

---

## ⚙️ Core Components

### 1. File Input

```python
def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
```

* Reads resume and job description from `.txt` files
* Converts them into plain text for processing

---

### 2. Skill Extraction

```python
jd_extract_chain = prompt_extract_job_requirement | llm | parser
resume_extract_chain = prompt_extract_resume | llm | parser
```

* Uses LLM to extract:

  * Technical skills
  * Soft skills
  * Tools & technologies
* Outputs structured JSON

---

### 3. Skill Normalization

```python
normalize_chain = prompt_normalize | llm | parser
```

* Standardizes skill names (e.g., "py" → "python")
* Removes duplicates
* Converts to consistent format

---

### 4. Skill Comparison

```python
compare_chain = prompt_compare | llm | parser
```

* Compares resume vs job requirements
* Generates:

  * Matched skills
  * Missing skills
  * Extra skills
  * Match percentage

---

### 5. Learning Plan Generation

* Based on missing skills, the system generates:

  * Learning roadmap
  * Timeline
  * Resources
  * Project ideas

---

## 🔗 Prompt Chaining (Key Concept)

This project uses **prompt chaining**, where:

```python
prompt → LLM → parser
```

Each step:

* Takes input
* Processes it using the LLM
* Passes output to the next step

### Why Prompt Chaining?

* ✅ Better accuracy
* ✅ Easier debugging
* ✅ Modular design
* ✅ Reusable components

---

## 🧪 Example Output

```json
{
  "matched_skills": ["python", "aws"],
  "missing_skills": ["kubernetes", "docker"],
  "match_percentage": 70
}
```

---

## 💡 Features

* 📄 Resume & JD file input
* 🤖 Multi-step AI processing
* 📊 Skill gap analysis
* 📈 Match scoring
* 🧠 Personalized learning plan

---

## 🚀 Tech Stack

* Python
* LangChain
* OpenAI GPT models
* dotenv

---

## 🔥 Future Improvements

* Streamlit UI for file upload
* CrewAI multi-agent architecture
* Vector database for large documents
* Real-time job matching API

---

## 🧠 Key Takeaway

This project demonstrates how **LLMs can be orchestrated using prompt chaining** to build real-world AI applications that go beyond simple chat and deliver actionable insights.

---

## 👨‍💻 Author

Built by Durga Prasad
