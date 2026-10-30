from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers.student_router import StudentRouter

app = FastAPI()

app.include_router(StudentRouter)


@app.get("/")
def home():
    return RedirectResponse(url="/docs")