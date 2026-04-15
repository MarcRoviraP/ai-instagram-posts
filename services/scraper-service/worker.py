from redis import Redis
from rq import Worker, Queue
import tasks

redis_conn = Redis(host="redis", port=6379)

if __name__ == "__main__":
    worker = Worker(
        [Queue("scrape", connection=redis_conn)],
        connection=redis_conn
    )
    worker.work()