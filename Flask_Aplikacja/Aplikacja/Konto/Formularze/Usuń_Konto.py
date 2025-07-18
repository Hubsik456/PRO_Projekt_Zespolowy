"""Moduł formularza usuwania konta."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    PasswordField as PASSWORD_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Usuń_Konto(FLASK_FORM):
    """Formularz do usuwania konta użytkownika.

    Wymaga podania i potwierdzenia hasła w celu weryfikacji.

    :param Pole_Hasło_1: Pole na hasło użytkownika.
    :type Pole_Hasło_1: wtforms.fields.PasswordField
    :param Pole_Hasło_2: Pole do powtórzenia hasła.
    :type Pole_Hasło_2: wtforms.fields.PasswordField
    :param Pole_Submit: Przycisk wysyłający formularz.
    :type Pole_Submit: wtforms.fields.SubmitField
    """

    Pole_Hasło_1 = PASSWORD_FIELD(
        "Hasło Hasło",
        [
            VALIDATORS.DataRequired(),
            VALIDATORS.EqualTo("Pole_Hasło_2"),
            VALIDATORS.length(min=8, max=100),
        ],
    )
    Pole_Hasło_2 = PASSWORD_FIELD(
        "Powtórz Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)]
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
