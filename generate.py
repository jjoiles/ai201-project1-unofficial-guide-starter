import os
from dotenv import load_dotenv
from groq import Groq

from retrieve import build_vector_store, retrieve


load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(query):
    collection, model = build_vector_store()

    results = retrieve(query, collection, model)

    context_parts = []
    sources = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for text, metadata in zip(documents, metadatas):
        source = metadata["source"]

        context_parts.append(f"Source: {source}\n{text}")
        sources.append(source)

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""
You are a Howard University housing assistant.

Answer the user's question using ONLY the information in the provided context.

If the context does not contain enough information to answer the question, say:
"I don't have enough information in the provided housing documents to answer that question."

Do not make up information.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="groq/compound",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    answer = response.choices[0].message.content

    unique_sources = list(dict.fromkeys(sources))

    return answer, unique_sources


if __name__ == "__main__":
    #question = "What should students know about applying for Howard University housing?"
    question = "What should students consider when looking for off-campus housing?"
    #question = "What is the best restaurant near Howard University?"

    answer, sources = generate_answer(question)

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")
    for source in sources:
        print(f"- {source}")