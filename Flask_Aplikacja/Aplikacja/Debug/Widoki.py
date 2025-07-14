# URL'e i logika związna z testowaniem aplikacji

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR, abort as ABORT, request as REQUEST, g as G, current_app as CURRENT_APP
from werkzeug.security import check_password_hash as CHECK_PASSWORD_HASH, generate_password_hash as GENERATE_PASSWORD_HASH
from flask_login import login_user as LOGIN_USER, logout_user as LOGOUT_USER, login_required as LOGIN_REQUIRED, fresh_login_required as FRESH_LOGIN_REQUIRED, current_user as CURRENT_USER

#! Lokalne Importy
from Aplikacja.Baza_Danych import DB
from Aplikacja.Modele.Użytkownicy import Użytkownicy
from Aplikacja.Debug import Blueprint_0

#! Main
#? Widoki
@Blueprint_0.route("/")
def Widok_Debug_Index():
    return RENDER_TEMPLATE("Debug/index.html", Nagłówek = "Index")

@Blueprint_0.route("/sciezki/")
def Widok_Debug_Reguły():
    Reguły = []

    for Reguła in CURRENT_APP.url_map.iter_rules():
        if Reguła.endpoint != "static":
            if Reguła.arguments != set():
                Argumenty = Reguła.arguments
            else:
                Argumenty = ""

            Reguły.append((Reguła.rule, Reguła.endpoint, Argumenty))

    return RENDER_TEMPLATE("Debug/index.html", Nagłówek = "Ścieżki", Reguły = Reguły)

@Blueprint_0.route("/flash/")
def Widok_Debug_Flash():
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

    return RENDER_TEMPLATE("Debug/index.html", Nagłówek = "Flash")

@Blueprint_0.route("/formularz/")
def Widok_Test_1():
    return RENDER_TEMPLATE("Debug/index.html", Nagłówek = "Formularz")

#? Generowanie Błędów
@Blueprint_0.route("/blad/<int:ID>")
def Widok_Debug_Generowanie_Błędu(ID):
    if ID not in [400, 401, 402, 403, 404, 405, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 421, 422, 423, 424, 425, 426, 428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511]:
        FLASH("Podano zły kod błedu HTTP do wygenerowania.\nWygenerowano błąd #500.", "danger")
        return ABORT(500)

    FLASH(f"Wygenerowano Błąd #{ID}.")
    return ABORT(ID)
