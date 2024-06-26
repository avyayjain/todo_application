# This is Todo application system 

## Installation
### 1. Clone the repository
```bash
git clone https://github.com/avyayjain/todo_application.git
```

### 2. Install the requirements to install the requirements run the following command
```bash
pip install -r requirements.txt
```
### 3. do alembic migration
```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```
### 4. create the .env file and add the following variables
```
DATABASE_URL
DATABASE_USER
DATABASE_PASSWORD
DATABASE_DB
SECRET_KEY
ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES
```
### 5. run the server
```bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
```
### 6. you can also build the docker container by running the following command
```bash
docker build -t todo_application .
```
### 7. you can run the docker container by running the following command
```bash
docker run -d -p 8000:8000 todo_application
```
# Testing
### 1. now you can go to the postman the collection by visiting this url 
```bash
https://www.postman.com/technical-saganist-64650375/workspace/projects/collection/23939640-60350063-a735-4dd8-b45c-aa41ff4d3762?action=share&creator=23939640
```
### 2. you can import the collection in the postman and test the api's
### 3. you can also go to the swagger documentation by going to the following url
```bash
http://localhost:8000/docs
```

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
 