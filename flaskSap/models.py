from app import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __str__(self) -> str:
        return (f'''
            Id: {self.id}'
            Name: {self.name}'
            LastName: {self.lastName}'
            Email: {self.email}'
        ''')