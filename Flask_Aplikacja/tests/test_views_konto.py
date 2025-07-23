import pytest
from Aplikacja.Modele.Użytkownicy import Uzytkownik
from werkzeug.security import check_password_hash


@pytest.mark.usefixtures("init_database")
class TestKontoViews:
    """
    Testy integracyjne dla widoków z blueprintu Konto,
    skupione na logice widoków i weryfikacji danych.
    """

    def test_rejestracja_nowego_uzytkownika(self, client):
        response = client.post(
            "/konto/rejestracja/",
            data={
                "Pole_Login": "nowyuser",
                "Pole_Hasło_1": "nowehaslo123",
                "Pole_Hasło_2": "nowehaslo123",
                "Pole_Email": "nowy@test.com",
            },
        )

        assert response.status_code == 302
        with client.session_transaction() as sess:
            flashes = sess.get("_flashes", [])
            assert len(flashes) > 0
            assert flashes[0][1] == "Rejestracja zakońoczna pomyślnie."

        uzytkownik = Uzytkownik.query.filter_by(login="nowyuser").first()
        assert uzytkownik is not None

    def test_logowanie_poprawne(self, client):
        response = client.post(
            "/konto/logowanie/",
            data={"Pole_Login": "testuser1", "Pole_Hasło": "password123"},
        )

        assert response.status_code == 302
        with client.session_transaction() as sess:
            flashes = sess.get("_flashes", [])
            assert len(flashes) > 0
            assert flashes[0][1] == "Zalogowano jako: 'testuser1'."

    def test_get_strona_rejestracji(self, client):
        response = client.get("/konto/rejestracja/")
        assert response.status_code == 200
        assert "Rejestracja" in response.data.decode("utf-8")

    def test_rejestracja_istniejacego_uzytkownika(self, client):
        response = client.post(
            "/konto/rejestracja/",
            data={
                "Pole_Login": "testuser1",
                "Pole_Hasło_1": "innehaslo123",
                "Pole_Hasło_2": "innehaslo123",
            },
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert "Takie konto już istnieje." in response.data.decode("utf-8")

    def test_logowanie_niepoprawne_haslo(self, client):
        response = client.post(
            "/konto/logowanie/",
            data={"Pole_Login": "testuser1", "Pole_Hasło": "wrongpassword"},
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert (
            "Taki użytkownik nie istnieje lub podano niepoprawne hasło."
            in response.data.decode("utf-8")
        )

    def test_wylogowanie(self, client):
        client.post(
            "/konto/logowanie/",
            data={"Pole_Login": "testuser1", "Pole_Hasło": "password123"},
        )
        response = client.get("/konto/wyloguj/", follow_redirects=True)
        assert response.status_code == 200
        assert "Wylogowano." in response.data.decode("utf-8")

    def test_edycja_konta(self, client):
        client.post(
            "/konto/logowanie/",
            data={"Pole_Login": "testuser1", "Pole_Hasło": "password123"},
        )
        response = client.post(
            "/konto/edytuj-konto/",
            data={
                "Pole_Login": "nowy_login",
                "Pole_Email": "nowy@email.com",
                "Pole_Opis": "Nowy opis",
            },
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert "Zapisano zmiany konta." in response.data.decode("utf-8")
        uzytkownik = Uzytkownik.query.filter_by(login="nowy_login").first()
        assert uzytkownik is not None

    def test_zmiana_hasla(self, client):
        client.post(
            "/konto/logowanie/",
            data={"Pole_Login": "testuser1", "Pole_Hasło": "password123"},
        )
        response = client.post(
            "/konto/zmiana-hasla/",
            data={
                "Pole_Stare_Hasło": "password123",
                "Pole_Nowe_Hasło_1": "supernowehaslo",
                "Pole_Nowe_Hasło_2": "supernowehaslo",
            },
            follow_redirects=True,
        )
        assert response.status_code == 200
        assert "Hasło zostało zmienione." in response.data.decode("utf-8")
        uzytkownik = Uzytkownik.query.filter_by(login="testuser1").first()
        assert check_password_hash(uzytkownik.haslo, "supernowehaslo")
