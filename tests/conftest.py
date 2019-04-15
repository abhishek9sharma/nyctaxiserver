import pytest
from app import APIServer

@pytest.fixture
def testserver():
    server = APIServer('testing')
    return server.app