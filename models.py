from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_NOT_AVAIL = "https://via.placeholder.com/250?text=No+Image+Available"

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """"Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, default=DEFAULT_IMG_NOT_AVAIL)

    age = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, nullable=False, default=True)
