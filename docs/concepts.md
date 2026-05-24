# Concepts

## 1. LangGraph
What is LangGraph?
Why not CrewAI?
State management
Nodes
Edges
Conditional routing

---

## 2. Hybrid RAG
What is RAG?
Vector search
BM25
Hybrid retrieval
Chunking
Reranking

---

## 3. pgvector
Why use vector DB?
How embeddings work
Similarity search

---

## 4. FastAPI
Why async?
Dependency injection

---

## 5. Prompt Engineering
System prompt
Context injection
Guardrails

---

## 6. Docker
Containers
Volumes
Networks
Compose

# FinSight AI Concepts

---

# 1. Why FastAPI?

FastAPI is a modern Python framework for APIs.

Why we chose it:

- async support
- automatic Swagger docs
- validation using Pydantic
- production ready

Why not Flask?

Flask is simpler but requires more setup.

FastAPI is better for enterprise AI systems.

---

# 2. Why PostgreSQL?

We need:

1. relational data
2. vector embeddings

Postgres + pgvector allows both.

Instead of using:

MongoDB + Pinecone

we use one database.

Benefits:

- cheaper
- simpler architecture
- docker friendly

---

# 3. Why Docker?

Docker makes environment consistent.

Without Docker:

"works on my machine" problem.

Docker ensures:

same Python
same DB
same dependencies
same setup

## OpenAI Service Layer

We isolate OpenAI logic inside services/.

Benefits:

- reusable
- testable
- easier debugging
- retries
- model switching

---

## Prompt Management

Prompts should never be hardcoded.

Why?

Maintainability.

We separate prompts into:

prompts/

This helps versioning and testing.