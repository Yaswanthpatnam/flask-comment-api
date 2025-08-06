from flask import Blueprint, jsonify,request
from app import db
from app.models.comment import Comment

# Registering blueprint
comment_bp = Blueprint('comment', __name__)

# Route to add a comment
@comment_bp.route('/comments', methods=["POST"])
def add_comment():
    # storing data initially in json format 
    data = request.get_json()
    
    # Extract data from Json
    task_id = data.get("task_id")
    content = data.get("content")
    
    # ensure to get required inputs
    if not task_id or not content:
        return jsonify({"error":"task_id and content are required"}), 400
    
    # Creating new comment object
    new_comment = Comment(task_id = task_id, content = content)
    
    # Add to DB
    db.session.add(new_comment)
    db.session.commit()
    
    return jsonify({
        "message":"Comment added Successfully",
        "comment": {
            "id":new_comment.id,
            "task_id":new_comment.task_id,
            "content":new_comment.content,
        }
    }), 201

    
@comment_bp.route('/comments/<int:comment_id>', methods=["PUT"])
def update_comment(comment_id):
    data = request.get_json()
    content = data.get("content")

    if not content:
        return jsonify({"error": "content is required"}), 400

    # Fetch the comment from DB
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    # Update and save
    comment.content = content
    db.session.commit()

    return jsonify({
        "message": "Comment updated successfully",
        "comment": {
            "id": comment.id,
            "task_id": comment.task_id,
            "content": comment.content
        }
    }), 200
    
# Route to delete a comment
@comment_bp.route('/comments/<int:comment_id>', methods=["DELETE"])
def delete_comment(comment_id):
    comment = Comment.query.get(comment_id)

    if not comment:
        return jsonify({"error": "Comment not found"}), 404

    db.session.delete(comment)
    db.session.commit()

    return jsonify({"message": f"Comment with ID {comment_id} deleted successfully"}), 200

# Route to get all comments
@comment_bp.route('/comments', methods=["GET"])
def get_comments():
    comments = Comment.query.all()

    all_comments = [
        {
            "id": comment.id,
            "task_id": comment.task_id,
            "content": comment.content
        } for comment in comments
    ]

    return jsonify({
        "comments": all_comments
    }), 200
