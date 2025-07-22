"""Model bazy danych dla tabeli 'Użytkownicy'.

Moduł definiuje model SQLAlchemy dla użytkowników aplikacji, integrując
się z Flask-Login do zarządzania sesjami.
"""

#! Zewnętrzne Importy
#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB
from flask_login import UserMixin as USER_MIXIN
from sqlalchemy.sql import func as FUNC


#! Main
class Uzytkownik(USER_MIXIN, DB.Model):
    """Model tabeli 'Uzytkownicy' w bazie danych.

    Reprezentuje użytkownika aplikacji i przechowuje jego dane.
    Dziedziczy z UserMixin dla kompatybilności z Flask-Login.

    :ivar int id: Unikalny identyfikator użytkownika (klucz główny).
    :ivar str login: Login użytkownika, musi być unikalny.
    :ivar str haslo: Zahaszowane hasło użytkownika.
    :ivar str email: Adres email użytkownika, musi być unikalny.
    :ivar datetime dodano: Data i czas utworzenia konta.
    :ivar str opis: Opcjonalny opis profilu użytkownika.
    :ivar list przedmioty_uzytkownika: Lista przedmiotów posiadanych przez użytkownika.
    """

    __tablename__ = "Użytkownicy"

    id = DB.Column(DB.Integer, primary_key=True)
    login = DB.Column(DB.String(100), unique=True, nullable=False)
    haslo = DB.Column(DB.Text, nullable=False)
    email = DB.Column(DB.String(100), unique=True, nullable=False)
    dodano = DB.Column(
        DB.DateTime(timezone=True), server_default=FUNC.now(), nullable=False
    )
    opis = DB.Column(DB.Text)

    przedmioty_uzytkownika = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="wlasciciel",
        lazy=True,
    )

    def get_id(self):
        """Zwraca ID użytkownika, wymagane przez Flask-Login.

        :return: ID użytkownika jako string.
        :rtype: str
        """
        return f"{self.id}"

    def __repr__(self):
        """Reprezentacja tekstowa obiektu Uzytkownik.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Użytkownik ---> ID: '{self.id}'"
