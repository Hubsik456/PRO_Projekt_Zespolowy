# Dokumentacja Projektu Zespołowego: Cyfrowy Kurator Kolekcji

## 1. Autorzy i Podział Zadań

**Skład grupy:**

- Hubert Michna (w67259)
- Patryk Pieniążek (w67174)

| Zadanie / Obszar                  | Odpowiedzialna osoba(y) |
| --------------------------------- | ----------------------- |
| Backend (Logika aplikacji, API)   | [Wpisz imię/imiona]     |
| Frontend (Interfejs użytkownika)  | [Wpisz imię/imiona]     |
| Baza danych (Projekt i zarządzanie) | [Wpisz imię/imiona]     |
| Dokumentacja techniczna i UML     | [Wpisz imię/imiona]     |
| Testowanie                        | [Wpisz imię/imiona]     |

---

## 2. Cel i Zakres Projektu

**Temat**: 3.5. Cyfrowy kurator kolekcji

**Cel**: Stworzenie elastycznej aplikacji webowej do kompleksowego zarządzania dowolnym typem osobistych kolekcji. Aplikacja ma umożliwiać użytkownikom śledzenie przedmiotów, dodawanie szczegółowych informacji, zdjęć oraz potencjalnie monitorowanie ich wartości rynkowej.

**Zakres podstawowy**:

- Możliwość definiowania własnych typów kolekcji i ich pól.
- Szczegółowy opis przedmiotów (rok, stan, cena zakupu, lokalizacja, notatki).
- Zarządzanie multimediami (dodawanie wielu zdjęć/skanów do każdego przedmiotu).
- Tworzenie "list życzeń" z brakującymi elementami.
- Podstawowe raportowanie, sortowanie i filtrowanie.

**Propozycje rozwinięcia (Stretch goals)**:

- Integracja z zewnętrznymi serwisami (np. Allegro, eBay) w celu śledzenia orientacyjnych cen rynkowych.
- Opcje społecznościowe (udostępnianie kolekcji).
- Zaawansowane raporty i statystyki.
- Eksport/import danych do formatu CSV.

---

## 3. Specyfikacja Wymagań

### 3.1. Wymagania Funkcjonalne

- **Zarządzanie użytkownikiem**: Rejestracja, logowanie, zarządzanie profilem.
- **Zarządzanie kolekcjami**: Tworzenie, edycja, usuwanie kolekcji. Użytkownik może definiować własne szablony kolekcji z niestandardowymi polami.
- **Zarządzanie przedmiotami**: Dodawanie, edycja, usuwanie przedmiotów w ramach kolekcji.
- **Wyszukiwanie i filtrowanie**: Zaawansowane wyszukiwanie przedmiotów po różnych kryteriach.
- **Multimedia**: Upload i przeglądanie wielu zdjęć dla każdego przedmiotu.
- *... (dodaj więcej w miarę rozwoju projektu)*

### 3.2. Wymagania Niefunkcjonalne

- **Wydajność**: Aplikacja powinna odpowiadać na żądania użytkownika w czasie nie dłuższym niż 2 sekundy.
- **Bezpieczeństwo**: Hasła użytkowników muszą być hashowane. Należy zabezpieczyć aplikację przed podstawowymi atakami (np. XSS, SQL Injection).
- **Użyteczność**: Interfejs powinien być intuicyjny i łatwy w obsłudze dla nowego użytkownika.
- **Skalowalność**: Architektura powinna pozwalać na łatwe dodawanie nowych funkcji w przyszłości.

### 3.3. Ograniczenia

- **Czas**: Projekt realizowany w ramach semestru (Maj-Lipiec 2025).
- **Technologia**: Projekt oparty o uzgodniony stos technologiczny (Python/Flask, ...).
- **Zasoby**: Projekt tworzony przez dwuosobowy zespół.

---

## 4. Architektura i Technologie

### 4.1. Architektura Systemu

Aplikacja została zaprojektowana w architekturze Klient-Serwer.

- **Backend**: Aplikacja napisana w języku Python z wykorzystaniem frameworka Flask, odpowiedzialna za logikę biznesową, obsługę API (REST) oraz komunikację z bazą danych.
- **Frontend**: Interfejs użytkownika stworzony przy użyciu [np. React, Vue, lub szablony Jinja2], komunikujący się z backendem poprzez API.
- **Baza danych**: System zarządzania bazą danych [np. PostgreSQL, SQLite] do przechowywania danych o użytkownikach, kolekcjach i przedmiotach.

### 4.2. Stos Technologiczny

- **Język programowania**: Python 3.x
- **Framework backendowy**: Flask
- **Baza danych**: [np. PostgreSQL] z ORM SQLAlchemy
- **Framework frontendowy**: [np. React / Vue / Jinja2]
- **Serwer**: [np. Gunicorn, Waitress]
- **Inne narzędzia**: Sphinx (do generowania dokumentacji), PyBabel (do tłumaczeń).

---

## 5. Dokumentacja UML

*W tej sekcji umieść wygenerowane diagramy, np. jako obrazy.*

### 5.1. Diagram Przypadków Użycia

![Use Case Diagram](sciezka/do/diagramu_przypadkow_uzycia.png)

### 5.2. Diagram Klas

![Class Diagram](sciezka/do/diagramu_klas.png)

### 5.3. Diagram Aktywności (przykładowy proces)

![Activity Diagram](sciezka/do/diagramu_aktywnosci.png)

---

## 6. Struktura Kodu i Dokumentacja Automatyczna

Struktura katalogów projektu jest następująca:

```
/PRO_Projekt_Zespolowy
├── /Flask_Aplikacja      # Główny kod aplikacji Flask
├── /Dokumentacja         # Pliki źródłowe i konfiguracja Sphinx
│   ├── /build            # Wygenerowana dokumentacja HTML
│   └── ...
├── /tests                # Testy jednostkowe i integracyjne
└── ...                   # Inne pliki konfiguracyjne
```

Dokumentacja kodu została wygenerowana automatycznie na podstawie docstringów przy użyciu narzędzia **Sphinx**.

**Aby wygenerować dokumentację:**

```bash
.\Dokumentacja\make.bat html
```

Wygenerowana strona główna dokumentacji znajduje się w pliku: `Dokumentacja/build/html/index.html`.

---

## 7. Prezentacja Implementacji

*W tej sekcji umieść zrzuty ekranu, GIFy lub krótkie wideo prezentujące działanie kluczowych funkcjonalności aplikacji.*

**Ekran główny:**
!Ekran główny

**Widok kolekcji:**
!Widok kolekcji

---

## 8. Testowanie

W projekcie zastosowano [np. testy jednostkowe]. Do ich uruchomienia służy biblioteka `pytest`.

**Przykładowy test:**

```python
# Wklej tutaj przykład testu
```

---

## 9. Podsumowanie i Wnioski

W ramach projektu udało się zrealizować następujące cele: [...]

Napotkane problemy i wyzwania: [...]

Możliwości dalszego rozwoju: [...]
