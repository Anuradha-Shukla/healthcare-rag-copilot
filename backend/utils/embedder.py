from sentence_transformers import SentenceTransformer


def create_embeddings(chunks):

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(chunks)

    return embeddings