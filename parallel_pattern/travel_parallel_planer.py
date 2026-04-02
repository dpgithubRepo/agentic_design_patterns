import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel


# ---------------------------
# 🔐 Load environment
# ---------------------------
load_dotenv()

# ---------------------------
# 🤖 Initialize LLM
# ---------------------------
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)




# 🗺️ Itinerary Planner
itinerary_prompt = ChatPromptTemplate.from_template(
    "Create a {days}-day travel itinerary for {destination} within budget {budget}."
)
itinerary_chain = itinerary_prompt | llm


# 💰 Budget Estimator
budget_prompt = ChatPromptTemplate.from_template(
    "Estimate total cost breakdown (stay, food, travel) for a {days}-day trip to {destination} under {budget}."
)
budget_chain = budget_prompt | llm


# 🏨 Hotel Suggestions
hotel_prompt = ChatPromptTemplate.from_template(
    "Suggest 3 budget-friendly hotels in {destination} within {budget} range."
)
hotel_chain = hotel_prompt | llm


# 🎯 Activities / Attractions
activities_prompt = ChatPromptTemplate.from_template(
    "List top attractions and activities to do in {destination} for {days} days."
)
activities_chain = activities_prompt | llm


# ---------------------------
# ⚡ Parallel Execution
# ---------------------------
parallel_chain = RunnableParallel(
    itinerary=itinerary_chain,
    budget=budget_chain,
    hotels=hotel_chain,
    activities=activities_chain
)

# ---------------------------
# ▶️ Run
# ---------------------------
if __name__ == "__main__":
    user_input = {
        "destination": "Goa",
        "days": "3",
        "budget": "₹15000"
    }

    result = parallel_chain.invoke(user_input)

    print("\n✈️ Travel Plan (Parallel Output)\n")

    print("🗺️ Itinerary:\n", result["itinerary"].content)
    print("\n💰 Budget:\n", result["budget"].content)
    print("\n🏨 Hotels:\n", result["hotels"].content)
    print("\n🎯 Activities:\n", result["activities"].content)