# URL'e i logika związana z kolekcjami użytkowników

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR, request as REQUEST
from werkzeug.security import check_password_hash as CHECK_PASSWORD_HASH, generate_password_hash as GENERATE_PASSWORD_HASH
from flask_login import login_user as LOGIN_USER, logout_user as LOGOUT_USER, login_required as LOGIN_REQUIRED, fresh_login_required as FRESH_LOGIN_REQUIRED, current_user as CURRENT_USER

#! Lokalne importy
from Aplikacja.Rozszerzenia import DB
from Aplikacja.Modele.Użytkownicy import Użytkownicy
from Aplikacja.Kolekcja import Blueprint_3

#! Main
@Blueprint_3.route("/")
def Widok_Kolekcja_Index():
    """
        Strona główna z kolekcjami użytkowników.
    """

    return RENDER_TEMPLATE("Kolekcja/index.html")
