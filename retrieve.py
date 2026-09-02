from sentence_transformers import SentenceTransformer
import chromadb

from ingest import load_documents, chunk_text


# Use the embedding model from your planning.md
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Number of chunks to retrieve per question
TOP_K = 4


def build_chunks():
    documents = load_documents()
    all_chunks = []

    for document in documents:
        chunks = chunk_text(document["text"])

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source": document["source"],
                "chunk_id": i,
                "text": chunk
            })

    return all_chunks


def build_vector_store():
    print("Loading embedding model...")
    model = SentenceTransformer(EMBEDDING_MODEL)

    print("Loading and chunking documents...")
    chunks = build_chunks()

    print(f"Preparing {len(chunks)} chunks for ChromaDB...")

    # Create ChromaDB client
    client = chromadb.Client()

    # Create a collection to store housing information
    collection = client.get_or_create_collection(
        name="howard_housing"
    )

    texts = [chunk["text"] for chunk in chunks]

    print("Creating embeddings...")
    embeddings = model.encode(texts).tolist()

    ids = []
    metadatas = []

    for index, chunk in enumerate(chunks):
        ids.append(f"chunk_{index}")

        metadatas.append({
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"]
        })

    collection.add(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

    return collection, model


def retrieve(query, collection, model, top_k=TOP_K):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results


if __name__ == "__main__":
    collection, model = build_vector_store()

    # query = "What should students consider when looking for off-campus housing?"
    # query = "What should students know about applying for Howard University housing?"
    query = "What is the difference between independent off-campus housing and university-sponsored housing?"

    print("\nQuestion:")
    print(query)

    results = retrieve(query, collection, model)

    print("\nTop retrieved chunks:")

    for i in range(len(results["documents"][0])):
        print("\n-----------------------------")
        print(f"Result {i + 1}")
        print(f"Source: {results['metadatas'][0][i]['source']}")
        print(f"Chunk ID: {results['metadatas'][0][i]['chunk_id']}")
        print(results["documents"][0][i])