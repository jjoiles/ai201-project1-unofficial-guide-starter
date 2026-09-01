from pathlib import Path

# Folder containing the housing documents
DOCUMENTS_FOLDER = Path("documents")


def load_documents():
    documents = []

    # Find every .txt file in the documents folder
    for file_path in DOCUMENTS_FOLDER.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": file_path.name,
            "text": text
        })

    return documents

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    documents = load_documents()

    print(f"Loaded {len(documents)} documents.")

    all_chunks = []

    for document in documents:
        chunks = chunk_text(document["text"])

        for i, chunk in enumerate(chunks):
            all_chunks.append({
                "source": document["source"],
                "chunk_id": i,
                "text": chunk
            })

    print(f"Created {len(all_chunks)} chunks.")

    # Display the first 5 chunks so we can inspect them
    for chunk in all_chunks[:5]:
        print("\n-----------------------------")
        print(f"Source: {chunk['source']}")
        print(f"Chunk ID: {chunk['chunk_id']}")
        print(chunk["text"])