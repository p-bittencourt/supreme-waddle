from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def red_root():
    return {"Hello": "World"}
