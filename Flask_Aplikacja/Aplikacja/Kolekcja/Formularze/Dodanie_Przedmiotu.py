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
    nazwa = STRING_FIELD("Nazwa", validators=[VALIDATORS.DataRequired(), VALIDATORS.length(min=3, max=100)])
    opis = TEXTAREA_FIELD("Opis")
    cena_zakupu = DECIMAL_FIELD("Cena Zakupu", validators=[VALIDATORS.DataRequired(), VALIDATORS.NumberRange(min=0)], places=2)
    id_cena_zakupu_waluta = SELECT_FIELD("Waluta Zakupu", validators=[VALIDATORS.DataRequired()], coerce=int)
    wartosc_rynkowa = DECIMAL_FIELD("Wartość Rynkowa", validators=[VALIDATORS.DataRequired(), VALIDATORS.NumberRange(min=0)], places=2)
    id_wartosc_rynkowa_waluta = SELECT_FIELD("Waluta Rynkowa", validators=[VALIDATORS.DataRequired()], coerce=int)
    id_kategoria = SELECT_FIELD("Kategoria", validators=[VALIDATORS.DataRequired()], coerce=int)
    czy_prywatne = BOOLEAN_FIELD("Czy Prywatne")
    Pola_Własne = FIELD_LIST(FORM_FIELD(Formularz_Pole_Własne), min_entries=1) # 0
    Pole_Submit = SUBMIT_FIELD("Wyślij")