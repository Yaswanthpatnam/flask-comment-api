from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# defining SQLALCHEMY
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # configuring SQlite DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comments.db'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # connecting DB with Flask app

    db.init_app(app)
    
    # registering routes
    
    from app.routes.comment_routes import comment_bp
    app.register_blueprint(comment_bp)
    
    # creates DB tables
    
    with app.app_context():
        db.create_all()
       
       
    return app    

