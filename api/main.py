from fastapi import FastAPI

app = FastAPI()


@app.get("/api/hello")
async def root():
    return {"message": "Hello World"}

@app.get("/api/hi")
async def root():
    return {"message": "Hi World"}