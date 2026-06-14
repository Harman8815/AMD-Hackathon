import chromadb

CHROMA_PATH = "./chroma_db"

try:
    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collections = client.list_collections()
    print(f"Collections: {[c.name for c in collections]}")
except Exception as e:
    print(f"Error: {e}")
