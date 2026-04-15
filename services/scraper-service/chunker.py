def create_chunks(blocks):
    """
    Convierte bloques HTML estructurados en chunks semánticos.
    Ideal para embeddings + RAG.
    """

    chunks = []
    current_chunk = []

    for block in blocks:

        # Si encontramos un nuevo título, empezamos nuevo chunk
        if block["type"] in ["h1", "h2"]:
            if current_chunk:
                chunks.append(current_chunk)

            current_chunk = [block]
        else:
            current_chunk.append(block)

    if current_chunk:
        chunks.append(current_chunk)

    return chunks