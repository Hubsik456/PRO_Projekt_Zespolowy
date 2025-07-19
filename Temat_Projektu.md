# PRO Projekt Zespołowy

**Temat**: 3.5. Cyfrowy kurator kolekcji

**Zakres podstawowy**: Narzędzie (mobilne/webowe) do śledzenia przedmiotów w kolekcji (cena, rok, stan, lokalizacja). Przykład: pocztówki z Rzeszowa.

**Propozycja rozwinięcia**:

- **Cel**: Stworzenie elastycznej i bogatej w funkcje aplikacji (webowej lub mobilnej) do kompleksowego zarządzania dowolnym typem osobistych kolekcji, z możliwością dodawania szczegółowych informacji, zdjęć i potencjalnie śledzenia wartości rynkowej.
- **Kluczowe funkcjonalności**:
  - **Elastyczność typów kolekcji**: Możliwość zdefiniowania przez użytkownika własnego typu kolekcji (np. monety, znaczki, książki, płyty winylowe, figurki, sztuka, zegarki, gry wideo) i dostosowania pól opisujących przedmioty (np. dla książki: autor, wydawnictwo, ISBN; dla monety: mennica, stop metalu; dla pocztówki: wydawca, temat, obieg). Zachowanie przykładu pocztówek z Rzeszowa jako demonstracji lokalnego kontekstu.
  - **Szczegółowy opis przedmiotu**: Poza podstawowymi danymi (rok, stan, cena zakupu, lokalizacja przechowywania), dodanie pól na: szczegółowy opis, historię przedmiotu (provenance), notatki osobiste, tagi/słowa kluczowe.
  - **Zarządzanie multimediami**: Kluczowa funkcja: możliwość dodawania wielu zdjęć lub skanów dla każdego przedmiotu, ich przeglądanie i zarządzanie.
  - **Śledzenie wartości (zadanie dla liderów)**:
    - **Podstawowe**: Ręczne wprowadzanie ceny zakupu i szacowanej wartości bieżącej.
    - **Zaawansowane** (trudne, jako "stretch goal"): Próba integracji z popularnymi platformami aukcyjnymi/sprzedażowymi (np. Allegro, eBay, specjalistyczne portale kolekcjonerskie) w celu wyszukiwania po- dobnych przedmiotów i prezentowania orientacyjnych cen rynkowych (wymagałoby to prawdopodobnie web scrapingu lub korzystania z API, jeśli dostępne, z uwzględnieniem kwestii etycznych i technicznych - należy to wyraźnie zaznaczyć jako trudne i opcjonalne).
  - **Funkcje dodatkowe**: Tworzenie "list życzeń" (brakujące elementy kolekcji), generowanie raportów (np. wartość kolekcji, rozkład roczników), opcje sortowania i filtrowania, eksport/import danych (np. CSV dla bezpieczeństwa).
  - **Opcjonalnie (społeczność)**: Możliwość (kontrolowanego przez użytkownika) udostępniania wybranych elementów kolekcji znajomym lub publicznie.
- **Proponowane technologie**:
  - **Web**: Frontend (React, Angular, Vue), Backend (Python/Django/Flask, Node.js/Express, PHP/Symfony/Laravel, Java/Spring), Baza danych (np. PostgreSQL – dobrze radzi sobie ze strukturą i relacjami, które tu wystąpią).
  - **Mobile**: React Native, Flutter lub natywnie (Swift/Kotlin).
  - **Przechowywanie Plików**: Usługi typu Cloud Storage (AWS S3, Google Cloud Storage, Azure Blob Storage) do przechowywania zdjęć/skanów.
  - **Potencjalnie**: Biblioteki do web scrapingu (jeśli realizowana będzie zaawansowana funkcja śledzenia wartości, np. BeautifulSoup, Scrapy w Pythonie). O Aspekty pracy zespołowej: Projektowanie solidnej struktury bazy danych będzie kluczowe. Podział ról: Frontend (UI/UX, interakcja z użytkownikiem), Backend (logika biznesowa, API, zarządzanie bazą danych i plikami), potencjalnie Mobile, research i integracja zewnętrznych danych (dla śledzenia wartości), testowanie (funkcjonalne, użyteczności, bezpieczeństwa)
