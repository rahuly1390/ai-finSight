# AI FinSight

Enterprise-grade **Agentic Financial Intelligence Platform** using **LangGraph, LangChain, OpenAI, Hybrid RAG (FAISS + BM25), FastAPI, and Streamlit**.

AI FinSight helps solve real-world **FinTech, Wealth Management, Tax, Audit, and Risk Analysis** use cases through a multi-agent architecture.

---

# Features

## Current Features (v0.3.0)

### AI + Agentic Architecture

* Multi-Agent System using LangGraph
* RAG Agent for evidence retrieval
* Risk Agent for financial reasoning
* Shared state orchestration
* OpenAI-powered analysis

### Hybrid RAG

* PDF / CSV / TXT document ingestion
* Text chunking
* OpenAI embeddings (`text-embedding-3-small`)
* FAISS vector search
* BM25 keyword retrieval
* Hybrid retrieval strategy

### Backend APIs

* Health API
* Ask OpenAI API
* Upload Document API
* Ask RAG API
* Ask Agent API

### User Interface

* Streamlit UI
* Document upload
* Financial assistant chat
* Risk analysis dashboard
* Retrieved evidence panel

---

# Architecture Overview

## Enterprise System Architecture

```text
┌──────────────────────────────┐
│        Streamlit UI          │
│ Upload + Chat + Dashboard    │
└──────────────┬───────────────┘
               │ REST API
               ▼
┌──────────────────────────────┐
│         FastAPI API          │
│ /upload /ask /ask-agent      │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       LangGraph Engine       │
│ Stateful Multi-Agent Flow    │
└──────────────┬───────────────┘
               │
     ┌─────────┴─────────┐
     ▼                   ▼
┌──────────────┐   ┌──────────────┐
│  RAG Agent   │   │ Risk Agent   │
│ Retrieve     │   │ Analyze      │
│ Evidence     │   │ Financial    │
└──────┬───────┘   │ Risk         │
       │           └──────┬───────┘
       ▼                  ▼
┌──────────────────────────────┐
│         Hybrid RAG           │
│      FAISS + BM25            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ OpenAI Embeddings + LLM      │
│ text-embedding-3-small       │
│ GPT Models                   │
└──────────────────────────────┘
```

---

## LangGraph Workflow

```text
START
   │
   ▼
RAG Agent
(Retrieve Evidence)
   │
   ▼
Risk Agent
(Financial Reasoning)
   │
   ▼
END
```

### Shared Graph State

```python
class GraphState(TypedDict):
    query: str
    retrieved_docs: list
    rag_response: str
    risk_analysis: str
    final_response: str
```

---

# Supported FinTech Use Cases

## Wealth Management

* Spending pattern analysis
* Investment risk awareness
* Savings recommendations
* Financial behavior insights

## FinTech Risk Analysis

* Unusual expense detection
* Risk scoring
* Financial anomaly detection
* Budget overspending analysis

## Tax Intelligence (Upcoming)

* Tax deduction suggestions
* Tax document summarization
* Expense categorization

## Audit Intelligence (Upcoming)

* Compliance checks
* Suspicious transaction review
* Audit trail analysis

---

# Tech Stack

## Backend

* Python 3.13
* FastAPI
* LangGraph
* LangChain
* OpenAI SDK
* Pydantic

## RAG Layer

* FAISS
* BM25 (`rank-bm25`)
* RecursiveCharacterTextSplitter
* OpenAI Embeddings

## Frontend

* Streamlit

## Parsing

* PyMuPDF
* PyPDF
* Pandas

---

# Project Structure

```text
finsight-ai/
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── config/
│   │   ├── graph/
│   │   ├── prompts/
│   │   ├── rag/
│   │   ├── schemas/
│   │   ├── services/
│   │   └── data/uploads/
│   │
│   └── requirements.txt
│
├── frontend/
│   └── streamlit/
│
└── docs/
```

---

# API Endpoints

| Endpoint            | Method | Description      |
| ------------------- | ------ | ---------------- |
| `/api/v1/health`    | GET    | Health check     |
| `/api/v1/ask`       | POST   | OpenAI query     |
| `/api/v1/upload`    | POST   | Upload documents |
| `/api/v1/ask-rag`   | POST   | Hybrid RAG query |
| `/api/v1/ask-agent` | POST   | Agentic workflow |

---

# Screenshots

Add your screenshots here.

## Dashboard

```md
![Dashboard](screenshots/dashboard.png)
```

## Upload Document

```md
![Upload](screenshots/upload.png)
```

## Financial Assistant

```md
![Assistant](screenshots/chat.png)
```

## Risk Analysis

```md
![Risk](screenshots/risk.png)
```

---

# Local Setup

## Clone Repository

```bash
git clone <repo-url>
cd ai-finSight
```

## Create Virtual Environment

```bash
py -3.13 -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

---

## Add Environment Variables

Create:

```text
backend/.env
```

```env
OPENAI_API_KEY=your_key
PROJECT_NAME=FinSight AI
API_V1=/api/v1
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/finsight
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger:

```text
http://localhost:8000/docs
```

---

## Run Streamlit

```bash
cd frontend/streamlit
streamlit run app.py
```

UI:

```text
http://localhost:8501
```

---

### v0.1.0

* FastAPI foundation
* OpenAI integration
* Prompt management
* `/ask` API

### v0.2.0

* Document ingestion
* Chunking
* Embeddings
* Hybrid RAG
* FAISS + BM25

### v0.3.0

* LangGraph workflow
* RAG Agent
* Risk Agent
* Streamlit UI


---

# Future Enterprise Architecture

```text
Frontend (Streamlit/React)
          │
          ▼
      API Gateway
          │
          ▼
        FastAPI
          │
     ┌────┴─────┐
     ▼          ▼
 LangGraph   Redis Cache
     │
┌────┼─────────────┐
▼    ▼             ▼
RAG  Risk       Tax Agent
│
▼
Postgres + pgvector
│
▼
OpenAI
```

---

# Why This Project Matters

This project demonstrates:

* Enterprise AI Architecture
* Agentic AI Design
* LangGraph Workflows
* Modern Hybrid RAG
* Explainable AI for FinTech
* API Development
* Streamlit UI
* Production-Ready Thinking

Useful for:

* Senior Frontend/Full Stack roles
* AI Engineer roles
* GenAI Engineer interviews
* FinTech Architect discussions
* Technical demos

---

# License

MIT License
