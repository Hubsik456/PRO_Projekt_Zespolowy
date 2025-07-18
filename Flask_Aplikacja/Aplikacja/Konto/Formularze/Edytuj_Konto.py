"""
Formularz edycji konta.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import EmailField as EMAIL_FIELD
from wtforms import StringField as STRING_FIELD
from wtforms import SubmitField as SUBMIT_FIELD
from wtforms import TextAreaField as TEXTAREA_FIELD
from wtforms import validators as VALIDATORS


#! Main
class Formularz_Edytuj_Konto(FLASK_FORM):
    """
    Klasa reprezentująca formularz Flask-WTF do edycji własnego konta przez użytkownika. Posiada następujące pola:

    :ivar Pole_Login: Pole tekstowe do wprowadzenia loginu. Wymagane, długość od 5 do 100 znaków.
    :vartype Pole_Login: wtforms.fields.StringField
    :ivar Pole_Email: Pole e-mail do wprowadzenia adresu e-mail. Wymagane, długość od 5 do 100 znaków.
    :vartype Pole_Email: wtforms.fields.EmailField
    :ivar Pole_Opis: Pole tekstowe (obszar) na opcjonalny opis użytkownika.
    :vartype Pole_Opis: wtforms.fields.TextAreaField
    :ivar Pole_Submit: Przycisk do wysłania formularza.
    :vartype Pole_Submit: wtforms.fields.SubmitFieldt
    """

    Pole_Login = STRING_FIELD(
        "Login", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Email = EMAIL_FIELD(
        "E-Mail", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Opis = TEXTAREA_FIELD("Opis")
    Pole_Submit = SUBMIT_FIELD("Wyślij")
