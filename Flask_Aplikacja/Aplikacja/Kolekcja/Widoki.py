"""WIP

Widoki (routes) dla Blueprintu #3 - Kolekcja.

Ten moduł zawiera logikę i definicje URL dla wszystkich stron
związanych z zarządzaniem kolekcjami użytkowników.
"""

#! Zewnętrzne Importy
from flask import render_template as RENDER_TEMPLATE, request as REQUEST, flash as FLASH, redirect as REDIRECT, url_for as URL_FOR, abort as ABORT
from flask_login import login_required as LOGIN_REQUIRED, current_user as CURRENT_USER
from sqlalchemy.sql import func as FUNC

#! Lokalne importy
from Aplikacja.Rozszerzenia import DB
from Aplikacja.Kolekcja import Blueprint_3

from Aplikacja.Kolekcja.Formularze.Dodanie_Przedmiotu import Formularz_Dodanie_Przedmiotu
from Aplikacja.Kolekcja.Formularze.Pole_Własne import Formularz_Pole_Własne

from Aplikacja.Modele.Użytkownicy import Uzytkownik
from Aplikacja.Modele.Kolekcja_Przedmioty import Przedmiot
from Aplikacja.Modele.Kolekcja_Pola_Własne_Rodzaje import PoleWlasneRodzaj
from Aplikacja.Modele.Kolekcja_Pola_Własne import PoleWlasne
from Aplikacja.Modele.Kolekcja_Waluty import Waluta
from Aplikacja.Modele.Kolekcja_Kategorie import Kategoria
from Aplikacja.Modele.Kolekcja_Notatki import Notatka
from Aplikacja.Modele.Kolekcja_Zdjęcia import Zdjecie

#! Main
@Blueprint_3.route("/")
def Widok_Kolekcja_Index():
    """Renderuje stronę główną z kolekcjami użytkownika.

    :return: Wyrenderowany szablon HTML strony głównej kolekcji.
    :rtype: str
    """
    return RENDER_TEMPLATE("Kolekcja/index.html")

@Blueprint_3.route("/podsumowanie/")
def Widok_Kolekcja_Podsumowanie():
    return RENDER_TEMPLATE("Kolekcja/Podsumowanie.html")

@Blueprint_3.route("/<int:ID>")
@LOGIN_REQUIRED
def Widok_Kolekcja_Kolekcja(ID):
    return RENDER_TEMPLATE("Kolekcja/Kolekcja.html", ID=ID)

@Blueprint_3.route("/moja-kolekcja/")
@LOGIN_REQUIRED
def Widok_Kolekcja_Moja_Kolekcja():
    Kolekcja = CURRENT_USER.przedmioty_uzytkownika

    return RENDER_TEMPLATE("Kolekcja/Moja_Kolekcja.html", Kolekcja=Kolekcja)

@Blueprint_3.route("/moja-kolekcja/dodaj/", methods=["POST", "GET"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Dodaj():
    Formularz = Formularz_Dodanie_Przedmiotu()

    #? Dodanie opcji do `<select>`
    Select_Waluty = DB.session.execute(DB.select(Waluta)).scalars().all()
    # Pamiętaj o str() dla SelectField, nawet jeśli masz coerce=int, bo html zawsze wysyła string
    Formularz.id_cena_zakupu_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
    Formularz.id_wartosc_rynkowa_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]

    Select_Kategorie = DB.session.execute(DB.select(Kategoria)).scalars().all()
    Formularz.id_kategoria.choices = [(str(x.id), x.nazwa) for x in Select_Kategorie]

    Select_Pola_Wlasne_Rodzaje = DB.session.execute(DB.select(PoleWlasneRodzaj)).scalars().all()
    Select_Pola_Wlasne_Rodzaje_Pozycje = [(str(x.id), x.nazwa) for x in Select_Pola_Wlasne_Rodzaje]

    # Ustaw choices dla wszystkich pól własnych na formularzu (w tym domyślnych)
    for _Pole_Własne in Formularz.Pola_Własne:
        _Pole_Własne.form.id_rodzaj.choices = Select_Pola_Wlasne_Rodzaje_Pozycje

    #? Jeśli formularz został przesłany
    if REQUEST.method == "POST":
        # Ponownie ustaw choices w POST przed validate_on_submit(),
        # aby walidacja SelectField mogła działać prawidłowo.
        Formularz.id_cena_zakupu_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
        Formularz.id_wartosc_rynkowa_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
        Formularz.id_kategoria.choices = [(str(x.id), x.nazwa) for x in Select_Kategorie]

        for _Pole_Własne in Formularz.Pola_Własne:
            _Pole_Własne.form.id_rodzaj.choices = Select_Pola_Wlasne_Rodzaje_Pozycje

        if Formularz.validate_on_submit():
            # populate_obj dla głównego formularza zadziała teraz poprawnie,
            # ponieważ SelectField mają coerce=int i choices są prawidłowo ustawione.
            # Ważne: NIE używaj populate_obj dla Nowy_Przedmiot, bo tworzysz go ręcznie
            # i przypisujesz wartości bezpośrednio z Formularz.data
            Nowy_Przedmiot = Przedmiot(
                nazwa=Formularz.nazwa.data,
                opis=Formularz.opis.data,
                id_wlasciciel=CURRENT_USER.id,
                cena_zakupu=Formularz.cena_zakupu.data,
                id_cena_zakupu_waluta=Formularz.id_cena_zakupu_waluta.data,
                wartosc_rynkowa=Formularz.wartosc_rynkowa.data,
                id_wartosc_rynkowa_waluta=Formularz.id_wartosc_rynkowa_waluta.data,
                id_kategoria=Formularz.id_kategoria.data,
                czy_prywatne=Formularz.czy_prywatne.data
            )

            DB.session.add(Nowy_Przedmiot)
            DB.session.flush()

            for entry_form in Formularz.Pola_Własne.entries:
                if entry_form.form.id_rodzaj.data and entry_form.form.wartosc.data:
                    Nowe_Pole_Wlasne = PoleWlasne(
                        id_przedmiot=Nowy_Przedmiot.id,
                        id_rodzaj=entry_form.form.id_rodzaj.data, # Już jest int dzięki coerce=int
                        wartosc=entry_form.form.wartosc.data
                    )
                    DB.session.add(Nowe_Pole_Wlasne)
                elif entry_form.form.id_rodzaj.data or entry_form.form.wartosc.data:
                    FLASH(f"Pomijam niekompletne pole własne: rodzaj='{entry_form.form.id_rodzaj.data}', wartość='{entry_form.form.wartosc.data}'.", "warning")

            DB.session.commit()

            FLASH(f"Dodano nowy przedmiot do Twojej kolekcji.", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Moja_Kolekcja"))

        FLASH("Podano niepoprawne dane.", "danger")

    return RENDER_TEMPLATE("Kolekcja/Dodaj.html", Formularz=Formularz, Select_Pola_Wlasne_Rodzaje_Pozycje=Select_Pola_Wlasne_Rodzaje_Pozycje)

@Blueprint_3.route("/moja-kolekcja/szczegoly/<int:ID>")
@LOGIN_REQUIRED
def Widok_Kolekcja_Szczegóły(ID):
    #? Pobranie przedmiotów
    _Przedmiot = DB.session.execute(DB.select(Przedmiot).filter_by(id=ID)).scalar_one_or_none()

    #? Sprawdzenie czy przedmiot istnieje
    if _Przedmiot is None:
        ABORT(404)

    #? Sprawdzenie czy obecny użytkownik to właściciel przedmiotu
    if _Przedmiot.id_wlasciciel != CURRENT_USER.id:
        ABORT(403)

    return RENDER_TEMPLATE("Kolekcja/Przedmiot_Szczegóły.html", Przedmiot=_Przedmiot)

@Blueprint_3.route("/moja-kolekcja/edytuj/<int:ID>/", methods=["GET", "POST"])
@LOGIN_REQUIRED
def Widok_Kolekcja_Edytuj(ID):
    #? Pobranie przedmiotu
    _Przedmiot = DB.get_or_404(Przedmiot, ID)

    #? Sprawdzenie czy obency użytkownik to właściciel przedmiotu
    if _Przedmiot.id_wlasciciel != CURRENT_USER.id:
        ABORT(403)

    # Inicjujemy formularz. populate_obj zadziała na głównych polach.
    # FieldList będzie zawierać min_entries=1 puste pole na początku,
    # które później nadpiszemy lub dodamy do niego dane z _Przedmiot.pola_wlasne.
    Formularz = Formularz_Dodanie_Przedmiotu(obj=_Przedmiot)

    #* Dodanie pozycji do Select (główne pola formularza)
    Select_Waluty = DB.session.execute(DB.select(Waluta)).scalars().all()
    Formularz.id_cena_zakupu_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
    Formularz.id_wartosc_rynkowa_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]

    Select_Kategorie = DB.session.execute(DB.select(Kategoria)).scalars().all()
    Formularz.id_kategoria.choices = [(str(x.id), x.nazwa) for x in Select_Kategorie]

    Select_Pola_Wlasne_Rodzaje = DB.session.execute(DB.select(PoleWlasneRodzaj)).scalars().all()
    Select_Pola_Wlasne_Rodzaje_Pozycje = [(str(x.id), x.nazwa) for x in Select_Pola_Wlasne_Rodzaje] # ID jako stringi

    #* Przetwarzanie formularza - GET
    if REQUEST.method == "GET":
        # Wyczyść domyślne wpisy z FieldList, aby wypełnić je danymi z bazy
        Formularz.Pola_Własne.entries = []

        # Wypełnij FieldList istniejącymi danymi z obiektu _Przedmiot
        for x in _Przedmiot.pola_wlasne:
            Pozycja = Formularz.Pola_Własne.append_entry()
            # Ustaw choices dla TEGO konkretnego SelectField w sub-formularzu
            Pozycja.form.id_rodzaj.choices = Select_Pola_Wlasne_Rodzaje_Pozycje
            # Ważne: przypisujemy ID jako STRING, bo SelectField oczekuje stringów
            Pozycja.form.id_rodzaj.data = str(x.id_rodzaj)
            Pozycja.form.wartosc.data = x.wartosc

        # Jeśli _Przedmiot.pola_wlasne jest puste, dodaj jedno puste pole
        # (ponieważ min_entries=1 w Formularz_Dodanie_Przedmiotu)
        if not _Przedmiot.pola_wlasne:
            Pozycja = Formularz.Pola_Własne.append_entry()
            Pozycja.form.id_rodzaj.choices = Select_Pola_Wlasne_Rodzaje_Pozycje


    #* Przetwarzanie formularza - POST
    if REQUEST.method == "POST":
        # ZAWSZE ustawiaj choices przed validate_on_submit() w POST,
        # aby walidatory SelectField mogły prawidłowo działać dla wszystkich pól.
        Formularz.id_cena_zakupu_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
        Formularz.id_wartosc_rynkowa_waluta.choices = [(str(x.id), x.nazwa) for x in Select_Waluty]
        Formularz.id_kategoria.choices = [(str(x.id), x.nazwa) for x in Select_Kategorie]

        # Ustaw choices dla każdego sub-formularza w FieldList również w POST
        for _Pole_Własne in Formularz.Pola_Własne:
            _Pole_Własne.form.id_rodzaj.choices = Select_Pola_Wlasne_Rodzaje_Pozycje


        if Formularz.validate_on_submit():
            # populate_obj zadba o główne pola formularza (nazwa, opis, ceny itd.)
            Formularz.populate_obj(_Przedmiot)

            _Przedmiot.data_edycji = FUNC.now()

            # Usunięcie istniejących pól własnych
            # Iterujemy po kopii listy, aby uniknąć problemów z modyfikacją podczas iteracji
            for existing_pole_wlasne in list(_Przedmiot.pola_wlasne):
                DB.session.delete(existing_pole_wlasne)
            DB.session.flush() # Ważne: Zastosuj usunięcia w sesji przed dodaniem nowych

            # Dodawanie nowych pól własnych na podstawie danych z formularza
            for entry_form in Formularz.Pola_Własne.entries:
                # Sprawdź, czy oba pola (rodzaj i wartość) są wypełnione
                # id_rodzaj.data jest już intem dzięki coerce=int
                if entry_form.form.id_rodzaj.data and entry_form.form.wartosc.data:
                    Nowe_Pole_Wlasne = PoleWlasne(
                        id_przedmiot=_Przedmiot.id, # Przypisujemy ID przedmiotu
                        id_rodzaj=entry_form.form.id_rodzaj.data,
                        wartosc=entry_form.form.wartosc.data
                    )
                    DB.session.add(Nowe_Pole_Wlasne)
                # Obsłuż przypadek, gdy jedno z pól jest wypełnione, ale drugie nie
                elif entry_form.form.id_rodzaj.data or entry_form.form.wartosc.data:
                    FLASH(f"Pomijam niekompletne pole własne: rodzaj='{entry_form.form.id_rodzaj.data}', wartość='{entry_form.form.wartosc.data}'.", "warning")


            # Zapisanie zmian do bazy danych
            DB.session.commit()
            FLASH("Zmiany zostały zapisane", "success")
            return REDIRECT(URL_FOR("Blueprint_3.Widok_Kolekcja_Moja_Kolekcja"))

        else:
            FLASH("Podano nieprawidłowe dane!", "danger")
            # Jeśli walidacja się nie powiedzie, formularz zostanie ponownie wyrenderowany.
            # Musisz się upewnić, że SelectFieldy w FieldList mają ponownie ustawione choices.
            # Ta pętla na początku bloku POST już to robi.

    # Przekazujemy Select_Pola_Wlasne_Rodzaje_Pozycje do szablonu dla JS
    return RENDER_TEMPLATE("Kolekcja/Przedmiot_Edycja.html", Formularz=Formularz, ID=ID, Select_Pola_Wlasne_Rodzaje_Pozycje=Select_Pola_Wlasne_Rodzaje_Pozycje)

@Blueprint_3.route("/moja-kolekcja/usun/<int:ID>")
@LOGIN_REQUIRED
def Widok_Kolekcja_Usuń():
    return RENDER_TEMPLATE("Kolekcja/Usuń.html")
