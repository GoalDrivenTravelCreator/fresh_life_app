from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Life Balance Dashboard API")

# Temporary in-memory list to act as our database for now
tasks_db = []

class TaskItem(BaseModel):
    title: str
    category: str  # "Household" or "Study"
    status: str = "Pending"

# Root route now serves a proper visual HTML page for PWABuilder
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <head>
            <title>Life Balance Dashboard</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="manifest" href="/manifest.json">
            <style>
              body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f4f9f4; color: #333; }
                h1 { color: #2c6b2f; }
                p { font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>🌿 Life Balance Dashboard</h1>
            <p>Your all-in-one command center for household duties, personal study, and daily planning.</p>
            <p><b>Status:</b> App Backend is Live & Running!</p>
        </body>
    </html>
    """

@app.get("/tasks", response_model=List[TaskItem])
def get_tasks():
    return tasks_db

@app.post("/tasks")
def add_task(task: TaskItem):
    tasks_db.append(task)
    return {"message": "Success! Task added.", "task": task}  
