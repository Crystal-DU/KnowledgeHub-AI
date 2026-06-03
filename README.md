# KnowledgeHub AI

KnowledgeHub AI is a local RAG-based document assistant that allows users to load documents, retrieve relevant content, and generate answers using a local LLM.

## Features

- Load documents from a local folder
- Supports PDF, Excel, PowerPoint, and TXT files
- Split documents into searchable chunks
- Generate embeddings with Ollama
- Store and retrieve chunks using ChromaDB
- Answer questions with a local Qwen model
- Display source chunks used for the answer
- Runs locally without OpenAI API

## Tech Stack

- Python
- Ollama
- Qwen2.5
- nomic-embed-text
- ChromaDB
- pypdf
- openpyxl
- python-pptx
- requests

## Project Structure

```text
KnowledgeHub-AI/
├── main.py
├── requirements.txt
├── .gitignore
└── documents/
```

## How It Works

```text
Documents
↓
Text Extraction
↓
Chunking
↓
Embedding
↓
ChromaDB Retrieval
↓
Local LLM Answer
↓
Source Citation
```

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama models:

```bash
ollama pull nomic-embed-text
ollama pull qwen2.5:3b
```

## Usage

Put your documents into the `documents/` folder.

Supported formats:

```text
.pdf
.xlsx
.pptx
.txt
```

Run the app:

```bash
python main.py
```

Ask a question:

```text
Ask a question: Can I work from home?
```

Example output:

```text
===== Answer =====
Employees may work remotely up to 2 days per week with manager approval.

===== Sources =====
[1] Remote Work Policy Employees may work remotely up to 2 days per week...
[2] Remote work requests should be submitted before the end of the previous week...
```

## Privacy Note

This project is designed to run locally.  
Sample documents are not included in this repository.

Do not upload confidential, internal, or company documents to a public GitHub repository.

## Future Improvements

- Web UI with Streamlit or FastAPI
- Better chunking strategy
- Metadata-based source citation
- Multi-file source tracking
- Persistent ChromaDB storage
- Chat history
- Agent-based document analysis