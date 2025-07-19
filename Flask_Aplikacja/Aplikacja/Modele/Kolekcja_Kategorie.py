"""WIP"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class Kategoria(DB.Model):
    __tablename__ = "Kategorie"

    id = DB.Column(DB.Integer, primary_key=True)
    nazwa = DB.Column(DB.String(100), unique=True, nullable=False)
    opis = DB.Column(DB.Text)

    # Ta relacja tworzy listę przedmiotów powiązanych z daną kategorią.
    # Używamy back_populates, aby powiązać ją z relacją 'kategoria' w Przedmiot.
    przedmioty = DB.relationship( # Zmieniono nazwę na "przedmioty" (jest OK, lista)
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="kategoria", # back_populates wskazuje na nazwę atrybutu relacji w Przedmiot
        lazy=True
    )

    def __repr__(self):
        return f"Kategoria ---> ID: '{self.id}', Nazwa: '{self.nazwa}'."