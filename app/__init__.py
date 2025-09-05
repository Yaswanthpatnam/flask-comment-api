from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# defining SQLALCHEMY
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # configuring SQlite DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # connecting DB with Flask app
    db.init_app(app)
    
    # registering routes
    from app.routes.comment_routes import comment_bp
    app.register_blueprint(comment_bp, url_prefix='/api')
    
    # creates DB tables
    with app.app_context():
        db.create_all()
    
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "ok"}), 200       
       
    return app