from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from .config import EMBED_MODEL, CHROMA_DIR, COLLECTION_NAME

model = SentenceTransformer(EMBED_MODEL)

client = chromadb.Client(Settings(
    persist_directory=CHROMA_DIR,
    is_persistent=True
))

collection = client.get_or_create_collection(name=COLLECTION_NAME)


def retrieve(query: str, k: int = 8):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )

    documents = results.get("documents", [[]])[0]
    distances = results.get("distances", [[]])[0]

    # Optional filtering
    filtered_docs = []
    for doc, dist in zip(documents, distances):
        if dist < 1.5:
            filtered_docs.append(doc)

    return filtered_docs
