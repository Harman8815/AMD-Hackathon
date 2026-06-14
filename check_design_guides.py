import chromadb

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "design_guides"

try:
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_collection(COLLECTION_NAME)
    print(f"Collection '{COLLECTION_NAME}' count: {collection.count()}")
except Exception as e:
    print(f"Error: {e}")
