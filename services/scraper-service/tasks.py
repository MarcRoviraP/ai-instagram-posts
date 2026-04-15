import uuid
import psycopg2
import json

from scraper import fetch_html
from extractor import extract_article
from chunker import create_chunks
from embeddings import get_embedding

DATABASE_URL = "postgresql://ai_user:ai_password@postgres:5432/ai_posts"
def embed_chunk(chunk):
    """
    Convierte un chunk en embedding listo para DB
    """

    # unir texto del chunk
    text = " ".join([b["text"] for b in chunk])

    embedding = get_embedding(text)

    return {
        "chunk": chunk,
        "text": text,
        "embedding": embedding
    }
def save_to_db(url: str, title: str, chunks: list):
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()

    for chunk in chunks:
        text = " ".join([b["text"] for b in chunk])

        embedding = get_embedding(text)
        cur.execute("""
            INSERT INTO article_chunks (id, url, title, chunk,embedding)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            str(uuid.uuid4()),
            url,
            title,
            json.dumps(chunk),  # JSON simple por ahora
            embedding
        ))

    conn.commit()
    cur.close()
    conn.close()

def scrape_and_store(url: str):
    """
    Pipeline principal:
    URL → HTML → estructura → chunks → DB
    """

    # 1. SCRAPING
    html = fetch_html(url)

    # 2. EXTRACCIÓN ESTRUCTURADA
    article = extract_article(html)

    # 3. CHUNKING SEMÁNTICO
    chunks = create_chunks(article["blocks"])

    # 4. GUARDAR EN DB
    save_to_db(url, article["title"], chunks)

    return {
        "status": "done",
        "url": url,
        "chunks": len(chunks)
    }