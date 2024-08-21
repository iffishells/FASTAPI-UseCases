import requests
task_id = "f4e55b6a-9041-4b13-9fe8-4c8edccc0097'"
response = requests.get(f"http://127.0.0.1:8000/task/{task_id}")
print(response.json())