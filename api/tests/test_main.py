from fastapi import status
from fastapi.routing import APIRoute
from fastapi.testclient import TestClient

from word_counter.main import app

client = TestClient(app)


def test_main_root():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.url.path == "/docs"


def test_main_word_count_ok():
    # test if with the right input body it returns ok
    ok_body = {
        "input_text": """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
                      incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
                      exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
                      dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur
                      Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit
                      anim id est laborum."""
    }
    response = client.post("/word-count", json=ok_body)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["word_count"] == 69


def test_main_word_count_not_ok_int():
    # test if without the righ input body it returns an error
    not_ok_body_int = {"input_text": 1}
    response = client.post("/word-count", json=not_ok_body_int)
    detail = response.json()["detail"]

    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert detail[0]["type"] == "string_type"
    assert detail[0]["loc"] == ["body", "input_text"]
    assert detail[0]["msg"] == "Input should be a valid string"


def test_main_word_count_not_ok_missing():
    not_ok_body_missing = {"whatever": "some text"}
    response = client.post("/word-count", json=not_ok_body_missing)
    detail = response.json()["detail"]
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert detail[0]["type"] == "missing"
    assert detail[0]["loc"] == ["body", "input_text"]
    assert detail[0]["msg"] == "Field required"


def test_main_api_routes():
    api_routes = [r.path for r in app.routes if type(r) is APIRoute]
    docs_route = [r.path for r in app.routes if r.path == "/docs"]

    assert len(api_routes) == 2
    assert len(docs_route) == 1
    assert "/word-count" in api_routes
    assert "/" in api_routes
    assert "/docs" in docs_route


def test_main_api_middlewares():
    middleware = app.user_middleware.pop()
    REFERENCE = {
        "origins": [
            "http://localhost:4173",
            "http://127.0.0.1:4173",
            "http://localhost:5173",
            "http://127.0.0.1:5173",
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "headers": ["*"],
    }

    assert REFERENCE["origins"] == middleware.options["allow_origins"]
    assert REFERENCE["methods"] == middleware.options["allow_methods"]
    assert REFERENCE["headers"] == middleware.options["allow_headers"]
