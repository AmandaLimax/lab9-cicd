from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "online",
        "ambiente": os.getenv("AMBIENTE", "desenvolvimento"),
        "mensagem": "API FastAPI rodando com CI/CD!"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}
