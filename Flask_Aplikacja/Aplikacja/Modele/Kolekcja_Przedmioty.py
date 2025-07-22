"""Model bazy danych dla tabeli 'Przedmioty'.

Główny moduł modelu kolekcji, definiujący strukturę przedmiotu,
który jest centralnym elementem aplikacji.
"""

#! Zewnętrzne importy
#! Lokalne importy
from Aplikacja.Rozszerzenia import DB
from sqlalchemy import DECIMAL
from sqlalchemy.sql import func as FUNC


#! Main
class Przedmiot(DB.Model):
    """Model tabeli 'Przedmioty' w bazie danych.

    Reprezentuje pojedynczy przedmiot w kolekcji użytkownika.

    :ivar int id: Unikalny identyfikator przedmiotu (klucz główny).
    :ivar str nazwa: Nazwa przedmiotu.
    :ivar str opis: Opcjonalny opis przedmiotu.
    :ivar datetime data_dodania: Data i czas dodania przedmiotu.
    :ivar datetime data_edycji: Data i czas ostatniej edycji przedmiotu.
    :ivar int id_wlasciciel: Klucz obcy wskazujący na właściciela przedmiotu.
    :ivar Decimal cena_zakupu: Cena, za jaką przedmiot został nabyty.
    :ivar int id_cena_zakupu_waluta: Klucz obcy waluty dla ceny zakupu.
    :ivar Decimal wartosc_rynkowa: Aktualna wartość rynkowa przedmiotu.
    :ivar int id_wartosc_rynkowa_waluta: Klucz obcy waluty dla wartości rynkowej.
    :ivar int id_kategoria: Klucz obcy wskazujący na kategorię przedmiotu.
    :ivar bool czy_prywatne: Flaga określająca, czy przedmiot jest widoczny publicznie.
    """

    __tablename__ = "Przedmioty"

    id = DB.Column(DB.Integer, primary_key=True)
    nazwa = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)
    data_dodania = DB.Column(
        DB.DateTime(timezone=True), server_default=FUNC.now(), nullable=False
    )
    data_edycji = DB.Column(DB.DateTime(timezone=True))
    id_wlasciciel = DB.Column(DB.Integer, DB.ForeignKey("Użytkownicy.id"))
    cena_zakupu = DB.Column(DECIMAL(precision=10, scale=2))
    id_cena_zakupu_waluta = DB.Column(
        DB.Integer, DB.ForeignKey("Waluty.id"), nullable=False
    )
    wartosc_rynkowa = DB.Column(DECIMAL(precision=10, scale=2))
    id_wartosc_rynkowa_waluta = DB.Column(
        DB.Integer, DB.ForeignKey("Waluty.id"), nullable=False
    )
    id_kategoria = DB.Column(DB.Integer, DB.ForeignKey("Kategorie.id"), nullable=False)
    czy_prywatne = DB.Column(DB.Boolean)

    wlasciciel = DB.relationship(
        "Aplikacja.Modele.Użytkownicy.Uzytkownik",
        back_populates="przedmioty_uzytkownika",
        lazy=True,
    )

    kategoria = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Kategorie.Kategoria",
        back_populates="przedmioty",
        lazy=True,
    )

    waluta_zakupu = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Waluty.Waluta",
        foreign_keys=[id_cena_zakupu_waluta],
        back_populates="przedmioty_cena_zakupu",
        lazy=True,
    )

    waluta_rynkowa = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Waluty.Waluta",
        foreign_keys=[id_wartosc_rynkowa_waluta],
        back_populates="przedmioty_wartosc_rynkowa",
        lazy=True,
    )

    pola_wlasne = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Pola_Własne.PoleWlasne",
        back_populates="przedmiot",
        lazy=True,
        cascade="all, delete-orphan",
    )
    notatki = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Notatki.Notatka",
        back_populates="przedmiot",
        lazy=True,
        cascade="all, delete-orphan",
    )
    zdjecia = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Zdjęcia.Zdjecie",
        back_populates="przedmiot",
        lazy=True,
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        """Reprezentacja tekstowa obiektu Przedmiot.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Przedmiot ---> ID: '{self.id}', Nazwa: '{self.nazwa}'."
