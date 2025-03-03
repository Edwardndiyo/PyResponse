# PyResponse-paradox 🚀  
A lightweight and structured response builder for Flask and FastAPI applications.  

## 📌 Overview  
PyResponse-paradox provides a consistent and structured way to return API responses in Flask and FastAPI applications.  
It helps standardize response formats while supporting custom messages, error codes, and flexible status handling.  

## 📖 Features  
✅ Standardized JSON response format  
✅ Supports both Flask and FastAPI frameworks  
✅ Predefined response helpers for common HTTP status codes  
✅ Customizable messages, data, and error codes  
✅ Fully tested with pytest  

## 📦 Installation  

To install PyResponse-paradox, simply run:

```sh
pip install pyresponse-paradox
```

## 🚀 Usage

🔹 Import & Use in Flask

```py
from flask import Flask
from responses import Ok, BadRequest, NotFound

app = Flask(__name__)

@app.route("/success")
def success():
    return Ok({"user": "John Doe"}, message="Request successful!")

@app.route("/error")
def error():
    return BadRequest(message="Invalid request")

if __name__ == "__main__":
    app.run(debug=True)
```

🔹 Import & Use in FastAPI

```py
from fastapi import FastAPI
from responses import Ok, NotFound

app = FastAPI()

@app.get("/data")
def get_data():
    return Ok({"id": 1, "name": "Alice"})

@app.get("/missing")
def missing():
    return NotFound(message="Item not found")
```


##🔧 Response Structure

Every response follows a structured JSON format:

```json
{
    "status": 200,
    "message": "Success",
    "data": {...},
    "error_code": "OPTIONAL"
}
```

##🛠 Response Builder Function

```py
def build_response(status_code, data=None, message=None, error_code=None):
    response_body = {"status": status_code}

    if message:
        response_body["message"] = message
    if data is not None:
        response_body["data"] = data
    if error_code:
        response_body["error_code"] = error_code

    return JSONResponse(content=response_body, status_code=status_code)
```


##📡 Available Response Helpers

### ✅ Success Responses  

| Function                  | HTTP Code | Default Message          | Example                 |
|---------------------------|----------|--------------------------|-------------------------|
| `Ok(data, message)`       | 200      | "Success"                | `Ok({"id": 1})`        |
| `Created(data, message)`  | 201      | "Created successfully"   | `Created({"user": "Alice"})` |
| `NoContent(message)`      | 204      | "No content"             | `NoContent()`          |

### ❌ Error Responses  

| Function                            | HTTP Code | Default Message            | Error Code             |
|--------------------------------------|----------|----------------------------|------------------------|
| `BadRequest(message, error_code)`   | 400      | "Bad request"              | `"BAD_REQUEST"`        |
| `Unauthorized(message, error_code)` | 401      | "Unauthorized"             | `"UNAUTHORIZED"`       |
| `Forbidden(message, error_code)`    | 403      | "Forbidden"                | `"FORBIDDEN"`          |
| `NotFound(message, error_code)`     | 404      | "Not found"                | `"NOT_FOUND"`          |
| `InternalServerError(message, error_code)` | 500 | "Internal server error" | `"INTERNAL_SERVER_ERROR"` |
| `ServiceUnavailable(message, error_code)` | 503 | "Service unavailable" | `"SERVICE_UNAVAILABLE"` |




##📁 Project Structure
```
PyResponse/
│── responses.py               # Main response helper functions
│── tests/
│   ├── test_responses.py      # Unit tests for response functions
│── .github/workflows/         # GitHub CI/CD pipeline (if applicable)
│── requirements.txt           # Dependencies
│── README.md                  # Documentation
```


##🤝 Contribution

###Got ideas? Found a bug? Feel free to contribute!

- Fork the repository
- Create a new branch
- Commit changes
- Push to your fork
- Create a Pull Request

  
##🛠️ Future Enhancements

✅ Add logging for response tracking
✅ Support for more status codes
✅ Async support for FastAPI



##📜 License
MIT License. Use it however you like! 🚀



