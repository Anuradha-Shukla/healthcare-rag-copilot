from utils.pdf_loader import extract_text_from_pdf
from utils.text_chunker import chunk_text
from utils.embedder import create_embeddings
from utils.vector_store import store_chunks
from utils.retriever import search_collection
from utils.generator import generate_answer

# STEP 1 — Load PDF

file_path = "../data/sample.pdf"

# STEP 2 — Extract text

text = extract_text_from_pdf(
file_path
)

# STEP 3 — Create chunks

chunks = chunk_text(
text
)

print(
"Number of chunks:",
len(chunks)
)

# STEP 4 — Create embeddings

embeddings = create_embeddings(
chunks
)

print(
"Number of embeddings:",
len(embeddings)
)

print(
"Embedding dimension:",
len(
embeddings[0]
)
)

# STEP 5 — Store in ChromaDB

collection = store_chunks(
chunks,
embeddings
)

print(
"Stored successfully"
)

# STEP 6 — Ask Question

question = input(
"\nAsk Question: "
)

# STEP 7 — Retrieve relevant context

results = search_collection(
collection,
question
)

context = results[
"documents"
][0][0]

# STEP 8 — Generate AI answer

answer = generate_answer(
question,
context
)

print(
"\nAI Answer:\n"
)

print(
answer
)
