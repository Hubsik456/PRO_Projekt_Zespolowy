"""Moduł formularza zmiany hasła."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    PasswordField as PASSWORD_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Zmiana_Hasła(FLASK_FORM):
    """Formularz do zmiany hasła przez zalogowanego użytkownika.

    :param Pole_Stare_Hasło: Pole na stare hasło użytkownika.
    :type Pole_Stare_Hasło: wtforms.fields.PasswordField
    :param Pole_Nowe_Hasło_1: Pole na nowe hasło.
    :type Pole_Nowe_Hasło_1: wtforms.fields.PasswordField
    :param Pole_Nowe_Hasło_2: Pole do powtórzenia nowego hasła.
    :type Pole_Nowe_Hasło_2: wtforms.fields.PasswordField
    :param Pole_Submit: Przycisk wysyłający formularz.
    :type Pole_Submit: wtforms.fields.SubmitField
    """

    Pole_Stare_Hasło = PASSWORD_FIELD(
        "Stare Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)]
    )
    Pole_Nowe_Hasło_1 = PASSWORD_FIELD(
        "Nowe Hasło",
        [
            VALIDATORS.DataRequired(),
            VALIDATORS.EqualTo("Pole_Nowe_Hasło_2"),
            VALIDATORS.length(min=8, max=100),
        ],
    )
    Pole_Nowe_Hasło_2 = PASSWORD_FIELD(
        "Powtórz Nowe Hasło",
        [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)],
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
