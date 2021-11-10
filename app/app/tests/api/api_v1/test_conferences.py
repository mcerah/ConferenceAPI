from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.db.db import get_session

from app.core.config import settings


def test_create_conference(
    client: TestClient, db: Session
) -> None:
    data = {"title": "PyCon", "description": "PyCon 2021", "start_date":"2021-11-10T16:39:12", "end_date":"2021-11-13T16:39:12"}
    response = client.post(
        f"{settings.API_V1_STR}/conferences/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["description"] == data["description"]
    assert "id" in content

