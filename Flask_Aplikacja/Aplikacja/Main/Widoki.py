"""Główne widoki (routes) dla Blueprintu #1 - Main.

Ten moduł zawiera logikę i definicje URL dla głównych,
ogólnodostępnych stron aplikacji, takich jak:
- Strona główna
- O programie
- Polityka prywatności
- Ustawienia języka i motywu
"""

#! Zewnętrzne Importy
from flask import (
    flash as FLASH,
    make_response as MAKE_RESPONSE,
    redirect as REDIRECT,
    render_template as RENDER_TEMPLATE,
    request as REQUEST,
    url_for as URL_FOR,
)

#! Lokalne Importy
from Aplikacja.Main import Blueprint_1
from Aplikacja.Main.Formularze.Wybór_Języka import Formularz_Wyboru_Języka
from Aplikacja.Main.Formularze.Wybór_Motywu import Formularz_Wyboru_Motywu


#! Main
@Blueprint_1.route("/")
def Widok_Main_Index():
    """Renderuje stronę główną aplikacji.

    :return: Wyrenderowany szablon HTML strony głównej.
    :rtype: str
    """
    return RENDER_TEMPLATE("Main/index.html")


@Blueprint_1.route("/o-programie/")
def Widok_Main_O_Programie():
    """Renderuje stronę z informacjami o programie.

    :return: Wyrenderowany szablon HTML strony "O programie".
    :rtype: str
    """
    return RENDER_TEMPLATE("Main/O_Programie.html")


@Blueprint_1.route("/polityka-prywatnosci/")
def Widok_Main_Polityka_Prywatności():
    """Renderuje stronę z polityką prywatności.

    :return: Wyrenderowany szablon HTML strony "Polityka Prywatności".
    :rtype: str
    """
    return RENDER_TEMPLATE("Main/Polityka_Prywatności.html")


@Blueprint_1.route("/jezyk/", methods=["POST", "GET"])
def Widok_Main_Język():
    """Renderuje stronę wyboru języka i obsługuje zmianę.

    Przy żądaniu GET wyświetla formularz.
    Przy żądaniu POST waliduje formularz, zapisuje wybrany
    język w ciasteczku i przekierowuje na stronę główną.

    :return: Wyrenderowany szablon HTML lub odpowiedź przekierowująca.
    :rtype: str or werkzeug.wrappers.response.Response
    """
    Formularz = Formularz_Wyboru_Języka()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            FLASH("Zapisano wybór języka.", "success")

            Wybrany_Język = Formularz.Pole_Język.data
            Odpowiedź = MAKE_RESPONSE(REDIRECT(URL_FOR("Blueprint_1.Widok_Main_Index")))
            Odpowiedź.set_cookie(
                key="Jezyk", value=Wybrany_Język, max_age=(30 * 24 * 3600)
            )

            return Odpowiedź

        FLASH("Podano niepoprawne dane", "danger")

    return RENDER_TEMPLATE("Main/Język.html", Formularz=Formularz)


@Blueprint_1.route("/motyw/", methods=["POST", "GET"])
def Widok_Main_Motyw():
    """Renderuje stronę wyboru motywu i obsługuje zmianę.

    Przy żądaniu GET wyświetla formularz.
    Przy żądaniu POST waliduje formularz, zapisuje wybrany
    motyw w ciasteczku i przekierowuje na stronę główną.

    :return: Wyrenderowany szablon HTML lub odpowiedź przekierowująca.
    :rtype: str or werkzeug.wrappers.response.Response
    """
    Formularz = Formularz_Wyboru_Motywu()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            FLASH("Zapisano wybór motywu.", "success")

            Wybrany_Motyw = Formularz.Pole_Motyw.data
            Odpowiedź = MAKE_RESPONSE(REDIRECT(URL_FOR("Blueprint_1.Widok_Main_Index")))
            Odpowiedź.set_cookie(
                key="Motyw", value=Wybrany_Motyw, max_age=(30 * 24 * 3600)
            )

            return Odpowiedź

        FLASH("Podano niepoprawne dane", "danger")

    return RENDER_TEMPLATE("Main/Motyw.html", Formularz=Formularz)
