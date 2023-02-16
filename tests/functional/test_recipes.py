"""
This file (test_recipes.py) contains the functional tests for the `recipes` blueprint.
"""


def test_get_home_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    header_items = [
        b"Unseen University",
        b"Wizardry Unclasses",
        b"Improbability Blog",
        b"Agnes Nutter"
        b"About",
        b"Register",
    ]
    response = test_client.get("/")
    assert response.status_code == 200
    for header_item in header_items:
        assert header_item in response.data
