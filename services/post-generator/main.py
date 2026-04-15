from fastapi import FastAPI
from redis import Redis
from rq import Queue
from uuid import uuid4

app = FastAPI()

redis_conn = Redis(host="redis", port=6379)
queue = Queue("scrape", connection=redis_conn)

@app.post("/scrape")
def scrape_url(url: str):
    job = queue.enqueue(
        "tasks.scrape_and_store",
        url,
        job_timeout=300
    )

    return {
        "job_id": job.id,
        "status": "queued",
        "url": url
    }