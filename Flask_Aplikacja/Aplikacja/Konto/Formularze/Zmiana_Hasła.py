"""Formularz zmiany hasła.

Moduł ten definiuje formularz, za pomocą którego zalogowany
użytkownik może zmienić swoje dotychczasowe hasło.
"""

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

    Wymaga podania aktualnego hasła oraz dwukrotnego wprowadzenia nowego.

    :ivar Pole_Stare_Hasło: Pole na bieżące hasło użytkownika.
    :ivar Pole_Nowe_Hasło_1: Pole na nowe hasło.
    :ivar Pole_Nowe_Hasło_2: Pole do powtórzenia nowego hasła.
    :ivar Pole_Submit: Przycisk do zatwierdzenia zmiany.
    """

    Pole_Stare_Hasło = PASSWORD_FIELD(
        "Stare Hasło",
        validators=[
            VALIDATORS.DataRequired(message="Musisz podać swoje obecne hasło."),
            VALIDATORS.Length(
                min=8, max=100, message="Hasło musi mieć minimum 8 znaków."
            ),
        ],
        description="Wprowadź hasło, którego aktualnie używasz.",
    )
    Pole_Nowe_Hasło_1 = PASSWORD_FIELD(
        "Nowe Hasło",
        [
            VALIDATORS.DataRequired(message="Nowe hasło nie może być puste."),
            VALIDATORS.EqualTo(
                "Pole_Nowe_Hasło_2", message="Nowe hasła muszą być identyczne."
            ),
            VALIDATORS.Length(
                min=8, max=100, message="Nowe hasło musi mieć co najmniej 8 znaków."
            ),
        ],
        description="Wprowadź nowe, silne hasło (minimum 8 znaków).",
    )
    Pole_Nowe_Hasło_2 = PASSWORD_FIELD(
        "Powtórz Nowe Hasło",
        [VALIDATORS.DataRequired(message="Musisz powtórzyć nowe hasło.")],
    )
    Pole_Submit = SUBMIT_FIELD("Zmień hasło")
