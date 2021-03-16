import pytest
import sys
sys.path.insert(0, '/Users/kabrams/ken_projects/quick_game')
import app as flask_app



@pytest.fixture
def app():
	yield flask_app


@pytest.fixture
def client(app):
	return app.test_client()