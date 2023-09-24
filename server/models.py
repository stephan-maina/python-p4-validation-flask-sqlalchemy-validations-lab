from app import db
from sqlalchemy.orm import validates

class FootballEntity(db.Model):
    __tablename__ = 'football_entities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        return f'<FootballEntity: {self.name}>'

    @validates('name')
    def validate_name(self, key, value):
        if len(value.strip()) == 0:
            raise ValueError('Name cannot be empty or contain only whitespace')
        return value

