from typing import  Generator

import pytest
from fastapi.testclient import TestClient

from app.core.config import settings
from app.db.db import get_session
from app.main import app


@pytest.fixture(scope="session")
def db() -> Generator:
    yield get_session()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
