from app import db
from sqlalchemy.orm import relationship

class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    todos = relationship("Todo", secondary="todo_tags", back_populates="tags")

    def __repr__(self):
        return f"<Tag {self.name}>"
