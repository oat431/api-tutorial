# API tutorial

just and example of how to implement API using python and flask

## Chapter list

## Chapter list

1. Chapter 1: Project Setup
2. Chapter 2: API
3. Chapter 3: Database
4. Chapter 4: CORS
5. Chapter 5: Pagination
6. Chapter 6: GraphQL
7. Chapter 7: API Documenting
8. Chapter 8: Environment Variable
9. Chapter 9: Testing
10. Chapter 10: Deploying

## Chapter 1: Project Setup

### Project Pre-requisites

- install python3
- install pip3

### To Setup the project

1. `python3 -m venv .venv` : create a virtual environment
2. `.venv\Scripts\activate` : activate the virtual environment
3. `pip install -r requirements.txt` : install all the dependencies

### To Run the project

1. you need to active the virtual environmens `.venv\Scripts\activate`
2. if you already have the virtual environment active continue with the next step
3. `flask --app app run --port 8080`

### Check if the project is running

open your browser and go to `http://localhost:8080/hello-world`
you should see a resposne like this:

``` json
{
    "message": "Hello World"
}
```

## Chapter 2: Basic API

In this chapter just create a basic API with flask (mock the data for now)

you can check the code in the branch `chapter-2-basic-api`

on this chapter we create the following endpoints:

### Endpoints

- POST: `api/v1/users/` : create a new user
- GET : `api/v1/users/` : get all the users
- GET : `api/v1/users/<id>` : get a specific user
- PUT : `api/v1/users/<id>` : update a specific user
- DELETE : `api/v1/users/<id>` : delete a specific user

### project structure:

``` bash
api-tutorial-flask/
├─ controllers/
│  ├─ user_controller.py
│  
├─ models/
│  ├─ user.py
│  
├─ payload/
│  ├─ request/
│  │  ├─ user_request.py
│  ├─ response/
│  │  ├─ user_dto.py
│  
├─ routes/
│  ├─ routes.py
│  
├─ services/
│  ├─ user_service.py
│  
├─ utils/
│  ├─ mock_users.py
│  
├─ app.py

```

### Simple API Implementation

1. Create a model
2. Create a DTO (Data Transfer Object)
3. Create a Request
4. Create a Service (Business Logic)
5. Create a Controller and link it  with the Service
6. Link the controller with the routes

and all the rest is learning by this example
