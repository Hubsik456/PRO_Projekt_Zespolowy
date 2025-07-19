"""Moduł formularza z dodawaniem pola własnego do przedmiotu z kolekcji."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    StringField as STRING_FIELD,
    validators as VALIDATORS,
    SelectField as SELECT_FIELD,
)


#! Main
class Formularz_Pole_Własne(FLASK_FORM):
    class Meta:
        csrf = False

    Pole_Rodzaj = SELECT_FIELD("Rodzaj", choices=[("a", "Opcja #A"), ("b", "Opcja #B"), ("c", "Opcja #C")])
    Pole_Treść = STRING_FIELD("Wartość")
