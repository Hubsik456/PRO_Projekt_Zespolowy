"""Moduł formularza z dodawaniem przedmiotu do kolekcji."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
    TextAreaField as TEXTAREA_FIELD,
    BooleanField as BOOLEAN_FIELD,
    SelectField as SELECT_FIELD,
    DecimalField as DECIMAL_FIELD,
    FieldList as FIELD_LIST,
    FormField as FORM_FIELD,
)

#! Lokalne Importy
from Aplikacja.Kolekcja.Formularze.Pole_Własne import Formularz_Pole_Własne


#! Main
class Formularz_Dodanie_Przedmiotu(FLASK_FORM):
    Pole_Nazwa = STRING_FIELD("Nazwa", validators=[VALIDATORS.DataRequired(), VALIDATORS.length(min=3, max=100)])
    Pole_Opis = TEXTAREA_FIELD("Opis")
    Pole_Cena_Zakupu = DECIMAL_FIELD("Cena Zakupu", validators=[VALIDATORS.DataRequired(), VALIDATORS.NumberRange(min=0.01)], places=2)
    Pole_Wartość_Rynkowa = DECIMAL_FIELD("Wartość Rynkowa", validators=[VALIDATORS.DataRequired(), VALIDATORS.NumberRange(min=0.01)], places=2)
    Pole_Kategoria = SELECT_FIELD("Kategoria", choices=[("1", "Opcja #1"), ("2", "Opcja #2"), ("3", "Opcja #3")], validators=[VALIDATORS.DataRequired()])
    Pole_Czy_Prywatne = BOOLEAN_FIELD("Czy Prywatne")

    Pola_Własne = FIELD_LIST(FORM_FIELD(Formularz_Pole_Własne), min_entries=3)

    Pole_Submit = SUBMIT_FIELD("Wyślij")
