# 🛠️ AMD Design Compliance AI

Welcome to the **Design Compliance RAG System**! This project uses Advanced Retrieval-Augmented Generation (RAG) to ensure design specifications meet regulatory and internal guidelines.

## 📁 Project Structure

```text
AMD-Hackathon/
├── data/               # Source PDF guidelines and rules.json
├── notebooks/          # Modular Jupyter Notebooks
│   ├── 01_Ingestion_Pipeline.ipynb     # Process PDFs -> ChromaDB
│   ├── 02_Compliance_Assistant.ipynb    # Interactive Q&A Portal
│   └── 03_Validation_Rules.ipynb       # Rule execution & testing
├── chroma_db/          # Vector Database
└── .venv/              # Python environment
```

## 🚀 Getting Started

### 1. Requirements
Ensure you have **Ollama** running locally with the `qwen3:4b` model.
```bash
ollama run qwen3:4b
```

### 2. Workflow
1. **Ingestion**: Run `notebooks/01_Ingestion_Pipeline.ipynb` to index the latest PDFs.
2. **Consultation**: Use `notebooks/02_Compliance_Assistant.ipynb` to ask compliance questions.
3. **Validation**: Use `notebooks/03_Validation_Rules.ipynb` for structured parameter checks.

## 🛠️ Tech Stack
- **LLM**: Qwen 3 (via Ollama)
- **Vector DB**: ChromaDB
- **Embeddings**: Sentence-Transformers (all-MiniLM-L6-v2)
- **Interface**: IPyWidgets
