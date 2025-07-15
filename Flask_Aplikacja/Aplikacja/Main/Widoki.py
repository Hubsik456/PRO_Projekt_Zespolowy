"""
    ;dsjlkdfnmglkfd
"""

# Ogólne URL'e

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR, request as REQUEST, Response as RESPONSE, make_response as MAKE_RESPONSE

#! Lokalne Importy
from Aplikacja.Main import Blueprint_1
from Aplikacja.Main.Formularze.Wybór_Języka import Formularz_Wyboru_Języka
from Aplikacja.Main.Formularze.Wybór_Motywu import Formularz_Wyboru_Motywu

#! Main
@Blueprint_1.route("/")
def Widok_Main_Index():
    """
        Strona główna.
    """
    return RENDER_TEMPLATE("Main/index.html")

@Blueprint_1.route("/o-programie/")
def Widok_Main_O_Programie():
    """
        Strona z podstawowymi informacjami o programie.
    """

    return RENDER_TEMPLATE("Main/O_Programie.html")

@Blueprint_1.route("/polityka-prywatnosci/")
def Widok_Main_Polityka_Prywatności():
    """
        Strona z informacjami na temat polityki prywatności.
    """

    return RENDER_TEMPLATE("Main/Polityka_Prywatności.html")

@Blueprint_1.route("/jezyk/", methods=["POST", "GET"])
def Widok_Main_Język():
    """
        Strona z formularzem wyboru języka.
    """

    Formularz = Formularz_Wyboru_Języka()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            FLASH("Zapisano wybór języka.", "success")

            Wybrany_Język = Formularz.Pole_Język.data
            print(f"{Wybrany_Język=}")

            Odpowiedź = MAKE_RESPONSE(REDIRECT(URL_FOR("Blueprint_1.Widok_Main_Index"))) # Trzeba przeładować stronę, bez tego zmiana ciasteczka będzie wymagała ręcznego przeładowania strony
            #Odpowiedź = MAKE_RESPONSE(RENDER_TEMPLATE("Main/index.html"))
            #Odpowiedź = MAKE_RESPONSE(RENDER_TEMPLATE("Main/Język.html", Formularz = Formularz))

            Odpowiedź.set_cookie(key="Jezyk", value=Wybrany_Język, max_age=(30 * 24 * 3600))

            return Odpowiedź

        FLASH("Podano niepoprawne dane", "danger")
        return RENDER_TEMPLATE("Main/Język.html", Formularz = Formularz)

    return RENDER_TEMPLATE("Main/Język.html", Formularz = Formularz)

@Blueprint_1.route("/motyw/", methods=["POST", "GET"])
def Widok_Main_Motyw():
    """
        Strona z formularzem motywu.
    """

    Formularz = Formularz_Wyboru_Motywu()

    if REQUEST.method == "POST":
        if Formularz.validate_on_submit():
            FLASH("Zapisano wybór języka.", "success")

            Wybrany_Motyw = Formularz.Pole_Motyw.data
            print(f"{Wybrany_Motyw=}")

            Odpowiedź = MAKE_RESPONSE(REDIRECT(URL_FOR("Blueprint_1.Widok_Main_Index"))) # Trzeba przeładować stronę, bez tego zmiana ciasteczka będzie wymagała ręcznego przeładowania strony
            #Odpowiedź = MAKE_RESPONSE(RENDER_TEMPLATE("Main/index.html"))
            #Odpowiedź = MAKE_RESPONSE(RENDER_TEMPLATE("Main/Motyw.html", Formularz = Formularz))

            Odpowiedź.set_cookie(key="Motyw", value=Wybrany_Motyw, max_age=(30 * 24 * 3600))

            return Odpowiedź

        FLASH("Podano niepoprawne dane", "danger")
        return RENDER_TEMPLATE("Main/Język.html", Formularz = Formularz)

    return RENDER_TEMPLATE("Main/Motyw.html", Formularz = Formularz)