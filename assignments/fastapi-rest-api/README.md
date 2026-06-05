# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to design and build a simple RESTful API using the FastAPI framework, including request handling, data validation with Pydantic, CRUD operations, and automatic API docs.

## 📝 Tasks

### 🛠️ Project Setup and Installation

#### Description

Create a new FastAPI project and install required dependencies. Provide instructions to run the app locally.

#### Requirements
Completed project should:

- Include a `requirements.txt` listing FastAPI and Uvicorn (or equivalent)
- Provide setup instructions to install dependencies and run the server
- Start a FastAPI app that responds on `http://localhost:8000`

### 🛠️ Define Data Models with Pydantic

#### Description

Design Pydantic models for request and response validation for a simple resource (e.g., `Item` with `id`, `name`, `description`, and `price`).

#### Requirements
Completed project should:

- Define request and response models using Pydantic
- Use type hints for all endpoint parameters
- Validate incoming JSON payloads and return clear validation errors

### 🛠️ Implement CRUD Endpoints

#### Description

Implement Create, Read, Update, and Delete endpoints for the chosen resource.

#### Requirements
Completed project should:

- Implement endpoints: `POST /items/`, `GET /items/`, `GET /items/{id}`, `PUT /items/{id}`, `DELETE /items/{id}`
- Return appropriate HTTP status codes (`201` for created, `200` for success, `404` for not found, etc.)
- Use an in-memory store (e.g., a Python dict) for simplicity or document how to swap in a real DB

### 🛠️ Documentation and Auto-generated API Docs

#### Description

Verify that FastAPI's automatic documentation is available and provide examples of using the interactive docs.

#### Requirements
Completed project should:

- Expose interactive docs at `/docs` (Swagger UI) and `/redoc`
- Include at least one example request/response in the README

### 🛠️ Error Handling, Dependencies, and Testing

#### Description

Add basic error handling, dependency injection examples, and a small test demonstrating an endpoint.

#### Requirements
Completed project should:

- Return JSON error responses with helpful messages for invalid operations
- Demonstrate one dependency (e.g., a simple header-based auth dependency) used by an endpoint
- Include at least one test (pytest) that calls an endpoint using FastAPI's `TestClient`

## 🧪 Example Requests

- Create item:

```http
POST /items/
Content-Type: application/json

{
  "name": "Widget",
  "description": "A useful widget",
  "price": 9.99
}
```

- Response:

```http
HTTP/1.1 201 Created
{
  "id": 1,
  "name": "Widget",
  "description": "A useful widget",
  "price": 9.99
}
```

## 📁 Suggested Starter Files (optional)

- `main.py` — FastAPI app and endpoint definitions
- `models.py` — Pydantic models
- `store.py` — simple in-memory store
- `requirements.txt` — `fastapi`, `uvicorn`, `pytest`, `requests`
- `tests/test_items.py` — example pytest using `TestClient`

## ✅ Submission

- Provide the code in a folder named `assignments/fastapi-rest-api/` with a `README.md` and any starter files you include.
- Ensure the README follows this template and clearly documents how to run and test the API.
