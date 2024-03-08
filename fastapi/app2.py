from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello(a: int, b: int):
    return a + b
