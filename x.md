# compliance_rag.py

Assumptions:

- ChromaDB already exists in ./chroma_db
- Collection name = regulations
- Ollama is running locally
- Model = qwen3:8b
- Embedding model used during ingestion = all-MiniLM-L6-v2

Required packages:

pip install chromadb sentence-transformers ollama

```python
import chromadb
import ollama

from sentence_transformers import SentenceTransformer


# =====================
# Configuration
# =====================

CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "regulations"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
OLLAMA_MODEL = "qwen3:8b"
TOP_K = 5


# =====================
# Load Embedding Model
# =====================

embedding_model = SentenceTransformer(
    EMBEDDING_MODEL
)


# =====================
# Connect ChromaDB
# =====================

client = chromadb.PersistentClient(
    path=CHROMA_PATH
)

collection = client.get_collection(
    COLLECTION_NAME
)


# =====================
# Retrieve Relevant Chunks
# =====================

def retrieve_context(question, top_k=TOP_K):

    query_embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]

    return documents


# =====================
# Build Prompt
# =====================

def build_prompt(question, chunks):

    context = "\n\n".join(chunks)

    prompt = f"""
You are a regulatory compliance expert.

Use ONLY the provided context to answer.

If the answer cannot be found in the context,
explicitly say:

"Insufficient information found in regulations."

Context:
{context}

Question:
{question}

Provide:
1. Direct Answer
2. Explanation
3. Relevant Regulation References
"""

    return prompt


# =====================
# Ask Ollama
# =====================

def generate_answer(prompt):

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# =====================
# Full Pipeline
# =====================

def ask(question):

    chunks = retrieve_context(question)

    prompt = build_prompt(
        question,
        chunks
    )

    answer = generate_answer(
        prompt
    )

    return {
        "question": question,
        "retrieved_chunks": chunks,
        "answer": answer
    }


# =====================
# Example
# =====================

if __name__ == "__main__":

    question = (
        "Can a payment aggregator onboard a merchant "
        "without completing KYC?"
    )

    result = ask(question)

    print("\nQUESTION\n")
    print(result["question"])

    print("\nRETRIEVED CHUNKS\n")

    for i, chunk in enumerate(
        result["retrieved_chunks"],
        start=1
    ):
        print(f"\nChunk {i}\n")
        print(chunk[:500])

    print("\nANSWER\n")
    print(result["answer"])
```
