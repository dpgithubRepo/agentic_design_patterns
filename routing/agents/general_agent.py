from openai import OpenAI
from config import client

def general_agent(query: str) -> str:
    """
    Handles general Q&A, explanations, and casual queries
    """

    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant.\n"
                    "Give clear, concise, and useful answers."
                )
            },
            {"role": "user", "content": query}
        ]
    )

    return response.choices[0].message.content