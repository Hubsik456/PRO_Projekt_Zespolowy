"""Formularz do przesyłania zdjęć dla przedmiotów w kolekcji.

Moduł definiuje pola do przesyłania plików graficznych wraz z ich
tytułem i opisem.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import (
    FileField as FILE_FIELD,
    StringField as STRING_FIELD,
    SubmitField as SUBMIT_FIELD,
    TextAreaField as TEXTAREA_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Zdjecie(FLASK_FORM):
    """
    Formularz do przesyłania i opisywania zdjęć przedmiotów w kolekcji.

    Zawiera pola na tytuł, opcjonalny opis oraz pole do wyboru pliku graficznego.
    """

    tytul = STRING_FIELD(
        "Tytuł Zdjęcia",
        validators=[
            VALIDATORS.DataRequired(message="Tytuł zdjęcia jest wymagany."),
            VALIDATORS.Length(
                min=3,
                max=100,
                message="Tytuł zdjęcia musi zawierać od 3 do 100 znaków.",
            ),
        ],
        description="Wprowadź krótki tytuł dla zdjęcia (np. 'Przód monety').",
    )
    opis = TEXTAREA_FIELD(
        "Opis Zdjęcia",
        validators=[
            VALIDATORS.Length(
                max=5000, message="Opis nie może przekraczać 5000 znaków."
            )
        ],
        description="Opcjonalny opis, co przedstawia zdjęcie lub na co zwrócić uwagę.",
    )
    zdjecie_plik = FILE_FIELD(
        "Plik Zdjęcia",
        validators=[
            FileAllowed(
                ["jpg", "png", "jpeg"],
                "Dozwolone są tylko pliki graficzne (jpg, png, jpeg)!",
            ),
            FileRequired(message="Musisz wybrać plik zdjęcia do przesłania."),
        ],
        description="Wybierz plik graficzny z dysku.",
    )
    Pole_Submit = SUBMIT_FIELD("Zapisz Zdjęcie")
