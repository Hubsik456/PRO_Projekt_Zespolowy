"""Moduł formularza wyboru motywu."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    SelectField as SELECT_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Wyboru_Motywu(FLASK_FORM):
    """Formularz do wyboru motywu kolorystycznego aplikacji.

    :param Pole_Motyw: Pole wyboru jednego z dostępnych motywów.
    :type Pole_Motyw: wtforms.fields.SelectField
    :param Pole_Submit: Przycisk wysyłający formularz.
    :type Pole_Submit: wtforms.fields.SubmitField
    """

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
