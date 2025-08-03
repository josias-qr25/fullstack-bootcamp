from app import db
from datetime import datetime, timezone
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship
import enum

# Enum for status
class TodoStatus(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    BLOCKED = "blocked"

# Join table for tags
todo_tags = db.Table(
    'todo_tags',
    db.Column('todo_id', db.Integer, db.ForeignKey('todos.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
)

class Todo(db.Model):
    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum(TodoStatus), default=TodoStatus.TODO, nullable=False)
    due_date = db.Column(db.DateTime, nullable=True)
    category = db.Column(db.String(50), nullable=True)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, onupdate=lambda: datetime.now(timezone.utc))
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    user = relationship("User", back_populates="todos")
    tags = relationship("Tag", secondary=todo_tags, back_populates="todos")
    completion_history = relationship("TaskCompletionHistory", back_populates="todo", cascade="all, delete-orphan")

    @hybrid_property
    def is_overdue(self):
        return self.due_date and self.status != TodoStatus.COMPLETED and self.due_date < datetime.now(timezone.utc)

    @hybrid_property
    def is_deleted(self):
        return self.deleted_at is not None

    def __repr__(self):
        return f"<Todo {self.title} ({self.status.value})>"
