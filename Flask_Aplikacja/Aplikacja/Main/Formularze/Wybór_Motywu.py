# Formularz Wyboru Motywu

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import SelectField as SELECT_FIELD
from wtforms import SubmitField as SUBMIT_FIELD
from wtforms import validators as VALIDATORS


#! Main
class Formularz_Wyboru_Motywu(FLASK_FORM):
    Pole_Motyw = SELECT_FIELD(
        "Motyw",
        choices=[
            ("brite", "Brite"),
            ("pulse", "Pulse"),
            ("united", "United"),
            ("zephyr", "Zephyr"),
            ("sketchy", "Sketchy"),
        ],
        validators=[VALIDATORS.DataRequired()],
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
