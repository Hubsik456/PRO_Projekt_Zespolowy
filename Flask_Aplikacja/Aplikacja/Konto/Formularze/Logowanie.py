"""Formularz logowania użytkownika.

Moduł ten definiuje formularz używany przez użytkowników
do zalogowania się na swoje konto w aplikacji.
"""

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
    """Formularz logowania do aplikacji.

    Zbiera od użytkownika login i hasło w celu autoryzacji.

    :ivar Pole_Login: Pole do wprowadzenia loginu użytkownika.
    :ivar Pole_Hasło: Pole do wprowadzenia hasła.
    :ivar Pole_Submit: Przycisk do zatwierdzenia formularza.
    """

    Pole_Login = STRING_FIELD(
        "Login",
        validators=[
            VALIDATORS.DataRequired(message="Pole z loginem nie może być puste."),
            VALIDATORS.Length(
                min=5, max=100, message="Login musi mieć od 5 do 100 znaków."
            ),
        ],
        description="Wprowadź swój login użyty podczas rejestracji.",
    )
    Pole_Hasło = PASSWORD_FIELD(
        "Hasło",
        validators=[
            VALIDATORS.DataRequired(message="Pole z hasłem nie może być puste."),
            VALIDATORS.Length(
                min=8, max=100, message="Hasło musi mieć minimum 8 znaków."
            ),
        ],
        description="Wprowadź swoje hasło.",
    )
    Pole_Submit = SUBMIT_FIELD("Zaloguj się")
