import chromadb


def store_chunks(chunks, embeddings):

    client = chromadb.Client()

    collection = client.create_collection(
        name="healthcare_docs"
    )

    ids = []

    for i in range(len(chunks)):
        ids.append(str(i))

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )

    return collection