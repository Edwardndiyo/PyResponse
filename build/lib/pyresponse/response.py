print("Running response.py...")  # Debugging check

from fastapi.responses import JSONResponse
from flask import jsonify, make_response, has_request_context

# Universal function to handle both FastAPI and Flask
def build_response(status_code, data=None, message=None, error_code=None):
    """
    Generate a response in a consistent structure.

    Args:
        status_code (int): HTTP status code.
        data (dict | None): The actual response data.
        message (str | None): Optional message to include.
        error_code (str | None): A specific error code identifier for debugging.

    Returns:
        Flask `Response` or FastAPI `JSONResponse`
    """
    response_body = {"status": status_code}

    if message:
        response_body["message"] = message

    # Ensure "data" is included **only** when explicitly expected
    if data is not None or (data is None and status_code == 200):  
        response_body["data"] = data  

    if error_code:
        response_body["error_code"] = error_code  # Useful for frontend debugging

    # More reliable Flask detection  
    if has_request_context():
        return make_response(jsonify(response_body), status_code)

    return JSONResponse(content=response_body, status_code=status_code)


# Response Helpers
def Ok(data=None, message="Success"):
    return build_response(200, data, message)

def Created(data=None, message="Resource created"):
    return build_response(201, data, message)

def Accepted(data=None, message="Request accepted"):
    return build_response(202, data, message)

def NoContent():
    return build_response(204, message="No content")

def BadRequest(message="Bad request", data=None, error_code="BAD_REQUEST"):
    return build_response(400, data, message, error_code)

def Unauthorized(message="Unauthorized", data=None, error_code="UNAUTHORIZED"):
    return build_response(401, data, message, error_code)

def Forbidden(message="Forbidden", data=None, error_code="FORBIDDEN"):
    return build_response(403, data, message, error_code)

def NotFound(message="Not found", data=None, error_code="NOT_FOUND"):
    return build_response(404, data, message, error_code)

def Conflict(message="Conflict", data=None, error_code="CONFLICT"):
    return build_response(409, data, message, error_code)

def UnprocessableEntity(message="Unprocessable Entity", data=None, error_code="UNPROCESSABLE_ENTITY"):
    return build_response(422, data, message, error_code)

def TooManyRequests(message="Too many requests", data=None, error_code="TOO_MANY_REQUESTS"):
    return build_response(429, data, message, error_code)

def InternalServerError(message="Internal server error", data=None, error_code="INTERNAL_SERVER_ERROR"):
    return build_response(500, data, message, error_code)

def ServiceUnavailable(message="Service unavailable", data=None, error_code="SERVICE_UNAVAILABLE"):
    return build_response(503, data, message, error_code)

if __name__ == "__main__":
    print("Response module is running...")
