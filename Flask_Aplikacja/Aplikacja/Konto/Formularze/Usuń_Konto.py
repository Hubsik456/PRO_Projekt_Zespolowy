"""Formularz usuwania konta użytkownika.

Moduł definiuje formularz służący do permanentnego
usunięcia konta z aplikacji.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    PasswordField as PASSWORD_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Usuń_Konto(FLASK_FORM):
    """Formularz do trwałego usunięcia konta użytkownika.

    Wymaga podania i potwierdzenia hasła w celu weryfikacji tożsamości.

    :ivar Pole_Hasło_1: Pole na hasło użytkownika.
    :ivar Pole_Hasło_2: Pole do powtórzenia hasła.
    :ivar Pole_Submit: Przycisk inicjujący usunięcie konta.
    """

    Pole_Hasło_1 = PASSWORD_FIELD(
        "Hasło",
        [
            VALIDATORS.DataRequired(
                message="Podanie hasła jest wymagane do usunięcia konta."
            ),
            VALIDATORS.EqualTo(
                "Pole_Hasło_2", message="Podane hasła muszą być identyczne."
            ),
            VALIDATORS.Length(
                min=8, max=100, message="Hasło musi mieć minimum 8 znaków."
            ),
        ],
        description="Aby potwierdzić, wprowadź swoje aktualne hasło.",
    )
    Pole_Hasło_2 = PASSWORD_FIELD(
        "Powtórz Hasło", [VALIDATORS.DataRequired(message="Musisz powtórzyć hasło.")]
    )
    Pole_Submit = SUBMIT_FIELD("Usuń konto na stałe")
