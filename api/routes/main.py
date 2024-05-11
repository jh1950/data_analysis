from fastapi import APIRouter

main = APIRouter(
    prefix="",
)

@main.get("/")
def home():
    return {
        "Python": "Framework",
    }
