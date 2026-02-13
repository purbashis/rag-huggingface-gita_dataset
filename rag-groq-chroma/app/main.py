from .rag import run_rag


def main():
    print("📜 Gita RAG System (HF + Chroma + Groq)\n")

    while True:
        q = input("Ask something --> ").strip()

        if q.lower() in ["exit", "quit"]:
            print("Goodbye 🙏")
            break

        if not q:
            continue

        answer = run_rag(q)

        print("\nAnswer:\n")
        print(answer)
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
