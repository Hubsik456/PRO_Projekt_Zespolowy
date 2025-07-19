"""Moduł formularza z dodawaniem notatki do danego przedmiotu z kolekcji."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
    TextAreaField as TEXTAREA_FIELD,
    BooleanField as BOOLEAN_FIELD,
)


#! Main
class Formularz_Dodanie_Notatki(FLASK_FORM):
    Pole_Treść = TEXTAREA_FIELD("Notatka", validators=[VALIDATORS.DataRequired()])
    Pole_Czy_Prywatne = BOOLEAN_FIELD("Czy Prywatne")
    Pole_Submit = SUBMIT_FIELD("Wyślij")
