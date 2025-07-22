"""Formularz dodawania nowego przedmiotu do kolekcji.

Główny formularz aplikacji, który zbiera wszystkie niezbędne
dane do stworzenia nowego obiektu w kolekcji użytkownika.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    BooleanField as BOOLEAN_FIELD,
    DecimalField as DECIMAL_FIELD,
    SelectField as SELECT_FIELD,
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    TextAreaField as TEXTAREA_FIELD,
    validators as VALIDATORS,
)

#! Lokalne Importy


#! Main
class Formularz_Dodanie_Przedmiotu(FLASK_FORM):
    """
    Formularz służący do dodawania nowego przedmiotu do kolekcji użytkownika.

    Zawiera wszystkie podstawowe pola opisujące przedmiot, takie jak nazwa, opis,
    cena, kategoria oraz pola dynamiczne (własne).
    """

    nazwa = STRING_FIELD(
        "Nazwa",
        validators=[
            VALIDATORS.DataRequired(message="Nazwa przedmiotu jest wymagana."),
            VALIDATORS.Length(
                min=3, max=100, message="Nazwa musi zawierać od 3 do 100 znaków."
            ),
        ],
        description="Wprowadź oficjalną lub własną nazwę przedmiotu.",
    )
    opis = TEXTAREA_FIELD(
        "Opis",
        validators=[
            VALIDATORS.Length(
                max=5000, message="Opis nie może przekraczać 5000 znaków."
            )
        ],
        description="Opcjonalny opis przedmiotu, jego historii, cech itp.",
    )
    cena_zakupu = DECIMAL_FIELD(
        "Cena Zakupu",
        validators=[
            VALIDATORS.DataRequired(message="Cena zakupu jest wymagana."),
            VALIDATORS.NumberRange(min=0, message="Cena nie może być ujemna."),
        ],
        places=2,
        description="Kwota, za którą nabyłeś przedmiot.",
    )
    id_cena_zakupu_waluta = SELECT_FIELD(
        "Waluta Zakupu", validators=[VALIDATORS.DataRequired()], coerce=int
    )
    wartosc_rynkowa = DECIMAL_FIELD(
        "Wartość Rynkowa",
        validators=[
            VALIDATORS.DataRequired(message="Wartość rynkowa jest wymagana."),
            VALIDATORS.NumberRange(min=0, message="Wartość nie może być ujemna."),
        ],
        places=2,
        description="Szacunkowa obecna wartość przedmiotu na rynku.",
    )
    id_wartosc_rynkowa_waluta = SELECT_FIELD(
        "Waluta Rynkowa", validators=[VALIDATORS.DataRequired()], coerce=int
    )
    id_kategoria = SELECT_FIELD(
        "Kategoria",
        validators=[VALIDATORS.DataRequired(message="Wybór kategorii jest wymagany.")],
        coerce=int,
    )
    czy_prywatne = BOOLEAN_FIELD(
        "Przedmiot Prywatny",
        description="Zaznacz, jeśli przedmiot ma być widoczny tylko dla Ciebie.",
    )
    Pole_Submit = SUBMIT_FIELD("Zapisz Przedmiot")
