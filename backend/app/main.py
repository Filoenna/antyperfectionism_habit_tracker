from fastapi import FastAPI

app = FastAPI(title="Antyperfectionism Habit Tracker API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to the Antyperfectionism Habit Tracker API!"}