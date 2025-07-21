"""Moduł formularza z dodawaniem notatki do danego przedmiotu z kolekcji."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
    TextAreaField as TEXTAREA_FIELD,
    BooleanField as BOOLEAN_FIELD,
)


#! Main
class Formularz_Notatka(FLASK_FORM):
    tytul = STRING_FIELD(
        "Tytuł Notatki",
        validators=[
            VALIDATORS.DataRequired(message="Tytuł notatki jest wymagany."),
            VALIDATORS.length(min=3, max=100, message="Tytuł notatki musi zawierać od 3 do 100 znaków.")
        ],
        description="Wprowadź krótki, ale treściwy tytuł dla swojej notatki."
    )
    opis = TEXTAREA_FIELD(
        "Treść Notatki",
        validators=[
            VALIDATORS.DataRequired(message="Treść notatki jest wymagana.")
        ],
        description="Tutaj możesz wpisać szczegółową treść swojej notatki."
    )
    czy_prywatne = BOOLEAN_FIELD(
        "Czy Prywatna",
        description="Zaznacz, jeśli chcesz, aby ta notatka była widoczna tylko dla Ciebie."
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")