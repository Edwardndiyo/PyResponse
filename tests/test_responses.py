# import json  
# from pyresponse.response import Ok, BadRequest  # Ensure you're importing correctly

# def test_ok_response():
#     response = Ok({"key": "value"})  # Create an instance of Ok response
#     assert response.status_code == 200

#     # Decode the response body (since it's bytes) into a dictionary
#     response_body = json.loads(response.body.decode("utf-8"))
#     assert response_body["message"] == "Success"

# def test_bad_request():
#     response = BadRequest("Invalid request")  # Create an instance of BadRequest response
#     assert response.status_code == 400

#     # Decode the response body (since it's bytes) into a dictionary
#     response_body = json.loads(response.body.decode("utf-8"))
#     assert response_body["message"] == "Invalid request"




import json 
from pyresponse.response import (
    Ok, Created, Accepted, NoContent, BadRequest, Unauthorized, Forbidden,
    NotFound, Conflict, UnprocessableEntity, TooManyRequests,
    InternalServerError, ServiceUnavailable
)



def test_ok_response():
    response = Ok({"key": "value"})
    assert response.status_code == 200
    assert response.body == b'{"status":200,"message":"Success","data":{"key":"value"}}'

def test_created_response():
    response = Created({"id": 1})
    assert response.status_code == 201
    assert response.body == b'{"status":201,"message":"Resource created","data":{"id":1}}'

def test_no_content_response():
    response = NoContent()
    assert response.status_code == 204
    assert response.body == b'{"status":204,"message":"No content"}'

def test_bad_request():
    response = BadRequest()
    assert response.status_code == 400
    assert response.body == b'{"status":400,"message":"Bad request","error_code":"BAD_REQUEST"}'

def test_unauthorized():
    response = Unauthorized()
    assert response.status_code == 401
    assert response.body == b'{"status":401,"message":"Unauthorized","error_code":"UNAUTHORIZED"}'

def test_not_found():
    response = NotFound()
    assert response.status_code == 404
    assert response.body == b'{"status":404,"message":"Not found","error_code":"NOT_FOUND"}'

def test_internal_server_error():
    response = InternalServerError()
    assert response.status_code == 500
    assert response.body == b'{"status":500,"message":"Internal server error","error_code":"INTERNAL_SERVER_ERROR"}'

def test_service_unavailable():
    response = ServiceUnavailable()
    assert response.status_code == 503
    assert response.body == b'{"status":503,"message":"Service unavailable","error_code":"SERVICE_UNAVAILABLE"}'

def test_ok_response_with_none():
    response = Ok(None)
    assert response.status_code == 200
    assert response.body == b'{"status":200,"message":"Success","data":null}'

def test_empty_data():
    response = Ok({})
    assert response.status_code == 200
    assert response.body == b'{"status":200,"message":"Success","data":{}}'

def test_unexpected_input():
    response = Ok(["list", "of", "values"])
    assert response.status_code == 200
    assert response.body == b'{"status":200,"message":"Success","data":["list","of","values"]}'

def test_error_with_custom_message():
    response = BadRequest("Custom error message", {"info": "Invalid data"})
    assert response.status_code == 400
    assert response.body == b'{"status":400,"message":"Custom error message","data":{"info":"Invalid data"},"error_code":"BAD_REQUEST"}'
