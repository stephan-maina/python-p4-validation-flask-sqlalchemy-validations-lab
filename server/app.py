from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates  # Add this import

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Replace with your actual database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

if __name__ == '__main__':
    db.create_all()

    # Add initial data to the database, including 'Liverpool FC' and 'CR7'
    initial_data = ['Data 1', 'Data 2', 'Liverpool FC', 'CR7']

    for data in initial_data:
        entry = FootballEntity(name=data)
        db.session.add(entry)

    db.session.commit()
