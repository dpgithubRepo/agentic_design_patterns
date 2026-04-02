import os
from dotenv import load_dotenv
from openai import OpenAI
import yfinance as yf
import json

# ---------------------------
# 🔐 Load env
# ---------------------------
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------------------------
# 🔧 Tool Function
# ---------------------------
def get_stock_price(symbol: str):
    try:
        import yfinance as yf
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")

        if not data.empty:
            price = data["Close"].iloc[-1]
            return f"{symbol} is trading at {price}"

        return "No data available"

    except Exception:
        return f"{symbol} price temporarily unavailable (Yahoo issue)"


# ---------------------------
# 🧠 Tool Definition (IMPORTANT)
# ---------------------------
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Get current stock price (e.g., AAPL, RELIANCE.NS)",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "Stock symbol"
                    }
                },
                "required": ["symbol"]
            }
        }
    }
]

# ---------------------------
# ▶️ Run Agent
# ---------------------------
def run_agent(user_input: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}],
        tools=tools
    )

    message = response.choices[0].message

    # If tool is called
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)

        result = get_stock_price(args["symbol"])

        # Send result back to LLM
        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input},
                message,
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                }
            ]
        )

        return final_response.choices[0].message.content

    return message.content


# ---------------------------
# ▶️ Main
# ---------------------------
if __name__ == "__main__":
    query = "What is the price of RELIANCE.NS?"

    answer = run_agent(query)

    print("\n📈 Answer:\n", answer)