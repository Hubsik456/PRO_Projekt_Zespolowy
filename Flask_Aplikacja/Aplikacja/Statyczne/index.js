//! Eventy
window.addEventListener("DOMContentLoaded", function()
{
    //console.log("Tryb Ciemny:", Ciasteczko_Czytaj("Tryb_Ciemny"));
    //console.log("Podkreślanie Linków:", Ciasteczko_Czytaj("Podkreslanie_Linkow"));

    Włączenie_Tooltipów_Bootstrap();
    Bootstrap_Tryb_Ciemny_Ciasteczko();
    Podkreślanie_Linków_Ciasteczko();

    window.addEventListener("scroll", Strzałka_Scroll_Przycisk);
});

//! Funkcje
function Włączenie_Tooltipów_Bootstrap()
{
    /* Włącznie tooltipów z Bootstrap 5, źródło: https://getbootstrap.com/docs/5.3/components/tooltips/#enable-tooltips. W przypadku button[data-bs-toggle="button"] bootstrap błędnie wyświetla console.error() */

    tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"], [title]')

    //console.log(tooltipTriggerList);

    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    //console.log(tooltipList);
}

function Strzałka_Scroll_Przycisk()
{
    /* Wyświetlanie/ukrywanie przycisku który po kliknięciu przewija stronę do samej góry. */

    if (document.documentElement.scrollTop > 50)
    {
        document.querySelector("#Przycisk_Scroll").style.display = "initial";
    }
    else
    {
        document.querySelector("#Przycisk_Scroll").style.display = "none";
    }

}

function Formularz_Wyświetlanie_Hasła(Selektor)
{
    /* Wyświetla zawartość pola z hasłem w formularzach. */

    var Pole = document.querySelector(Selektor);

    if (Pole.type === "password")
    {
        Pole.type = "text";
    }
    else
    {
        Pole.type = "password";
    }
}

function Strzałka_Scroll()
{
    /* Przewinięcie strony do samej góry. */

    document.documentElement.scrollTop = 0;
}

function Bootstrap_Tryb_Ciemny() // TODO: Do naprawienia
{
    /* Włączanie/Wyłączanie trybu ciemnego poprzez atrybut "data-bs-theme" znacznika "HTML" i ustawienie odpowiedniego ciasteczka. */

    var Tag_HMTL = document.querySelector("html")

    if (!Tag_HMTL.hasAttribute("data-bs-theme") || Tag_HMTL.getAttribute("data-bs-theme") == "light") // Ustawienie trybu ciemnego
    {
        Ciasteczko_Zapisz("Tryb_Ciemny", 1, 30);
        Tag_HMTL.setAttribute("data-bs-theme", "dark");
    }
    else // Ustawienie tryby jasnego
    {
        Ciasteczko_Zapisz("Tryb_Ciemny", 0, 30);
        Tag_HMTL.setAttribute("data-bs-theme", "light");
    }
}

function Bootstrap_Tryb_Ciemny_Ciasteczko()
{
    /* Automatycznie włączanie trybu ciemnego kiedy ciasteczko ma odpowiednią wartość. */

    //console.log("WIP", Ciasteczko_Czytaj("Tryb_Ciemny"));

    if (Ciasteczko_Czytaj("Tryb_Ciemny") == "1")
    {
        Bootstrap_Tryb_Ciemny();
        //console.log("Włacznie trybu ciemnego.");
    }
    else
    {
        //console.log("NIE Włączenie trybu ciemnego.");
    }
}

function Podkreślanie_Linków() // TODO: Do przerobienia
{
    let Linki = document.querySelectorAll("a, button, input[type='button'], input[type='submit'], input[type='reset']");

    //console.log(Linki);

    if (Ciasteczko_Czytaj("Podkreslanie_Linkow") == "1")
    {
        //console.log("Wyłączono podkreślanie linków");

        Ciasteczko_Zapisz("Podkreslanie_Linkow", 0, 30);
        Linki.forEach(x => x.classList.remove("Podkreślenie_Linku"));
    }
    else
    {
        //console.log("Włączenie podkreślanie linków");

        Ciasteczko_Zapisz("Podkreslanie_Linkow", 1, 30);
        Linki.forEach(x => x.classList.add("Podkreślenie_Linku"));
    }

    //console.log("Ciasteczko:", Ciasteczko_Czytaj("Podkreslanie_Linkow"));
}

function Podkreślanie_Linków_Ciasteczko()
{
    /* Automatyczne podkreślenie linków i przycisków kiedy ciasteczko ma odpowiednią wartość. */

    if (Ciasteczko_Czytaj("Podkreslanie_Linkow", 1) == "1")
    {
        Podkreślanie_Linków();
    }
}

//! Funkcje Pomocnicze
function Ciasteczko_Zapisz(Nazwa, Wartość, Dni)
{
    /* Zapisanie ciasteczka ciasteczka, jeśli takie ciasteczko nie istnieje to zostanie utworzone. */

    var Expires = "";
    var Data_Wygaśnięcia = new Date();

    Data_Wygaśnięcia.setTime(Data_Wygaśnięcia.getTime() + (Dni * 24 * 3600 * 1000));
    Expires = `; expires=${Data_Wygaśnięcia.toUTCString()}`;

    document.cookie = `${Nazwa}=${Wartość} ${Expires}; path=/`;
}

function Ciasteczko_Czytaj(Nazwa)
{
    /* Odczytanie i zwrócenie wartości ciasteczka. */

    var Ciasteczka = document.cookie.split(";");

    for (let x = 0; x < Ciasteczka.length; x++)
    {
        var Ciasteczko = Ciasteczka[x];

        while (Ciasteczko.charAt(0) === " ")
        {
            Ciasteczko = Ciasteczko.substring(1);
        }

        if (Ciasteczko.indexOf(`${Nazwa}=`) === 0)
        {
            return Ciasteczko.substring(`${Nazwa}=`.length, Ciasteczko.length); // Jeśli ciasteczko istnieje
        }
    }

    return null; // Jeśli ciasteczko nie istnieje
}

function Ciasateczko_Usuń(Nazwa)
{
    /* Usunięcie ciasteczka. */

    document.cookie = `${Nazwa}=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}

function Formularz_Dodaj_Pole_Własne()
{
    /*
        Dodanie nowego pola własnego do formularza. Wymaga przerobienia aby mogło byś stosowane w większej ilości przypadków.
        Źródło: https://blog.miguelgrinberg.com/post/dynamic-forms-with-flask
    */

    const Pierwsze_Pole_Własne = document.querySelector('.Pole_Własne');
    const Nowe_Pole_Własne = document.createElement('div');

    Nowe_Pole_Własne.classList.add('mb-3');
    Nowe_Pole_Własne.classList.add('p-2');
    Nowe_Pole_Własne.classList.add('Pole_Własne');
    Nowe_Pole_Własne.innerHTML = Pierwsze_Pole_Własne.innerHTML;

    const Nowe_ID = document.querySelectorAll('.Pole_Własne').length;
    const Pole_Select = Nowe_Pole_Własne.querySelector('#Pola_Własne-0-id_rodzaj');

    Pole_Select.id = `Pola_Własne-${Nowe_ID}-id_rodzaj`;
    Pole_Select.name = Pole_Select.id;
    Pole_Select.value = "1";

    const Pole_Input = Nowe_Pole_Własne.querySelector('#Pola_Własne-0-wartosc');

    Pole_Input.id = `Pola_Własne-${Nowe_ID}-wartosc`;
    Pole_Input.name = Pole_Input.id;
    Pole_Input.value = "";

    document.getElementById('Pola_Własne').appendChild(Nowe_Pole_Własne);
    document.querySelector('.Pole_Własne:last-child input').focus();
}

function Formularz_Usuń_Pole_Własne(Pole_Własne)
{
    /* "Usuwa" podane pole własne. W obecnej wersji, usuwnie polega na ukryciu pola i wstawieniu wartości null w jego polach. W przyszłosci można przerobić tę funkcję, tak aby faktycznie usuwała pola. */
    Pole_Własne.classList.add("d-none");

    Pole_Input = Pole_Własne.querySelector("input");
    Pole_Input.value = "";
}