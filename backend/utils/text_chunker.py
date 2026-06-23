def chunk_text(text):

    chunks = text.split("\n")

    cleaned_chunks = []

    for chunk in chunks:

        chunk = chunk.strip()

        if chunk:

            cleaned_chunks.append(chunk)

    return cleaned_chunks