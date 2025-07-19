#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class Waluta(DB.Model):
    __tablename__ = "Waluty"

    id = DB.Column(DB.Integer, primary_key=True)
    skrot = DB.Column(DB.String(5), unique=True, nullable=False)
    nazwa = DB.Column(DB.String(100), unique=True, nullable=False)

    # Relacja dla przedmiotów, które mają tę walutę jako cenę zakupu
    przedmioty_cena_zakupu = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot", # Cel - klasa Przedmiot
        back_populates="waluta_zakupu", # Nazwa atrybutu relacji w klasie Przedmiot
        # Jawnie wskazujemy, że ta relacja używa klucza obcego id_cena_zakupu_waluta
        foreign_keys="Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot.id_cena_zakupu_waluta",
        lazy=True
    )

    # Relacja dla przedmiotów, które mają tę walutę jako wartość rynkową
    przedmioty_wartosc_rynkowa = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot", # Cel - klasa Przedmiot
        back_populates="waluta_rynkowa", # Nazwa atrybutu relacji w klasie Przedmiot
        # Jawnie wskazujemy, że ta relacja używa klucza obcego id_wartosc_rynkowa_waluta
        foreign_keys="Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot.id_wartosc_rynkowa_waluta",
        lazy=True
    )

    def __repr__(self):
        return f"Waluta ---> ID: '{self.id}', Skrót: '{self.skrot}'."