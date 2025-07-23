from Aplikacja.Modele.Kolekcja_Notatki import Notatka
from Aplikacja.Modele.Kolekcja_Pola_Własne import PoleWlasne
from Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje import PoleWlasneRodzaj
from Aplikacja.Modele.Kolekcja_Przedmioty import Przedmiot
from Aplikacja.Modele.Kolekcja_Zdjęcia import Zdjecie
from Aplikacja.Modele.Użytkownicy import Uzytkownik
from werkzeug.security import check_password_hash


def test_modelu_uzytkownika(init_database):
    """Sprawdza poprawność danych w modelu Uzytkownik."""
    uzytkownik = Uzytkownik.query.filter_by(login="testuser1").first()
    assert uzytkownik is not None
    assert uzytkownik.login == "testuser1"
    assert check_password_hash(uzytkownik.haslo, "password123")
    assert not check_password_hash(uzytkownik.haslo, "wrongpassword")


def test_modelu_przedmiotu_i_relacji(init_database):
    """Sprawdza poprawność danych i relacji w modelu Przedmiot."""
    przedmiot = Przedmiot.query.filter_by(nazwa="Laptop").first()
    assert przedmiot is not None
    assert przedmiot.opis == "Używany laptop"
    assert przedmiot.wlasciciel.login == "testuser1"
    assert przedmiot.kategoria.nazwa == "Elektronika"
    assert przedmiot.waluta_zakupu.skrot == "PLN"
    assert Uzytkownik.query.first().przedmioty_uzytkownika[0].nazwa == "Laptop"


def test_modelu_notatki(init_database):
    """Sprawdza dodawanie notatki i jej relację z przedmiotem."""
    db = init_database
    przedmiot = Przedmiot.query.first()
    notatka = Notatka(
        tytul="Info", opis="Porysowana obudowa", id_przedmiot=przedmiot.id
    )
    db.session.add(notatka)
    db.session.commit()

    assert Notatka.query.count() == 1
    assert przedmiot.notatki[0].tytul == "Info"


def test_modelu_zdjecia(init_database):
    """Sprawdza dodawanie zdjęcia i jego relację z przedmiotem."""
    db = init_database
    przedmiot = Przedmiot.query.first()
    zdjecie = Zdjecie(
        tytul="Laptop od frontu",
        zdjecie_dane=b"testowe_dane_binarne",
        mimetype="image/jpeg",
        id_przedmiot=przedmiot.id,
    )
    db.session.add(zdjecie)
    db.session.commit()

    assert Zdjecie.query.count() == 1
    assert Zdjecie.query.first().mimetype == "image/jpeg"
    assert przedmiot.zdjecia[0].tytul == "Laptop od frontu"


def test_modelu_pola_wlasnego(init_database):
    """Sprawdza dodawanie pola własnego i jego relacje."""
    db = init_database
    przedmiot = Przedmiot.query.first()
    rodzaj_pola = PoleWlasneRodzaj.query.first()

    pole_wlasne = PoleWlasne(
        wartosc="Dobry", id_przedmiot=przedmiot.id, id_rodzaj=rodzaj_pola.id
    )
    db.session.add(pole_wlasne)
    db.session.commit()

    assert PoleWlasne.query.count() == 1
    assert przedmiot.pola_wlasne[0].wartosc == "Dobry"
    assert przedmiot.pola_wlasne[0].typ_pola_wlasnego.nazwa == "Stan"
