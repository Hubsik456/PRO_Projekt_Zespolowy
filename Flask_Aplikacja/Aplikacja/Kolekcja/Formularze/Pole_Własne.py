"""Formularz dla niestandardowych (własnych) pól przedmiotu.

Moduł zawiera definicję formularza, który pozwala użytkownikom
dodawać własne, zdefiniowane przez siebie pola do przedmiotów.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    SelectField as SELECT_FIELD,
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Pole_Własne(FLASK_FORM):
    """
    Formularz do definiowania niestandardowych pól dla przedmiotów w kolekcji.

    Umożliwia użytkownikowi wybór rodzaju pola oraz podanie jego wartości.
    """

    class Meta:
        """
        Klasa Meta konfigurująca zachowanie formularza.

        Wyłącza ochronę CSRF dla tego formularza, co jest przydatne,
        gdy jest on używany jako podformularz w innych, dynamicznie generowanych formularzach.
        """

        csrf = False

    id_rodzaj = SELECT_FIELD(
        "Rodzaj Pola",
        coerce=int,
        validators=[VALIDATORS.DataRequired(message="Musisz wybrać rodzaj pola.")],
        description="Wybierz z listy typ informacji, którą chcesz dodać (np. 'Numer seryjny').",
    )
    wartosc = STRING_FIELD(
        "Wartość",
        validators=[
            VALIDATORS.DataRequired(message="Wartość pola jest wymagana."),
            VALIDATORS.Length(
                min=1, max=1000, message="Wartość musi zawierać od 1 do 1000 znaków."
            ),
        ],
        description="Wpisz konkretną wartość dla wybranego rodzaju pola (np. 'ABC-12345').",
    )
    Pole_Submit = SUBMIT_FIELD("Zapisz Pole")
