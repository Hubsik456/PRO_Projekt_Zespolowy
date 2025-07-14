# Notatki

## **Aktywacja venv:**

    .\Scripts\activate.bat

## **Tworzenie środowiska:**

    git clone https://github.com/Hubsik456/PRO_Projekt_Zespolowy.git
    python -m venv "PRO_Projekt_Zespolowy"

## **Instalacja Bibliotek:**

    pip install Flask Flask_Login Flask_sqlalchemy Flask_wtf dotenv

## **Uruchamianie aplikacji:**

    flask run

## **Generowanie bazy danych:**

    flask shell

    from Aplikacja.Baza_Danych import DB
    from Aplikacja.Modele import Użytkownicy
    DB.drop_all()
    DB.create_all()

    from Aplikacja.Modele.Użytkownicy import Użytkownicy as Użytkownik
    Użytkownik_1 = Użytkownik(ID=1, Login="Login_1", Hasło="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", Email="wip_1@wip.wip") # Hasło: "Hasło#123"
    Użytkownik_2 = Użytkownik(ID=2, Login="Login_2", Hasło="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", Email="wip_2@wip.wip") # Hasło: "Hasło#123"
    Użytkownik_3 = Użytkownik(ID=3, Login="Login_3", Hasło="scrypt:32768:8:1$oIQDlKkWWMceQYtD$de949013c356f9786d7cfd3981854df2a249e70c7b53607d4de91abfeb688176f4af9142c6aae189a6903b6ea820843a6856f5f0ce5e873fbe4a59ff26ec0771", Email="wip_3@wip.wip") # Hasło: "Hasło#123"
    DB.session.add(Użytkownik_1)
    DB.session.add(Użytkownik_2)
    DB.session.add(Użytkownik_3)
    DB.session.commit()

    exit()
