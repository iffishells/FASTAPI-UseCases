# Redis Queue in FAST API Application
We use the redis queue for the background task or that type of task which take long time to fullflll the request. In this code i integreated the redis queue using fastAPI application.
* FASTAPI
* Redis Queue
* Task(Sending email take about 10 sec or 10 mints)
* Creating Redis Queue
```angular2html
# example ->rq worker redis_queue_name
rq worker email-worker
```