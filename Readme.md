# This is Todo application system 

## Installation
1. Clone the repository
2. Install the requirements to install the requirements run the following command
```bash
pip install -r requirements.txt
```
3. do alembic migration
```bash
alembic revision --autogenerate -m "initial migration"
alembic upgrade head
```
4. run the server
```bash
python main.py
```
5. you can also build the docker container by running the following command
```bash
docker build -t todo_application .
```
6. you can run the docker container by running the following command
```bash
docker run -d -p 8000:8000 todo_application
```
## Testing
1. now you can go to the postman the collection by visiting this url "https://www.postman.com/technical-saganist-64650375/workspace/projects/collection/23939640-60350063-a735-4dd8-b45c-aa41ff4d3762?action=share&creator=23939640"
2. you can import the collection in the postman and test the api's
3. you can also go to the swagger documentation by going to the following url
```bash
http://localhost:8000/docs
```
 