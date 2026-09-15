# Day 1 - LangChain LLM Integration

## Objective

Learn how to integrate an OpenAI chat model into a Python application using LangChain.

## What I Learned

- LangChain
- Chat models
- ChatOpenAI
- Model configuration
- invoke()
- Response handling
- Environment variables

## Architecture

Python Application
        ↓
LangChain ChatOpenAI
        ↓
OpenAI GPT-4.1
        ↓
Response

## Key Concepts

### ChatOpenAI

`ChatOpenAI` is the LangChain integration used to interact with an OpenAI chat model.

### invoke()

`invoke()` sends an input to the configured model and returns the model response.

### response.content

`response.content` contains the generated text from the model.

### Temperature

Temperature controls the variability of model generation. Lower values generally produce more consistent responses.

## Example

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-4.1",
    temperature=0
)

response = model.invoke(
    "Explain LangChain in simple terms."
)

print(response.content)
