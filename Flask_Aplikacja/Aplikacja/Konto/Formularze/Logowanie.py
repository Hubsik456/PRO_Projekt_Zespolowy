"""
Formularz logowania.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import PasswordField as PASSWORD_FIELD
from wtforms import StringField as STRING_FIELD
from wtforms import SubmitField as SUBMIT_FIELD
from wtforms import validators as VALIDATORS


#! Main
class Formularz_Logowanie(FLASK_FORM):
    Pole_Login = STRING_FIELD(
        "Login", [VALIDATORS.DataRequired(), VALIDATORS.length(min=5, max=100)]
    )
    Pole_Hasło = PASSWORD_FIELD(
        "Hasło", [VALIDATORS.DataRequired(), VALIDATORS.length(min=8, max=100)]
    )
    Pole_Submit = SUBMIT_FIELD("Wyślij")
