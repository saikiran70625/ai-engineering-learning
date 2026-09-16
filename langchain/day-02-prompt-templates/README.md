# Day 2 - LangChain Prompt Templates

## Objective

Learn how to create reusable prompts using LangChain Prompt Templates.

## Why Prompt Templates?

A hard-coded prompt is difficult to reuse.

Example:

"Explain RAG in simple terms."

A prompt template allows us to create a reusable structure:

"Explain {topic} in {style}."

The values can change for each request.

## Architecture

User Input
    ↓
Prompt Template
    ↓
Chat Model
    ↓
Response

## Example

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in {style}."
)

model = ChatOpenAI(
    model="gpt-4.1",
    temperature=0
)

chain = prompt | model

response = chain.invoke({
    "topic": "RAG",
    "style": "simple terms"
})

print(response.content)
