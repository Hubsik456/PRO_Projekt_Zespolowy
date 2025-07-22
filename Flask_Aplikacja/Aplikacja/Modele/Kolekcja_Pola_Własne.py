"""Model bazy danych dla tabeli 'Pola_Wlasne'.

Moduł definiuje model SQLAlchemy dla wartości niestandardowych pól,
które użytkownik może dodać do swoich przedmiotów w kolekcji.
"""

#! Lokalne Importy
from Aplikacja.Rozszerzenia import DB


#! Main
class PoleWlasne(DB.Model):
    """Model tabeli 'Pola_Wlasne' w bazie danych.

    Przechowuje konkretną wartość dla niestandardowego pola przypisanego
    do przedmiotu.

    :ivar int id: Unikalny identyfikator pola (klucz główny).
    :ivar int id_rodzaj: Klucz obcy wskazujący na rodzaj tego pola.
    :ivar int id_przedmiot: Klucz obcy wskazujący na przedmiot, do którego należy to pole.
    :ivar str wartosc: Wartość pola, przechowywana jako tekst.
    :ivar Przedmiot przedmiot: Relacja do obiektu nadrzędnego Przedmiot.
    :ivar PoleWlasneRodzaj typ_pola_wlasnego: Relacja do obiektu definiującego typ tego pola.
    """

    __tablename__ = "Pola_Wlasne"

    id = DB.Column(DB.Integer, primary_key=True)
    id_rodzaj = DB.Column(
        DB.Integer, DB.ForeignKey("Pola_Wlasne_Rodzaje.id"), nullable=False
    )
    id_przedmiot = DB.Column(DB.Integer, DB.ForeignKey("Przedmioty.id"), nullable=False)
    wartosc = DB.Column(DB.Text)

    przedmiot = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Przedmioty.Przedmiot",
        back_populates="pola_wlasne",
        lazy=True,
    )

    typ_pola_wlasnego = DB.relationship(
        "Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje.PoleWlasneRodzaj",
        back_populates="powiazane_pola_wlasne",
        lazy=True,
    )

    def __repr__(self):
        """Reprezentacja tekstowa obiektu PoleWlasne.

        :return: Tekstowa reprezentacja obiektu.
        :rtype: str
        """
        return f"Pole Własne ---> ID: '{self.id}', Wartość: '{self.wartosc}'"
