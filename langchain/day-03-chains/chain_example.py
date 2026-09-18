from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a {audience}. "
    "Give a short explanation and one practical example."
)

model = ChatOpenAI(model="gpt-4o-mini")

chain = prompt | model

response = chain.invoke({
    "topic": "RAG",
    "audience": "beginner"
})

print(response.content)
