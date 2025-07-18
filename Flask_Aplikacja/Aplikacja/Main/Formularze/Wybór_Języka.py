# Formularz Wyboru Języka

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import SelectField as SELECT_FIELD
from wtforms import SubmitField as SUBMIT_FIELD
from wtforms import validators as VALIDATORS


#! Main
class Formularz_Wyboru_Języka(FLASK_FORM):
    Pole_Język = SELECT_FIELD(
        "Motyw",
        choices=[("pl", "Polski"), ("en", "English")],
        validators=[VALIDATORS.DataRequired()],
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
