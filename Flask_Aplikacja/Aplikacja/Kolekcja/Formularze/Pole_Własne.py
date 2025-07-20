"""Moduł formularza z dodawaniem pola własnego do przedmiotu z kolekcji."""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    StringField as STRING_FIELD,
    SelectField as SELECT_FIELD,
    validators as VALIDATORS
)

#! Main
class Formularz_Pole_Własne(FLASK_FORM):
    class Meta:
        csrf = False

    id_rodzaj = SELECT_FIELD(
        "Rodzaj",
        coerce=int,
        validators=[VALIDATORS.DataRequired()]
    )
    wartosc = STRING_FIELD("Wartość", validators=[VALIDATORS.DataRequired()])
