from fastapi import FastAPI


app = FastAPI()


@app.get("/home")
async def home():
    return {"message": "Hello World"}
