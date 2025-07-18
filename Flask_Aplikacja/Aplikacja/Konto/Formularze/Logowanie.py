"""Moduł formularza logowania."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    PasswordField as PASSWORD_FIELD,
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Logowanie(FLASK_FORM):
    """Formularz logowania użytkownika.

    :param Pole_Login: Pole na login użytkownika.
    :type Pole_Login: wtforms.fields.StringField
    :param Pole_Hasło: Pole na hasło użytkownika.
    :type Pole_Hasło: wtforms.fields.PasswordField
    :param Pole_Submit: Przycisk wysyłający formularz.
    :type Pole_Submit: wtforms.fields.SubmitField
    """

    Pole_Login = STRING_FIELD(
        "Login", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Hasło = PASSWORD_FIELD(
        "Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)]
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
