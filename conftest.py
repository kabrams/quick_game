import pytest
from . import app

@pytest.fixture
def test_app():
	test_app = app()
	return app
	