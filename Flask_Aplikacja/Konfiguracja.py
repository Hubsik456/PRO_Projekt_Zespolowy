# Plik z konfiguracja

#! Zewnętrzne Importy
import os as OS
from dotenv import load_dotenv as LOAD_DOTENV

#! Main
LOAD_DOTENV()

Ścieżka_Root = OS.path.abspath(OS.path.dirname(__file__))

class Konfiguracja():
    SECRET_KEY = OS.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = OS.environ.get('DATABASE_URI') or 'sqlite:///' + OS.path.join(Ścieżka_Root, 'Baza_Danych.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = OS.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")

    LANGUAGES = ["pl", "en"]
    BABEL_DEFAULT_LOCALE = "pl"

    BABEL_TRANSLATION_DIRECTORIES = "D:\\Python - Flask\\PRO_Projekt_Zespołowy_v2\\translations"
    #BABEL_TRANSLATION_DIRECTORIES = OS.path.join(OS.path.abspath(OS.path.dirname(__file__)), "Aplikacja/Tłumaczenia/en")