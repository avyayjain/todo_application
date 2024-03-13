import os
from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION_LINK = "postgresql://{}:{}@{}/{}".format(
    os.getenv("DATABASE_USER"),
    os.getenv("DATABASE_PASS"),
    os.getenv("DATABASE_URL"),
    os.getenv("DATABASE_DB"),
)

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 600


