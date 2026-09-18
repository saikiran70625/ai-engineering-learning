# Day 3 - LangChain Chains

## Objective

Learn how to compose a prompt template and an LLM into a reusable LangChain chain.

## What I Learned

A LangChain chain connects multiple processing steps together.

In this example, a prompt template receives dynamic inputs and passes the formatted prompt to the LLM.

## Architecture

```text
User Input
    ↓
Prompt Template
    ↓
LLM
    ↓
Response
```

## Implementation

The chain is created using LangChain's runnable composition:

```python
chain = prompt | model
```

The output from the prompt is passed to the model.

## Example Input

```text
topic: RAG
audience: beginner
```

## Key Takeaways

* Chains allow multiple LLM workflow steps to be composed together.
* Prompt templates can accept dynamic input values.
* The `|` operator can be used to compose LangChain runnables.

## Why This Matters for RAG

A RAG application can extend this pattern:

```text
User Question
    ↓
Retriever
    ↓
Relevant Context
    ↓
Prompt Template
    ↓
LLM
    ↓
Answer
```

This exercise is a basic building block for more advanced RAG and agentic workflows.
