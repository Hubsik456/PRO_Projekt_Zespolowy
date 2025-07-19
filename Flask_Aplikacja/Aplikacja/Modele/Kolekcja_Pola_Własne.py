"""WIP"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB

#! Main
class PoleWlasne(DB.Model):
    __tablename__ = "Pola_Wlasne"

    id = DB.Column(DB.Integer, primary_key=True)
    id_rodzaj = DB.Column(DB.Integer, DB.ForeignKey("Pola_Wlasne_Rodzaje.id"), nullable=False)
    id_przedmiot = DB.Column(DB.Integer, DB.ForeignKey("Przedmioty.id"), nullable=False)
    wartosc = DB.Column(DB.Text)

    przedmiot = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="pola_wlasne", # Użyj back_populates
        lazy=True
    )

    # Używamy back_populates tutaj, aby powiązać z relacją 'pola_wlasne' w PoleWlasneRodzaj
    typ_pola_wlasnego = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje.PoleWlasneRodzaj",
        back_populates="powiazane_pola_wlasne", # back_populates musi wskazywać na nazwę atrybutu relacji w drugiej klasie
        lazy=True
    )

    def __repr__(self):
        return f"Pole Własne ---> ID: '{self.id}', Wartość: '{self.wartosc}'"