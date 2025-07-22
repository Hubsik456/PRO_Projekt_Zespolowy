"""Główny plik konfiguracyjny aplikacji.

Ten moduł ładuje zmienne środowiskowe z pliku .env i definiuje
klasę konfiguracyjną `Konfiguracja`, która przechowuje wszystkie
ustawienia aplikacji Flask.
"""

#! Zewnętrzne Importy
import os as OS

from dotenv import load_dotenv as LOAD_DOTENV

#! Main
LOAD_DOTENV()

Ścieżka_Root = OS.path.abspath(OS.path.dirname(__file__))


class Konfiguracja:
    """Klasa przechowująca konfigurację aplikacji Flask.

    Zmienne są wczytywane ze zmiennych środowiskowych (plik .env)
    lub ustawiane na wartości domyślne.

    :cvar SECRET_KEY: Tajny klucz używany przez Flask do celów kryptograficznych.
    :vartype SECRET_KEY: str
    :cvar SQLALCHEMY_DATABASE_URI: Ścieżka do bazy danych SQLAlchemy.
    :vartype SQLALCHEMY_DATABASE_URI: str
    :cvar SQLALCHEMY_TRACK_MODIFICATIONS: Wyłącza śledzenie modyfikacji obiektów SQLAlchemy.
    :vartype SQLALCHEMY_TRACK_MODIFICATIONS: bool
    :cvar LANGUAGES: Lista obsługiwanych języków dla tłumaczeń.
    :vartype LANGUAGES: list
    :cvar BABEL_DEFAULT_LOCALE: Domyślny język aplikacji.
    :vartype BABEL_DEFAULT_LOCALE: str
    """

    SECRET_KEY = OS.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = OS.environ.get(
        "DATABASE_URI"
    ) or "sqlite:///" + OS.path.join(Ścieżka_Root, "Baza_Danych.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = OS.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
