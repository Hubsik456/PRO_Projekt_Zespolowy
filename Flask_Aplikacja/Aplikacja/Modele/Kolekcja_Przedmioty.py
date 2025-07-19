"""WIP"""

#! Zewnętrzne importy
from sqlalchemy.sql import func as FUNC
from sqlalchemy import DECIMAL

#! Lokalne importy
from Aplikacja.Rozszerzenia import DB

#! Main
class Przedmiot(DB.Model):
    __tablename__ = "Przedmioty"

    id = DB.Column(DB.Integer, primary_key=True)
    nazwa = DB.Column(DB.String(100), nullable=False)
    opis = DB.Column(DB.Text)
    data_dodania = DB.Column(DB.DateTime(timezone=True), server_default=FUNC.now(), nullable=False)
    data_edycji = DB.Column(DB.DateTime(timezone=True))
    id_wlasciciel = DB.Column(DB.Integer, DB.ForeignKey("Użytkownicy.id"))
    cena_zakupu = DB.Column(DECIMAL(precision=10, scale=2))
    id_cena_zakupu_waluta = DB.Column(DB.Integer, DB.ForeignKey("Waluty.id"), nullable=False)
    wartosc_rynkowa = DB.Column(DECIMAL(precision=10, scale=2))
    id_wartosc_rynkowa_waluta = DB.Column(DB.Integer, DB.ForeignKey("Waluty.id"), nullable=False)
    id_kategoria = DB.Column(DB.Integer, DB.ForeignKey("Kategorie.id"), nullable=False)
    czy_prywatne = DB.Column(DB.Boolean)

    wlasciciel = DB.relationship(
        "Aplikacja.Modele.Użytkownicy.Uzytkownik",
        back_populates="przedmioty_uzytkownika", # Użyj back_populates
        lazy=True
    )

    # To jest kluczowa relacja, która łączy Przedmiot z Kategorią (jeden Przedmiot ma jedną Kategorię)
    kategoria = DB.relationship( # Nazwa atrybutu relacji
        "Aplikacja.Modele.Kolekcja_Kategorie.Kategoria",
        back_populates="przedmioty", # back_populates wskazuje na atrybut relacji w Kategoria
        lazy=True
    )

    # Poprzednio miałeś tu relację "przedmiot_kategoria_powiazana", która była chyba błędnym backrefem
    # lub redundantną definicją. Usunąłem ją, bo relacja "kategoria" jest wystarczająca.

    waluta_zakupu = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Waluty.Waluta",
        foreign_keys=[id_cena_zakupu_waluta],
        back_populates="przedmioty_cena_zakupu", # Użyj back_populates
        lazy=True
    )

    waluta_rynkowa = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Waluty.Waluta",
        foreign_keys=[id_wartosc_rynkowa_waluta],
        back_populates="przedmioty_wartosc_rynkowa", # Użyj back_populates
        lazy=True
    )

    # Relacje do Notatek, Pol_Własnych, Zdjęć (upewnij się, że używają back_populates)
    pola_wlasne = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Pola_Własne.PoleWlasne",
        back_populates="przedmiot", # back_populates do relacji w PoleWlasne
        lazy=True
    )
    notatki = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Notatki.Notatka",
        back_populates="przedmiot", # back_populates do relacji w Notatka
        lazy=True
    )
    zdjecia = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Zdjęcia.Zdjecie",
        back_populates="przedmiot", # back_populates do relacji w Zdjecie
        lazy=True
    )

    def __repr__(self):
        return f"Przedmiot ---> ID: '{self.id}', Nazwa: '{self.nazwa}'."