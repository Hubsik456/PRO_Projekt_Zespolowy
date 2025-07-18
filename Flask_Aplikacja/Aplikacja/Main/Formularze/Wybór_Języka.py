"""Moduł formularza wyboru języka."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    SelectField as SELECT_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Wyboru_Języka(FLASK_FORM):
    """Formularz do wyboru języka interfejsu aplikacji.

    :param Pole_Język: Pole wyboru języka (Polski lub Angielski).
    :type Pole_Język: wtforms.fields.SelectField
    :param Pole_Submit: Przycisk wysyłający formularz.
    :type Pole_Submit: wtforms.fields.SubmitField
    """

    Pole_Język = SELECT_FIELD(
        "Motyw",
        choices=[("pl", "Polski"), ("en", "English")],
        validators=[VALIDATORS.DataRequired()],
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
