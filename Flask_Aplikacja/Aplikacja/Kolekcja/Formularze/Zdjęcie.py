#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    StringField as STRING_FIELD,
    TextAreaField as TEXTAREA_FIELD,
    FileField as FILE_FIELD, # Nowe pole do przesyłania plików
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)
from flask_wtf.file import FileRequired, FileAllowed # Walidatory dla plików

#! Main
class Formularz_Zdjecie(FLASK_FORM):
    tytul = STRING_FIELD(
        "Tytuł Zdjęcia",
        validators=[
            VALIDATORS.DataRequired(message="Tytuł zdjęcia jest wymagany."),
            VALIDATORS.Length(min=3, max=100, message="Tytuł zdjęcia musi zawierać od 3 do 100 znaków.")
        ],
        description="Wprowadź krótki tytuł dla zdjęcia."
    )
    opis = TEXTAREA_FIELD(
        "Opis Zdjęcia",
        description="Opcjonalny opis, co przedstawia zdjęcie."
    )
    zdjecie_plik = FILE_FIELD(
        "Plik Zdjęcia",
        validators=[
            FileAllowed(['jpg', 'png', 'jpeg'], 'Tylko pliki graficzne (JPG, PNG, GIF) są dozwolone!'),
            FileRequired(message="Wybierz plik zdjęcia.") # W widoku edycji, nie będzie required
        ],
        description="Wybierz plik graficzny do przesłania."
    )
    Pole_Submit = SUBMIT_FIELD("Zapisz Zdjęcie")