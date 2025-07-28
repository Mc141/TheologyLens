# TheologyLens – AI-Powered Scripture Search

---

## Overview

TheologyLens is a semantic search application for scripture passages. Instead of basic keyword matching, it uses AI to understand the meaning of queries and find relevant biblical passages based on context and theme. Built as a learning project to explore modern AI/ML techniques in natural language processing.

---

## Features

- **Semantic Search:** Uses SentenceTransformers for meaning-based search
- **Vector Similarity:** FAISS for efficient similarity matching
- **Result Clustering:** Groups related passages by theme
- **React Frontend:** Clean interface for queries and results
- **FastAPI Backend:** Python API for search functionality
- **Real-time Results:** Fast response times with pre-computed embeddings

---

## Tech Stack

### Backend
- **FastAPI** - Python web framework
- **SentenceTransformers** - Text embedding models
- **FAISS** - Vector similarity search
- **Python 3.8+** - Core language

### Frontend
- **React** - UI framework
- **JavaScript** - Frontend logic
- **CSS** - Styling

---

## How It Works

1. User enters a question about scripture
2. Query is converted to a vector using SentenceTransformers
3. FAISS finds similar scripture passages in the vector database
4. Results are clustered by theme and returned to the frontend
5. User sees relevant passages grouped by topic

---

## Dependencies

### Backend
- `fastapi` - Web framework
- `sentence-transformers` - Text embeddings
- `faiss-cpu` - Vector search

### Frontend
- `react` - UI library
- `axios` - HTTP client

---

## Future Improvements

- Add support for multiple Bible versions
- Implement user authentication
- Add search history
- Improve clustering algorithms
- Add mobile responsiveness
