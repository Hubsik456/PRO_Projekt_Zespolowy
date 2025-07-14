//! Eventy
window.addEventListener("DOMContentLoaded", function()
{
    console.log("Tryb Ciemny:", Ciasteczko_Czytaj("Tryb_Ciemny"));
    console.log("Podkreślanie Linków:", Ciasteczko_Czytaj("Podkreślanie_Linków"));

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

    console.log("WIP", Ciasteczko_Czytaj("Tryb_Ciemny"));

    if (Ciasteczko_Czytaj("Tryb_Ciemny") == "1")
    {
        Bootstrap_Tryb_Ciemny();
        console.log("Włacznie trybu ciemnego.");
    }
    else
    {
        console.log("NIE Włączenie trybu ciemnego.");
    }
}

function Podkreślanie_Linków() // TODO: Do naprawienia
{
    let Linki = document.querySelectorAll("a, button, input[type='button'], input[type='submit'], input[type='reset']");

    //console.log(Linki);

    if (Ciasteczko_Czytaj("Podkreślanie_Linków") == "1")
    {
        console.log("Wyłączono podkreślanie linków");

        Ciasteczko_Zapisz("Podkreślanie_Linków", 0, 30);
        Linki.forEach(x => x.classList.remove("Podkreślenie_Linku"));
    }
    else
    {
        console.log("Włączenie podkreślanie linków");

        Ciasteczko_Zapisz("Podkreślanie_Linków", 1, 30);
        Linki.forEach(x => x.classList.add("Podkreślenie_Linku"));
    }

    console.log("Ciasteczko:", Ciasteczko_Czytaj("Podkreślanie_Linków"));
}

function Podkreślanie_Linków_Ciasteczko()
{
    /* Automatyczne podkreślenie linków i przycisków kiedy ciasteczko ma odpowiednią wartość. */

    if (Ciasteczko_Czytaj("Podkreślanie_Linków", 1) == "1")
    {
        Podkreślanie_Linków();
    }
}

//! Funkcje Pomocnicze
function Ciasteczko_Zapisz(Nazwa, Wartość, Dni)
{
    var Expires = "";
    var Data_Wygaśnięcia = new Date();

    Data_Wygaśnięcia.setTime(Data_Wygaśnięcia.getTime() + (Dni * 24 * 3600 * 1000));
    Expires = `; expires=${Data_Wygaśnięcia.toUTCString()}`;

    document.cookie = `${Nazwa}=${Wartość} ${Expires}; path=/`;

    //console.log(`Zapisano ciasteczko '${Nazwa}' = '${Wartość}'`)
}

function Ciasteczko_Czytaj(Nazwa)
{
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
    document.cookie = `${Nazwa}=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;`;
}