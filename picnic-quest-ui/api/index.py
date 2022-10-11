from fastapi import FastAPI
app = FastAPI


@app.get("https://picnic-quest.vercel.app/")
def read_root():
    return {"message": "Server is up and running"}
