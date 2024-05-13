from fastapi.testclient import TestClient

from src import app
from tests.BaseTest import BaseTest


class ApiBaseTest(BaseTest):
    test_api = TestClient(app)
