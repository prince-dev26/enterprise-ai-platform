from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Enterprise AI Platform Backend Running 🚀"
    }