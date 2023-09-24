from app import db, YourModel

if __name__ == '__main__':
    db.create_all()

    # Add initial data to the database, including 'Liverpool FC' and 'CR7'
    initial_data = ['Data 1', 'Data 2', 'Liverpool FC', 'CR7']

    for data in initial_data:
        entry = YourModel(name=data)
        db.session.add(entry)

    db.session.commit()
