CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS article_chunks (
    id UUID PRIMARY KEY,
    url TEXT,
    title TEXT,
    content TEXT,
    topic TEXT,
    embedding VECTOR(384),
    chunk JSONB,

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS generated_posts (
    id UUID PRIMARY KEY,
    topic TEXT,
    caption TEXT,
    hashtags TEXT,
    status TEXT,
    raw_html TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);