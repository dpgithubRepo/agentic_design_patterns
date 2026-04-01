from dotenv import load_dotenv
from openai import OpenAI
from config import client

def get_weather(city: str) -> str:
    """
    Mock weather tool (replace with real API)
    """
    return f"Weather in {city}: 28°C, Sunny ☀️"


def tool_agent(query: str) -> str:
    """
    Handles tool-based queries:
    - weather
    - APIs
    - external data
    """

    query_lower = query.lower()

    # 🔹 Weather routing
    if "weather" in query_lower:
        return get_weather("Bangalore")

    # 🔹 Future tools can go here
    # if "stock" in query_lower:
    #     return get_stock_price("RELIANCE")

    return "No matching tool found."