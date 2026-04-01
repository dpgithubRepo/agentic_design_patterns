from openai import OpenAI
from dotenv import load_dotenv
import os
## Setup 
load_dotenv()


# Initialize once (reuse across app)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def code_agent(query: str) -> str:
    """
    Handles coding-related queries:
    - writing code
    - debugging
    - explanations
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a senior software engineer.\n"
                    "Provide clean, correct, and efficient code.\n"
                    "Explain briefly when needed."
                )
            },
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0].message.content