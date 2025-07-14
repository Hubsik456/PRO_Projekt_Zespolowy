# Formularz rejestracji

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import validators as VALIDATORS, SubmitField as SUBMIT_FIELD,  StringField as STRING_FIELD, PasswordField as PASSWORD_FIELD, EmailField as EMAIL_FIELD

#! Main
class Formularz_Rejestracja(FLASK_FORM):
    Pole_Login = STRING_FIELD("Login:", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)])
    Pole_Hasło_1 = PASSWORD_FIELD("Hasło:", [VALIDATORS.DataRequired(), VALIDATORS.EqualTo("Pole_Hasło_2"), VALIDATORS.length(min=8, max=100)])
    Pole_Hasło_2 = PASSWORD_FIELD("Powtórz Hasło:", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)])
    Pole_Email = EMAIL_FIELD("E-Mail:", [VALIDATORS.Optional(), VALIDATORS.length(min=5, max=100)])
    Pole_Submit = SUBMIT_FIELD("Wyślij")