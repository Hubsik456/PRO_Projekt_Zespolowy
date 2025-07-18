"""Moduł formularza rejestracji."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    EmailField as EMAIL_FIELD,
    PasswordField as PASSWORD_FIELD,
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Rejestracja(FLASK_FORM):
    """Formularz rejestracji nowego użytkownika.

    :param Pole_Login: Pole na login użytkownika.
    :type Pole_Login: wtforms.fields.StringField
    :param Pole_Hasło_1: Pole na hasło użytkownika.
    :type Pole_Hasło_1: wtforms.fields.PasswordField
    :param Pole_Hasło_2: Pole do powtórzenia hasła.
    :type Pole_Hasło_2: wtforms.fields.PasswordField
    :param Pole_Email: Pole na adres email użytkownika (opcjonalne).
    :type Pole_Email: wtforms.fields.EmailField
    :param Pole_Submit: Przycisk wysyłający formularz.
    :type Pole_Submit: wtforms.fields.SubmitField
    """

    Pole_Login = STRING_FIELD(
        "Login", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Hasło_1 = PASSWORD_FIELD(
        "Hasło",
        [
            VALIDATORS.DataRequired(),
            VALIDATORS.EqualTo("Pole_Hasło_2"),
            VALIDATORS.length(min=8, max=100),
        ],
    )
    Pole_Hasło_2 = PASSWORD_FIELD(
        "Powtórz Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)]
    )
    Pole_Email = EMAIL_FIELD(
        "E-Mail", [VALIDATORS.Optional(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
