from groq import Groq
from .config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def generate_answer(question: str, context: str):

    system_prompt = """
You are a Bhagavad Gita knowledge assistant.

Rules:
- Answer ONLY using the provided context.
- Do NOT add outside knowledge.
- If answer not found, say:
  "I could not find the answer in the provided scripture passages."
- Keep answers clear and meaningful.
"""

    user_prompt = f"""
Context:
{context}

Question:
{question}
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # updated model
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return completion.choices[0].message.content.strip()
