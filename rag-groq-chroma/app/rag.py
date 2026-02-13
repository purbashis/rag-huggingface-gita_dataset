from .retrieval import retrieve
from .llm import generate_answer


def run_rag(question: str):

    docs = retrieve(question)

    if not docs:
        return "I could not find relevant passages for this question."

    context = "\n\n---\n\n".join(docs)

    return generate_answer(question, context)
