import pytest
import requests


def test_get_users_api():
    url = "https://reqres.in/api/users?page=1"
    response = requests.get(url)

    # Cloudflare may block automated requests
    if response.status_code != 200:
        pytest.skip("Reqres API blocked by Cloudflare")

    # Status code
    assert response.status_code == 200

    body = response.json()

    # Assert total
    assert "total" in body
    assert isinstance(body["total"], int)

    # Assert pagination correctness
    assert len(body["data"]) <= body["per_page"], "The number of records per page must not exceed 'per_page'"

    assert len(body["data"]) == body["per_page"]

    # Assert last_name for first two users
    assert "last_name" in body["data"][0]
    assert "last_name" in body["data"][1]

    # Bonus – data type assertions
    for user in body["data"]:
        assert isinstance(user["id"], int)
        assert isinstance(user["email"], str)
        assert isinstance(user["first_name"], str)
        assert isinstance(user["last_name"], str)
        assert isinstance(user["avatar"], str)
