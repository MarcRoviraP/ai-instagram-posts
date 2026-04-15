from bs4 import BeautifulSoup

def extract_article(html: str):
    soup = BeautifulSoup(html, "lxml")

    title = soup.title.get_text(strip=True) if soup.title else "Untitled"

    # eliminar ruido
    for tag in soup(["nav", "footer", "header", "aside", "script", "style"]):
        tag.decompose()

    main = soup.find("main") or soup.find("article") or soup.body

    blocks = []

    if not main:
        return {"title": title, "blocks": []}

    for tag in main.find_all(["h1", "h2", "h3", "p", "pre", "code"]):

        text = tag.get_text(" ", strip=True)

        if not text:
            continue

        # filtro anti basura (muy importante)
        if len(text) < 3:
            continue

        blocks.append({
            "type": tag.name,
            "text": text
        })

    return {
        "title": title,
        "blocks": blocks
    }

def is_code_block(tag):
    return tag.name in ["code", "pre"] or "language-" in str(tag.get("class", []))
    # título
    title = soup.title.get_text(strip=True) if soup.title else "Untitled"

    # eliminar ruido típico (muy importante en docs modernas)
    for tag in soup(["nav", "footer", "header", "aside", "script", "style"]):
        tag.decompose()

    blocks = []

    # elementos relevantes
    for tag in soup.find_all(["h1", "h2", "h3", "p", "code", "pre"]):

        text = tag.get_text(" ", strip=True)

        if not text:
            continue

        # limpieza extra
        text = " ".join(text.split())

        blocks.append({
            "type": tag.name,
            "text": text
        })

    return {
        "title": title,
        "blocks": blocks
    }