import chromadb

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "regulations"

try:
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(COLLECTION_NAME)
    count = collection.count()
    print(f"Collection '{COLLECTION_NAME}' has {count} documents.")
except Exception as e:
    print(f"Error: {e}")
