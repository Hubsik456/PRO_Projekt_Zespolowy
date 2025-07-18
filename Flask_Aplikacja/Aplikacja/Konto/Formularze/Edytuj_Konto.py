"""Moduł formularza edycji konta."""

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

    :param Pole_Login: Pole na nowy login użytkownika.
    :type Pole_Login: wtforms.fields.StringField
    :param Pole_Email: Pole na nowy adres email użytkownika.
    :type Pole_Email: wtforms.fields.EmailField
    :param Pole_Opis: Pole na opcjonalny opis użytkownika.
    :type Pole_Opis: wtforms.fields.TextAreaField
    :param Pole_Submit: Przycisk wysyłający formularz.
    :type Pole_Submit: wtforms.fields.SubmitField
    """

    Pole_Login = STRING_FIELD(
        "Login", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Email = EMAIL_FIELD(
        "E-Mail", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Opis = TEXTAREA_FIELD("Opis")
    Pole_Submit = SUBMIT_FIELD("Wyślij")
