from fastapi import FastAPI
from app.routers import habit

app = FastAPI(title="Antyperfectionism Habit Tracker API", version="1.0.0")

app.include_router(habit.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Antyperfectionism Habit Tracker API!"}