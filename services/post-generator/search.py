from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import psycopg2

app = FastAPI()

model = SentenceTransformer("all-MiniLM-L6-v2")

DB = "postgresql://ai_user:ai_password@postgres:5432/ai_posts"