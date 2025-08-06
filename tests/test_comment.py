# test_comment.py

import os
import sys
import pytest

# Add app directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db

# Setting up test client and in-memory DB
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        db.create_all()

    with app.test_client() as client:
        yield client

# Test: Add comment
def test_add_comment(client):
    res = client.post("/comments", json={
        "task_id": 1,
        "content": "Just testing the add feature"
    })
    assert res.status_code == 201
    data = res.get_json()
    assert data["comment"]["task_id"] == 1
    assert data["comment"]["content"] == "Just testing the add feature"

# Test: Get all comments
def test_get_all_comments(client):
    # Add one comment before fetching
    client.post("/comments", json={
        "task_id": 2,
        "content": "Second comment"
    })
    res = client.get("/comments")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data["comments"]) >= 1

# Test: Update comment
def test_update_comment(client):
    # Add comment to update
    add = client.post("/comments", json={
        "task_id": 3,
        "content": "Initial content"
    })
    comment_id = add.get_json()["comment"]["id"]

    # Now update it
    update = client.put(f"/comments/{comment_id}", json={
        "content": "Content updated"
    })
    assert update.status_code == 200
    updated = update.get_json()
    assert updated["comment"]["content"] == "Content updated"

# Test: Delete comment
def test_delete_comment(client):
    # Add comment to delete
    add = client.post("/comments", json={
        "task_id": 4,
        "content": "Will be deleted"
    })
    comment_id = add.get_json()["comment"]["id"]

    # Deleting now
    delete = client.delete(f"/comments/{comment_id}")
    assert delete.status_code == 200
    result = delete.get_json()
    assert f"{comment_id}" in result["message"]
