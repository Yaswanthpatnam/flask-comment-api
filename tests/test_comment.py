import os
import sys
import pytest

# Add app directory to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.comment import Comment

# Setting up test client and in-memory DB
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
        yield app.test_client()
        # Clean up after each test
        db.session.remove()
        db.drop_all()

# Test: Add comment
def test_add_comment(client):
    res = client.post("/api/comments", json={
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
    client.post("/api/comments", json={
        "task_id": 2,
        "content": "Second comment"
    })
    res = client.get("/api/comments")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data["comments"]) == 1  # Should only have the one we just added

# Test: Get single comment
def test_get_single_comment(client):
    # Add comment first
    add_res = client.post("/api/comments", json={
        "task_id": 3,
        "content": "Test single comment"
    })
    comment_id = add_res.get_json()["comment"]["id"]
    
    # Get the comment
    res = client.get(f"/api/comments/{comment_id}")
    assert res.status_code == 200
    data = res.get_json()
    assert data["comment"]["id"] == comment_id
    assert data["comment"]["content"] == "Test single comment"

# Test: Update comment
def test_update_comment(client):
    # Add comment to update
    add = client.post("/api/comments", json={
        "task_id": 3,
        "content": "Initial content"
    })
    comment_id = add.get_json()["comment"]["id"]

    # Now update it
    update = client.put(f"/api/comments/{comment_id}", json={
        "content": "Content updated"
    })
    assert update.status_code == 200
    updated = update.get_json()
    assert updated["comment"]["content"] == "Content updated"

# Test: Delete comment
def test_delete_comment(client):
    # Add comment to delete
    add = client.post("/api/comments", json={
        "task_id": 4,
        "content": "Will be deleted"
    })
    comment_id = add.get_json()["comment"]["id"]

    # Deleting now
    delete = client.delete(f"/api/comments/{comment_id}")
    assert delete.status_code == 200
    result = delete.get_json()
    assert f"{comment_id}" in result["message"]

# Test: Filter comments by task_id
def test_filter_comments(client):
    # Add comments for different tasks
    client.post("/api/comments", json={"task_id": 5, "content": "Task 5 comment"})
    client.post("/api/comments", json={"task_id": 6, "content": "Task 6 comment"})
    
    # Filter by task_id
    res = client.get("/api/comments?task_id=5")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data["comments"]) == 1  # Should only find the one with task_id=5
    assert data["comments"][0]["task_id"] == 5