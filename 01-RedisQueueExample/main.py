# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import Redis
from rq import Queue
from tasks import send_email

app = FastAPI()

# Set up Redis and Queue
redis_conn = Redis(host='localhost', port=6379, db=0)
queue = Queue('email_queue', connection=redis_conn)

class EmailRequest(BaseModel):
    email: str

@app.post("/send-email/")
def enqueue_email(request: EmailRequest):
    try:
        email = request.email
        # Enqueue the task
        job = queue.enqueue(send_email, email)
        return {"job_id": job.id, "status": "Enqueued"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class JobStatusRequest(BaseModel):
    job_id: str

@app.post("/job-status/")
def get_job_status(request: JobStatusRequest):
    job = queue.fetch_job(request.job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job_id": request.job_id, "status": job.get_status(), "result": job.result}


@app.get("/queue-length/")
def get_queue_length():
    try:
        length = queue.count
        return {"queue_length": length}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))