"""Moduł z modelem bazy danych dla tabeli Użytkownicy."""

#! Zewnętrzne Importy
from sqlalchemy.sql import func as FUNC
from flask_login import UserMixin as USER_MIXIN

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class Uzytkownik(USER_MIXIN, DB.Model):
    """Model tabeli 'Uzytkownicy' w bazie danych.

    Reprezentuje użytkownika aplikacji i przechowuje jego dane,
    takie jak login, hasło, email i inne.

    :param str login: Login użytkownika. Musi być unikalny.
    :param str haslo: Zahaszowane hasło użytkownika.
    :param str email: Adres email użytkownika.
    :param str opis: Opcjonalny opis użytkownika.

    :ivar int id: Unikalny identyfikator użytkownika (klucz główny).
    :ivar str login: Login użytkownika.
    :ivar str haslo: Zahaszowane hasło.
    :ivar str email: Adres email.
    :ivar datetime dodano: Data i czas dodania użytkownika.
    :ivar str opis: Opcjonalny opis profilu.
    """

    __tablename__ = "Użytkownicy"

    id = DB.Column(DB.Integer, primary_key=True)
    login = DB.Column(DB.String(100), unique=True, nullable=False)
    haslo = DB.Column(
        DB.Text, nullable=False
    )
    email = DB.Column(DB.String(100), unique=True, nullable=False)
    dodano = DB.Column(
        DB.DateTime(timezone=True), server_default=FUNC.now(), nullable=False
    )
    opis = DB.Column(DB.Text)

    przedmioty_uzytkownika = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="wlasciciel",
        lazy=True
    )

    def get_id(self):
        """Zwraca ID użytkownika, wymagane przez Flask-Login.

        :return: ID użytkownika.
        :rtype: int
        """
        return f"{self.id}"

    def __repr__(self):
        """Reprezentacja tekstowa obiektu Uzytkownik.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Użytkownik ---> ID: '{self.id}'"