from fastapi import APIRouter


main = APIRouter()

@main.get("/")
def index():
    return {
        "Python": "Framework",
    }
