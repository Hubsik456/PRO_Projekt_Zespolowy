"""Formularz rejestracji nowego użytkownika.

Moduł ten definiuje formularz umożliwiający nowym użytkownikom
założenie konta w aplikacji.
"""

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
    """Formularz rejestracji nowego konta.

    Wymaga podania unikalnego loginu, hasła (wraz z potwierdzeniem)
    oraz opcjonalnie adresu e-mail.

    :ivar Pole_Login: Pole na login użytkownika.
    :ivar Pole_Hasło_1: Pole na hasło.
    :ivar Pole_Hasło_2: Pole do powtórzenia hasła.
    :ivar Pole_Email: Opcjonalne pole na adres email.
    :ivar Pole_Submit: Przycisk do zatwierdzenia formularza.
    """

    Pole_Login = STRING_FIELD(
        "Login",
        validators=[
            VALIDATORS.DataRequired(message="Login jest wymagany."),
            VALIDATORS.Length(
                min=5, max=100, message="Login musi mieć od 5 do 100 znaków."
            ),
        ],
        description="Twoja unikalna nazwa w serwisie. Będzie widoczna dla innych.",
    )
    Pole_Hasło_1 = PASSWORD_FIELD(
        "Hasło",
        [
            VALIDATORS.DataRequired(message="Hasło jest wymagane."),
            VALIDATORS.EqualTo(
                "Pole_Hasło_2", message="Podane hasła muszą być identyczne."
            ),
            VALIDATORS.Length(
                min=8, max=100, message="Hasło musi mieć co najmniej 8 znaków."
            ),
        ],
        description="Wybierz silne hasło składające się z co najmniej 8 znaków.",
    )
    Pole_Hasło_2 = PASSWORD_FIELD(
        "Powtórz Hasło",
        validators=[VALIDATORS.DataRequired(message="Musisz powtórzyć hasło.")],
    )
    Pole_Email = EMAIL_FIELD(
        "E-Mail",
        validators=[
            VALIDATORS.Optional(),
            VALIDATORS.Length(
                max=100, message="E-mail nie może być dłuższy niż 100 znaków."
            ),
        ],
        description="Opcjonalny adres e-mail. Nie będzie nigdzie publikowany.",
    )
    Pole_Submit = SUBMIT_FIELD("Zarejestruj się")
