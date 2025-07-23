import pytest


@pytest.mark.usefixtures("client")
class TestMainViews:
    """Testy dla głównych, publicznych widoków aplikacji."""

    def test_widok_index(self, client):
        """Sprawdza, czy strona główna "/" zwraca kod 200 OK."""
        response = client.get("/")
        assert response.status_code == 200
        assert b"Kurator Kolekcji" in response.data

    def test_widok_o_programie(self, client):
        """Sprawdza, czy strona "/o-programie/" zwraca kod 200 OK."""
        response = client.get("/o-programie/")
        assert response.status_code == 200
        assert b"O Programie" in response.data

    def test_widok_polityka_prywatnosci(self, client):
        """Sprawdza, czy strona "/polityka-prywatnosci/" zwraca kod 200 OK."""
        response = client.get("/polityka-prywatnosci/")
        assert response.status_code == 200
        assert b"Polityka Prywatno" in response.data

    def test_widok_motyw_post(self, client):
        """Sprawdza, czy wysłanie formularza motywu ustawia ciasteczko i przekierowuje."""
        response = client.post("/motyw/", data={"Pole_Motyw": "pulse"})

        assert response.status_code == 302
        assert response.location == "/"

        set_cookie_header = response.headers["Set-Cookie"]
        assert "Motyw=pulse" in set_cookie_header
