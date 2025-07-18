"""Widoki (routes) dla Blueprintu #0 - Debug.

Moduł zawiera widoki i logikę przydatną podczas tworzenia
i testowania aplikacji.
"""

#! Zewnętrzne Importy
from flask import (
    abort as ABORT,
    current_app as CURRENT_APP,
    flash as FLASH,
    render_template as RENDER_TEMPLATE,
)

#! Lokalne Importy
from Aplikacja.Debug import Blueprint_0


#! Main
@Blueprint_0.route("/")
def Widok_Debug_Index():
    """Renderuje stronę główną panelu debugowania.

    :return: Wyrenderowany szablon HTML strony głównej panelu debugowania.
    :rtype: str
    """
    return RENDER_TEMPLATE("Debug/index.html", Nagłówek="Index")


@Blueprint_0.route("/sciezki/")
def Widok_Debug_Ścieżki():
    """Wyświetla listę wszystkich dostępnych ścieżek URL w aplikacji.

    Iteruje po `current_app.url_map`, aby zebrać informacje o wszystkich
    zdefiniowanych regułach routingu.

    :return: Wyrenderowany szablon HTML z tabelą zawierającą ścieżki.
    :rtype: str
    """
    Reguły = []

    for Reguła in CURRENT_APP.url_map.iter_rules():
        if Reguła.endpoint != "static":
            if Reguła.arguments != set():
                Argumenty = Reguła.arguments
            else:
                Argumenty = ""

            Reguły.append((Reguła.rule, Reguła.endpoint, Argumenty))

    return RENDER_TEMPLATE("Debug/Ścieżki.html", Reguły=Reguły)


@Blueprint_0.route("/flash/")
def Widok_Debug_Flash():
    """Testuje wyświetlanie komunikatów flash.

    Generuje komunikaty flash dla wszystkich dostępnych kategorii Bootstrapa.

    :return: Wyrenderowany szablon HTML.
    :rtype: str
    """
    FLASH("<h1 class='text-primary'>WIP| Lorem Ipsum</h1>", "primary")
    FLASH("WIP| Primary: Lorem Ipsum", "primary")
    FLASH("WIP| Secondary:  Lorem Ipsum", "secondary")
    FLASH("WIP| Success: Lorem Ipsum", "success")
    FLASH("WIP| Danger: Lorem Ipsum", "danger")
    FLASH("WIP| Warning: Lorem Ipsum", "warning")
    FLASH("WIP| Info: Lorem Ipsum", "info")
    FLASH("WIP| Light: Lorem Ipsum", "light")
    FLASH("WIP| Dark: Lorem Ipsum", "dark")
    FLASH("WIP| Null: Lorem Ipsum")

    return RENDER_TEMPLATE("Debug/index.html")


@Blueprint_0.route("/formularz/")  # TODO:
def Widok_Test_1():
    """Widok testowy dla formularzy.

    :return: Wyrenderowany szablon HTML.
    :rtype: str
    """
    return RENDER_TEMPLATE("Debug/index.html")


@Blueprint_0.route("/blad/<int:ID>")
def Widok_Debug_Generowanie_Błędu(ID):
    """Celowo generuje błąd HTTP o podanym kodzie.

    Funkcja służy do testowania stron błędów.

    :param int ID: Kod błędu HTTP do wygenerowania.
    :raises werkzeug.exceptions.HTTPException: Przerywa żądanie z podanym kodem błędu.
    """
    if ID not in [
        400,
        401,
        402,
        403,
        404,
        405,
        407,
        408,
        409,
        410,
        411,
        412,
        413,
        414,
        415,
        416,
        417,
        418,
        421,
        422,
        423,
        424,
        425,
        426,
        428,
        429,
        431,
        451,
        500,
        501,
        502,
        503,
        504,
        505,
        506,
        507,
        508,
        510,
        511,
    ]:
        FLASH(
            "Podano zły kod błedu HTTP do wygenerowania.\nWygenerowano błąd #500.",
            "danger",
        )
        return ABORT(500)

    FLASH(f"Wygenerowano celowo błąd #{ID}.", "warning")
    return ABORT(ID)
