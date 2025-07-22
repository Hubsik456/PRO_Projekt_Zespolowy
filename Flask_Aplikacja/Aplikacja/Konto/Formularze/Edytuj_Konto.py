"""Formularz edycji danych konta użytkownika.

Moduł definiuje formularz pozwalający zalogowanemu
użytkownikowi na zmianę danych swojego profilu.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    EmailField as EMAIL_FIELD,
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    TextAreaField as TEXTAREA_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Edytuj_Konto(FLASK_FORM):
    """Formularz do edycji danych konta użytkownika.

    Pozwala na zmianę loginu, adresu email oraz opisu profilu.

    :ivar Pole_Login: Pole na nowy login użytkownika.
    :ivar Pole_Email: Pole na nowy adres email.
    :ivar Pole_Opis: Pole na opcjonalny opis profilu.
    :ivar Pole_Submit: Przycisk do zapisania zmian.
    """

    Pole_Login = STRING_FIELD(
        "Login",
        validators=[
            VALIDATORS.DataRequired(message="Login jest wymagany."),
            VALIDATORS.Length(
                min=5, max=100, message="Login musi mieć od 5 do 100 znaków."
            ),
        ],
        description="Twoja publiczna nazwa w serwisie.",
    )
    Pole_Email = EMAIL_FIELD(
        "E-Mail",
        validators=[
            VALIDATORS.DataRequired(message="Adres e-mail jest wymagany."),
            VALIDATORS.Length(
                min=5, max=100, message="E-mail musi mieć od 5 do 100 znaków."
            ),
        ],
        description="Twój prywatny adres e-mail.",
    )
    Pole_Opis = TEXTAREA_FIELD(
        "Opis",
        validators=[
            VALIDATORS.Length(
                max=1000, message="Opis nie może przekraczać 1000 znaków."
            )
        ],
        description="Opcjonalny, krótki opis o sobie, który będzie widoczny na Twoim profilu.",
    )
    Pole_Submit = SUBMIT_FIELD("Zapisz zmiany")
