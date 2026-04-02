import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# ---------------------------
# 🔐 Load env
# ---------------------------
load_dotenv()

# ---------------------------
# 🤖 LLM
# ---------------------------
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# ---------------------------
# 🧠 Step 1: Planner
# ---------------------------
planner_prompt = ChatPromptTemplate.from_template("""
You are a planner.

Break down the following task into clear numbered steps.

Task:
{task}
""")

planner_chain = planner_prompt | llm


# ---------------------------
# ⚙️ Step 2: Executor
# ---------------------------
executor_prompt = ChatPromptTemplate.from_template("""
You are an executor.

Given the overall task and a step, execute that step clearly.

Task: {task}
Step: {step}
""")

executor_chain = executor_prompt | llm


# ---------------------------
# ▶️ Run Planning Pattern
# ---------------------------
def run_planner(task: str):
    print("\n🧠 Generating Plan...\n")

    # Step 1: Generate plan
    plan_response = planner_chain.invoke({"task": task})
    plan_text = plan_response.content

    print("📋 Plan:\n", plan_text)

    # Convert plan into steps
    steps = [
        line for line in plan_text.split("\n")
        if line.strip() and line[0].isdigit()
    ]

    print("\n⚙️ Executing Steps...\n")

    results = []

    # Step 2: Execute each step
    for step in steps:
        print(f"➡️ {step}")

        result = executor_chain.invoke({
            "task": task,
            "step": step
        })

        output = result.content
        results.append(output)

        print("✅ Result:", output, "\n")

    # Step 3: Combine results
    final_output = "\n".join(results)

    return final_output


# ---------------------------
# ▶️ Main
# ---------------------------
if __name__ == "__main__":
    user_task = "Analyze whether investing in Reliance is a good idea"

    final_answer = run_planner(user_task)

    print("\n📊 Final Output:\n", final_answer)