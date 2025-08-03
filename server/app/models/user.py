from app import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    preferences = db.Column(db.JSON, nullable=True)

    todos = relationship("Todo", back_populates="user")

    def __repr__(self):
        return f"<User {self.name}>"
