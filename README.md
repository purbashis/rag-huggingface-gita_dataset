# 📜 Gita Intelligence System (RAG with HuggingFace + Chroma + Groq)

A production-style Retrieval-Augmented Generation (RAG) system built over the Bhagavad Gita dataset using:

- HuggingFace Embeddings
- ChromaDB Vector Store
- Groq LLM (Llama 3.1)
- Modular Python Architecture

This system retrieves semantically relevant scripture passages and generates grounded answers without hallucination.

---

## 🚀 Features

- Batch embedding ingestion
- Persistent vector database (Chroma)
- Semantic similarity search
- Context-grounded LLM responses
- Hallucination mitigation
- Modular RAG pipeline
- Clean architecture

---

## 🧠 Architecture

User Query
↓
Embedding (SentenceTransformers)
↓
Chroma Vector Search
↓
Relevant Gita Verses
↓
Groq LLM (Llama 3.1)
↓
Grounded Answer


---

## 🛠 Tech Stack

- Python 3.11+
- SentenceTransformers (`all-MiniLM-L6-v2`)
- ChromaDB (persistent local vector store)
- HuggingFace Datasets
- Groq API (Llama 3.1)
- dotenv

---

The dataset contains structured Bhagavad Gita verses including translations and related metadata.

HuggingFace Reference:
https://huggingface.co/datasets/knowrohit07/gita_dataset

The ingestion pipeline embeds scripture passages and stores them in a persistent Chroma vector database for semantic retrieval.

