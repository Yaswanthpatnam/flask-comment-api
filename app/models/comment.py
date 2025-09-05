from app import db

# Creating db model (formatting data where and how to store)
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(260), nullable=False)
    
    def __repr__(self):
        return f"<comment{self.id} - Task {self.task_id}>"