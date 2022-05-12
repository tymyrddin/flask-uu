import pytest
from project import create_app
from flask_fontawesome import FontAwesome


@pytest.fixture(scope="module")
def test_client():
    flask_app = create_app()
    fa = FontAwesome(flask_app)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        yield testing_client  # this is where the testing happens!
