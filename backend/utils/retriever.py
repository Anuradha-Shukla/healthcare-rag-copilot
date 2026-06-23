from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def search_collection(
    collection,
    query
):

    query_embedding = model.encode(
        [query]
    )

    results = collection.query(

        query_embeddings=query_embedding.tolist(),

        n_results=2

    )

    return results