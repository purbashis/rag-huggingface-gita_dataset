from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from tqdm import tqdm
from .config import EMBED_MODEL, CHROMA_DIR, COLLECTION_NAME, DATASET_NAME, DATASET_SPLIT


def ingest_data():

    print("📖 Loading Gita dataset...")
    ds = load_dataset(DATASET_NAME, split=DATASET_SPLIT)

    

    model = SentenceTransformer(EMBED_MODEL)

    client = chromadb.Client(Settings(
        persist_directory=CHROMA_DIR,
        is_persistent=True
    ))

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    print("🚀 Generating embeddings in batches...")

    batch_size = 64
    documents = []
    ids = []

    for i, row in enumerate(tqdm(ds)):

        text = row.get("text", str(row))
        documents.append(text)
        ids.append(str(i))

        if len(documents) == batch_size:
            embeddings = model.encode(documents).tolist()

            collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=documents
            )

            documents = []
            ids = []

    # Insert remaining docs
    if documents:
        embeddings = model.encode(documents).tolist()
        collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents
        )

    print("🎉 Ingestion complete!")


if __name__ == "__main__":
    ingest_data()
