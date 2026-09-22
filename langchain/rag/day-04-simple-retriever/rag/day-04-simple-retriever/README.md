# Day 4 - Simple RAG Retriever

## Objective

Learn how retrieval works as a building block of a Retrieval-Augmented Generation (RAG) system.

## What I Learned

A retriever searches a collection of documents and returns the documents that are most relevant to a user's question.

In this example, documents are converted into embeddings and stored in a FAISS vector store.

## Architecture

```text
Documents
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
User Query
    ↓
Retriever
    ↓
Relevant Documents
