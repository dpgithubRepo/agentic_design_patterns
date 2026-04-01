import json
from typing import Literal
from config import client



# ---------------------------
# 📊 ROUTE TYPES
# ---------------------------
RouteType = Literal["code", "general", "tool"]


# ---------------------------
# 🔀 ROUTER FUNCTION
# ---------------------------
def route_query(user_input: str) -> RouteType:
    """
    Routes user query into:
    - code
    - general
    - tool
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,  # deterministic routing
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a strict routing classifier.\n"
                    "Always return valid JSON.\n"
                    "Choose the most appropriate route."
                )
            },
            {
                "role": "user",
                "content": f"""
Classify the user request into one of the following routes:
- code → programming, debugging, scripts
- general → normal Q&A, explanations
- tool → requires external tool (weather, API, DB)

Return ONLY JSON:
{{
  "route": "code | general | tool"
}}

User input:
{user_input}
"""
            }
        ],
        response_format={"type": "json_object"}
    )

    try:
        result = json.loads(response.choices[0].message.content)
        route = result.get("route", "general")

        if route not in ["code", "general", "tool"]:
            return "general"

        return route

    except Exception:
        return "general"


# ---------------------------
# 🔍 OPTIONAL: DEBUG ROUTER
# ---------------------------
def route_with_debug(user_input: str) -> dict:
    """
    Returns route + reasoning (for logging/debugging)
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a routing assistant. Return JSON only."
            },
            {
                "role": "user",
                "content": f"""
Classify and explain briefly.

Routes:
- code
- general
- tool

Return:
{{
  "route": "...",
  "reason": "short explanation"
}}

User: {user_input}
"""
            }
        ],
        response_format={"type": "json_object"}
    )

    try:
        return json.loads(response.choices[0].message.content)
    except Exception:
        return {"route": "general", "reason": "fallback"}