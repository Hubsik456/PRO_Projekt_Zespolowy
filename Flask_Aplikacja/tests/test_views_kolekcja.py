import pytest
from Aplikacja.Modele.Kolekcja_Kategorie import Kategoria
from Aplikacja.Modele.Kolekcja_Przedmioty import Przedmiot
from Aplikacja.Modele.Kolekcja_Waluty import Waluta
from Aplikacja.Modele.Użytkownicy import Uzytkownik
from werkzeug.security import generate_password_hash


@pytest.mark.usefixtures("init_database")
class TestKolekcjaViews:
    """
    Testy integracyjne dla widoków z blueprintu Kolekcja.
    """

    def login(self, client, login, haslo):
        """Funkcja pomocnicza do logowania użytkownika."""
        return client.post(
            "/konto/logowanie/",
            data=dict(Pole_Login=login, Pole_Hasło=haslo),
            follow_redirects=True,
        )

    def test_widok_moja_kolekcja_zalogowany(self, client):
        """Sprawdza, czy zalogowany użytkownik widzi swoją kolekcję."""
        self.login(client, "testuser1", "password123")
        response = client.get("/kolekcja/moja-kolekcja/")
        assert response.status_code == 200
        assert "Laptop" in response.data.decode("utf-8")

    def test_dodawanie_przedmiotu(self, client):
        """Sprawdza dodawanie nowego przedmiotu."""
        self.login(client, "testuser1", "password123")
        item_data = {
            "nazwa": "Stary Zegar",
            "opis": "Zegar z kukułką",
            "cena_zakupu": 120.00,
            "id_cena_zakupu_waluta": 1,
            "wartosc_rynkowa": 200.00,
            "id_wartosc_rynkowa_waluta": 1,
            "id_kategoria": 1,
        }
        response = client.post(
            "/kolekcja/moja-kolekcja/dodaj/", data=item_data, follow_redirects=True
        )
        assert response.status_code == 200
        assert "Dodano nowy przedmiot do Twojej kolekcji." in response.data.decode(
            "utf-8"
        )
        assert Przedmiot.query.filter_by(nazwa="Stary Zegar").first() is not None

    def test_edycja_przedmiotu(self, client):
        """
        Sprawdza edycję przedmiotu, testując komunikat flash w sesji.
        """
        self.login(client, "testuser1", "password123")
        przedmiot = Przedmiot.query.filter_by(nazwa="Laptop").first()
        updated_data = {
            "nazwa": "Laptop po renowacji",
            "opis": "Działa lepiej",
            "cena_zakupu": 2500.00,
            "id_cena_zakupu_waluta": 1,
            "wartosc_rynkowa": 2200.00,
            "id_wartosc_rynkowa_waluta": 1,
            "id_kategoria": 1,
        }

        response = client.post(
            f"/kolekcja/moja-kolekcja/edytuj/{przedmiot.id}/", data=updated_data
        )
        assert response.status_code == 302

        with client.session_transaction() as sess:
            flashes = sess.get("_flashes", [])
            assert (
                flashes[0][1] == f"Zaktualizowano przedmiot '{updated_data['nazwa']}'."
            )

    def test_usuwanie_przedmiotu(self, client, init_database):
        """
        Sprawdza usunięcie przedmiotu, testując komunikat flash w sesji.
        """
        self.login(client, "testuser1", "password123")
        przedmiot = Przedmiot.query.filter_by(nazwa="Laptop").first()
        przedmiot_id = przedmiot.id

        response = client.post(f"/kolekcja/moja-kolekcja/usun/{przedmiot_id}/")
        assert response.status_code == 302

        with client.session_transaction() as sess:
            flashes = sess.get("_flashes", [])
            assert (
                flashes[0][1]
                == f"Przedmiot '{przedmiot.nazwa}' został pomyślnie usunięty."
            )

        db = init_database
        przedmiot_po_usunieciu = db.session.get(Przedmiot, przedmiot_id)
        assert przedmiot_po_usunieciu is None

    def test_proba_edycji_cudzego_przedmiotu(self, app, client, init_database):
        """Sprawdza, czy próba edycji cudzego przedmiotu zwraca błąd 404."""
        with app.app_context():
            db = init_database
            uzytkownik_b = Uzytkownik(
                login="userB",
                email="b@b.com",
                haslo=generate_password_hash("passwordB"),
            )

            kategoria = db.session.get(Kategoria, 1)
            waluta = db.session.get(Waluta, 1)

            db.session.add(uzytkownik_b)
            db.session.commit()
            przedmiot_b = Przedmiot(
                nazwa="ZegarekB",
                wlasciciel=uzytkownik_b,
                kategoria=kategoria,
                id_cena_zakupu_waluta=waluta.id,
                id_wartosc_rynkowa_waluta=waluta.id,
            )
            db.session.add(przedmiot_b)
            db.session.commit()
            przedmiot_b_id = przedmiot_b.id

        self.login(client, "testuser1", "password123")
        response = client.get(f"/kolekcja/moja-kolekcja/edytuj/{przedmiot_b_id}/")
        assert response.status_code == 404
