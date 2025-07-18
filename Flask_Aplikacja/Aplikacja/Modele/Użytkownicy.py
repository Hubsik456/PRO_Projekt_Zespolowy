"""Moduł z modelem bazy danych dla tabeli Użytkownicy."""

#! Zewnętrzne Importy
#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB
from flask_login import UserMixin as USER_MIXIN
from sqlalchemy.sql import func as FUNC


#! Main
class Użytkownicy(USER_MIXIN, DB.Model):
    """Model tabeli 'Użytkownicy' w bazie danych.

    Reprezentuje użytkownika aplikacji i przechowuje jego dane,
    takie jak login, hasło, email i inne.

    :param str Login: Login użytkownika. Musi być unikalny.
    :param str Hasło: Zahaszowane hasło użytkownika.
    :param str Email: Adres email użytkownika.
    :param str Opis: Opcjonalny opis użytkownika.

    :ivar int ID: Unikalny identyfikator użytkownika (klucz główny).
    :ivar str Login: Login użytkownika.
    :ivar str Hasło: Zahaszowane hasło.
    :ivar str Email: Adres email.
    :ivar datetime Dodano: Data i czas dodania użytkownika.
    :ivar str Opis: Opcjonalny opis profilu.
    """

    __tablename__ = "Użytkownicy"

    ID = DB.Column(DB.Integer, primary_key=True)
    Login = DB.Column(DB.String(100), unique=True, nullable=False)
    Hasło = DB.Column(
        DB.String(100), nullable=False
    )  # TODO: Czy tu na pewno ma być String(100)
    Email = DB.Column(DB.String(100), nullable=False, unique=False)
    Dodano = DB.Column(
        DB.DateTime(timezone=True), server_default=FUNC.now(), nullable=False
    )
    Opis = DB.Column(DB.Text)

    def get_id(self):
        """Zwraca ID użytkownika, wymagane przez Flask-Login.

        :return: ID użytkownika.
        :rtype: int
        """
        return self.ID

    def __repr__(self):
        """Reprezentacja tekstowa obiektu Użytkownicy.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Użytkownik ---> ID: '{self.ID}'"
