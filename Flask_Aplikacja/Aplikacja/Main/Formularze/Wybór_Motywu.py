"""Formularz wyboru motywu wizualnego aplikacji.

Moduł ten definiuje formularz, który pozwala użytkownikowi
na zmianę motywu kolorystycznego interfejsu.
"""

#! Zewnętrzne Importy
from flask_wtf import FlaskForm as FLASK_FORM
from wtforms import (
    SelectField as SELECT_FIELD,
    SubmitField as SUBMIT_FIELD,
    validators as VALIDATORS,
)


#! Main
class Formularz_Wyboru_Motywu(FLASK_FORM):
    """Formularz do wyboru motywu kolorystycznego aplikacji.

    Umożliwia użytkownikowi wybór jednego z predefiniowanych
    motywów wizualnych. Wybór jest zapisywany w ciasteczku.

    :ivar Pole_Motyw: Pole wyboru (lista rozwijana) z dostępnymi motywami.
    :ivar Pole_Submit: Przycisk do zatwierdzenia wyboru.
    """

    Pole_Motyw = SELECT_FIELD(
        "Wybierz Motyw",
        choices=[
            ("brite", "Brite"),
            ("pulse", "Pulse"),
            ("united", "United"),
            ("zephyr", "Zephyr"),
            ("sketchy", "Sketchy"),
        ],
        validators=[VALIDATORS.DataRequired(message="Musisz wybrać jeden z motywów.")],
        description="Zmiana motywu odświeży wygląd całej aplikacji.",
    )
    Pole_Submit = SUBMIT_FIELD("Zmień Motyw")
