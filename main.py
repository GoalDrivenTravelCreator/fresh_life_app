from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Life Balance Dashboard API")

# Temporary in-memory list to act as our database for now
tasks_db = []

class TaskItem(BaseModel):
    title: str
    category: str  # "Household" or "Study"
    status: str = "Pending"

@app.get("/")
def home():
    return {"message": "Welcome to the Life Balance App API! 🌸"}

@app.get("/tasks", response_model=List[TaskItem])
def get_tasks():
    return tasks_db

@app.post("/tasks")
def add_task(task: TaskItem):
    tasks_db.append(task)
    return {"message": "Success! Task added.", "task": task}