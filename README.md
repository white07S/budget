![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/white07S/budget)
![GitHub repo size](https://img.shields.io/github/repo-size/white07S/budget)
![GitHub last commit](https://img.shields.io/github/last-commit/white07S/budget)

# FamilyBudget
An API for Family Budget project in Django 

- [x] Implementation Technologies:
  - Backend:
    - [Python](https://www.python.org/downloads/) 3.8
    - [FastAPI](https://fastapi.tiangolo.com/) 0.83
  - Communication:
    - REST API
      - Backend: [Rest Framework]
  - Docs:
      - [Markdown Lint](https://github.com/igorshubovych/markdownlint-cli)
      
# Compile and Run

```
chmod +x /scripts/build.sh
```

```
./scripts/build.sh
```

```
docker-compose up -d
```

* if want to test backend
```
./scripts/test_backend.sh
```


      
- [x] Functionalities
  - [x] User Registration
  - [x] Email validation (PyDantic)
  - [x] Passlib Encryption for password
  - [x] JWT Token Authorization
  - [x] Users can create budgets
  - [x] Users can share to any other users
  - [x] Tests
  - [x] Pagination
  - [x] Filtering
  - [x] Redis Implemented for Caching
  - [x] Search based on Category(Income,Expenses)
  - [x] CORS configuration (Its configured for all domain) [For production: it will be restricted to list or orgin needed for api]
  - [x] NGINX added
  - [ ] Frontend half-done



- [x] Get methods
- [x] /users/{id} by id
- [x] /budget 
- [x] /budget based on URL pagination and serach by category like /budget?limit=10@search="expenses"
- [x] /getallbudget
  

- [x] Post Methods
- [x] /login
- [x] /signup
- [x] /budget
- [x] /share with id as list in input


NOTE: for production we need to change docker param and setup env 

