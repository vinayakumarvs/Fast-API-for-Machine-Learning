# FastAPI Learning Repository

This repository contains various FastAPI demos, projects, and integrations to help you learn and experiment with FastAPI in Python.

## Structure

- `main.py` — Entry point for basic FastAPI demo.
- `building_api/` — Contains examples of building FastAPI apps, including async and sync demos, pydantic usage, and models.
- `database_integration/` — Shows how to integrate FastAPI with databases, including a CRUD app using SQLite.
- `machine_learning_integration/` — Demonstrates integrating machine learning models with FastAPI, including model training, prediction, and serialization.
- `fast-api-venv/` — Python virtual environment for package management.

## Getting Started

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd fast-api
   ```
2. **Activate the virtual environment**
   ```sh
   fast-api-venv\Scripts\activate
   ```
3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install FastAPI and Uvicorn:)*
   ```sh
   pip install fastapi uvicorn
   ```

## Running Examples

### Basic FastAPI App
```sh
uvicorn main:app --reload
```

### Building API Demos
```sh
uvicorn building_api.main:app --reload
```

### Database CRUD Example
```sh
uvicorn database_integration.crud-app.main:app --reload
```

### Machine Learning Integration
```sh
uvicorn machine_learning_integration.ml_model.main:app --reload
```

## Learning Topics
- FastAPI basics (routes, requests, responses)
- Async vs sync endpoints
- Pydantic models and validation
- Database integration (CRUD, SQLite)
- Machine learning model serving

## Useful Commands
- Run any FastAPI app: `uvicorn <module>:app --reload`
- Install packages: `pip install <package>`
- Deactivate venv: `deactivate`

## References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

---
Feel free to explore each folder and file for hands-on FastAPI learning!
