import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 API
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# 🤖 Embedding model
EMBED_MODEL = "all-MiniLM-L6-v2"

# 🗄 Chroma settings
CHROMA_DIR = "data/chroma"
COLLECTION_NAME = "gita_rag"

# 📦 Dataset
DATASET_NAME = "knowrohit07/gita_dataset"
DATASET_SPLIT = "train"