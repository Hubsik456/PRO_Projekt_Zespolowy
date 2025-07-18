# Formularz usuwania konta

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import PasswordField as PASSWORD_FIELD
from wtforms import SubmitField as SUBMIT_FIELD
from wtforms import validators as VALIDATORS


#! Main
class Formularz_Usuń_Konto(FLASK_FORM):
    Pole_Hasło_1 = PASSWORD_FIELD(
        "Hasło Hasło",
        [
            VALIDATORS.DataRequired(),
            VALIDATORS.EqualTo("Pole_Hasło_2"),
            VALIDATORS.length(min=8, max=100),
        ],
    )
    Pole_Hasło_2 = PASSWORD_FIELD(
        "Powtórz Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)]
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
