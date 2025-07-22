"""Formularz dodawania i edycji notatki do przedmiotu.

Moduł ten definiuje strukturę formularza używanego do tworzenia
i modyfikowania notatek w kolekcji.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    BooleanField as BOOLEAN_FIELD,
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    TextAreaField as TEXTAREA_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Notatka(FLASK_FORM):
    """
    Formularz do tworzenia i edycji notatek powiązanych z przedmiotem w kolekcji.

    Definiuje pola formularza, ich walidatory oraz opisy, które są wyświetlane użytkownikowi.
    """

    tytul = STRING_FIELD(
        "Tytuł Notatki",
        validators=[
            VALIDATORS.DataRequired(message="Tytuł notatki jest wymagany."),
            VALIDATORS.length(
                min=3,
                max=100,
                message="Tytuł notatki musi zawierać od 3 do 100 znaków.",
            ),
        ],
        description="Wprowadź krótki, ale treściwy tytuł dla swojej notatki.",
    )
    opis = TEXTAREA_FIELD(
        "Treść Notatki",
        validators=[
            VALIDATORS.DataRequired(message="Treść notatki jest wymagana."),
            VALIDATORS.Length(
                max=5000, message="Treść notatki nie może przekraczać 5000 znaków."
            ),
        ],
        description="Tutaj możesz wpisać szczegółową treść swojej notatki.",
    )
    czy_prywatne = BOOLEAN_FIELD(
        "Notatka Prywatna",
        description="Zaznacz, jeśli chcesz, aby ta notatka była widoczna tylko dla Ciebie.",
    )
    Pole_Submit = SUBMIT_FIELD("Zapisz Notatkę")
