from app import db
from datetime import datetime, timezone

class TaskCompletionHistory(db.Model):
    __tablename__ = 'task_completion_history'

    id = db.Column(db.Integer, primary_key=True)
    todo_id = db.Column(db.Integer, db.ForeignKey('todos.id'), nullable=False)
    completed_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    todo = db.relationship("Todo", back_populates="completion_history")

    def __repr__(self):
        return f"<Completed {self.completed_at} for Todo {self.todo_id}>"
