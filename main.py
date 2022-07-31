from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get("/user/{userno}")
def root():
    return {"Hello":"World"}
