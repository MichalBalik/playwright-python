import json
import time
import pytest
from playwright.sync_api import sync_playwright
from jsonschema import validate, ValidationError

# Loading user data from a JSON file
with open("tests/api/test-data/users.json") as f:
    users = json.load(f)

# Schema for response validation
create_user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
        "name": {"type": "string"},
        "job": {"type": "string"},
    },
    "required": ["id", "createdAt", "name", "job"]
}

RESPONSE_TIME_LIMIT = 100  # ms

@pytest.mark.parametrize("user", users)
def test_create_user(user):
    with sync_playwright() as p:
        request_context = p.request.new_context()
        
        start_time = time.time()
        response = request_context.post("https://reqres.in/api/users", data=user)
        response_time = (time.time() - start_time) * 1000 

        # HTTP status
        assert response.status == 201, f"Expected 201, got {response.status}"

        # Response time
        assert response_time < RESPONSE_TIME_LIMIT, f"Response took {response_time}ms"

        body = response.json()

        # ID a createdAt
        assert "id" in body, "Response missing 'id'"
        assert "createdAt" in body, "Response missing 'createdAt'"

        # Schema validation
        try:
            validate(instance=body, schema=create_user_schema)
        except ValidationError as e:
            pytest.fail(f"Schema validation failed: {e}")
