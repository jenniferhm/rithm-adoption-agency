from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField, SelectField


class AddPetForm(FlaskForm):
    """Form to add new pets."""

    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = FloatField("Age")
    notes = StringField("Notes")

