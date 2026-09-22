from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


documents = [
    Document(
        page_content="AWS Lambda lets you run code without managing servers."
    ),
    Document(
        page_content="Amazon DynamoDB is a managed NoSQL database service."
    ),
    Document(
        page_content="AWS IoT Core connects IoT devices to AWS cloud services."
    ),
    Document(
        page_content="Amazon S3 is an object storage service used to store files and data."
    ),
    Document(
        page_content="AWS AppSync is a managed service for building APIs with GraphQL."
    ),
]


embeddings = OpenAIEmbeddings()

vector_store = FAISS.from_documents(
    documents,
    embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

query = "Which AWS service lets me run code without managing servers?"

results = retriever.invoke(query)

print("Query:")
print(query)

print("\nRetrieved Documents:")

for index, document in enumerate(results, start=1):
    print(f"\n{index}. {document.page_content}")
