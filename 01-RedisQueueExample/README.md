# Redis Queue in FastAPI Application

We use Redis Queue for background tasks or tasks that take a long time to complete. In this example, we integrated Redis Queue into a FastAPI application.

* **FastAPI**
* **Redis Queue**
* **Task**: Sending email (takes about 10 seconds to 10 minutes)

## Creating Redis Queue

```bash
# Example command to start an RQ worker for a Redis queue
rq worker redis_queue_name
rq worker email-worker
```

Feel free to adjust any additional details or commands as needed!





