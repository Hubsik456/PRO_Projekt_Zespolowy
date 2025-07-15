# Formularz zmiany hasła

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import validators as VALIDATORS, SubmitField as SUBMIT_FIELD, PasswordField as PASSWORD_FIELD

#! Main
class Formularz_Zmiana_Hasła(FLASK_FORM):
    Pole_Stare_Hasło = PASSWORD_FIELD("Stare Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)])
    Pole_Nowe_Hasło_1 = PASSWORD_FIELD("Nowe Hasło", [VALIDATORS.DataRequired(), VALIDATORS.EqualTo("Pole_Nowe_Hasło_2"), VALIDATORS.length(min=8, max=100)])
    Pole_Nowe_Hasło_2 = PASSWORD_FIELD("Powtórz Nowe Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)])
    Pole_Submit = SUBMIT_FIELD("Wyślij")