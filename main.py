import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.resources.change_status import change_stat
from src.resources.task import task_router
from src.resources.sign_up import add_user_router
from src.resources.token import token_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(add_user_router, prefix="/api/user/sign-up")
app.include_router(token_router, prefix="/api/token")
app.include_router(task_router, prefix="/api/task")
app.include_router(change_stat, prefix="/api/status")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
