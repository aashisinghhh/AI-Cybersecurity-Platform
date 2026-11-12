
from fastapi import FastAPI

app = FastAPI(
    title="AI Cybersecurity Platform API",
    description="Backend API for our AI-powered CTF platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Cybersecurity Platform Backend",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "backend"
    }


@app.get("/api/v1/status")
def platform_status():
    return {
        "platform": "AI Cybersecurity Platform",
        "backend": "FastAPI",
        "version": "1.0.0"
    }
