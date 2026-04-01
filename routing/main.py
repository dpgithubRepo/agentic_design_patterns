from router import route_query
from agents.code_agent import code_agent
from agents.general_agent import general_agent
from agents.tool_agent import tool_agent



import os

# ---------------------------
# 🧠 ORCHESTRATOR
# ---------------------------
def handle_query(user_input: str) -> str:
    """
    Main orchestrator:
    - Routes query
    - Calls appropriate agent
    """

    route = route_query(user_input)

    print(f"[DEBUG] Selected route: {route}")

    if route == "code":
        return code_agent(user_input)

    elif route == "tool":
        return tool_agent(user_input)

    elif route == "general":
        return general_agent(user_input)

    # fallback (safety)
    return general_agent(user_input)


# ---------------------------
# ▶️ CLI LOOP
# ---------------------------
def run_cli():
    print(print(os.getenv("OPENAI_API_KEY")))
    print("🤖 AI Assistant (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye 👋")
            break

        if not user_input:
            continue

        try:
            response = handle_query(user_input)
            print(f"AI: {response}\n")

        except KeyboardInterrupt:
            print("\nExiting... 👋")
            break

        except Exception as e:
            print(f"⚠️ Error: {str(e)}\n")


# ---------------------------
# 🚀 ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    run_cli()