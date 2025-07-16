# **Polecenia**

Poniżej znajdują się polecenia terminalowe, które pomogą Ci podczas pracy z tym projektem.

## **Dokumentacja**

Wygenerowanie dokumentacji:

`PS PRO_Projekt_Zespołowy_v2> .\Dokumentacja\make.bat html` - Generuje dokumentację w formie osobnych plików .html.

`PS PRO_Projekt_Zespołowy_v2> .\Dokumentacja\make.bat singlehtml` - Generuje dokumentację w formie jednego pliku .html.

Wygenerowana dokumentacja bedzie się znajdowała w `Dokumentacja\build\...`, gdzie `...` to typ dokumentacji jaki został wygenerowany.

## **Uruchamianie Projektu**

WIP

## **Baza Danych**


WIP

## **Tłumaczenie**

WIP

`pybabel.exe extract -F Aplikacja/babel.cfg -k _l -o Aplikacja/Tłumaczenia.pot .` - Wygenerowanie pliku  szablonem pod pliki z tłumaczeniami na poszczególne języki. Tutaj się nie dodaje tłumaczeń. Aby zaktualizować listę teskstów do przetłumaczenia trzeba najpierw wywołać to polecenie a potem `pybabel.exe update`.

`pybabel.exe init -i Aplikacja/Tłumaczenia.pot -d Aplikacja/Tłumaczenia -l en` - Wygenerowanie **nowego** pliku z tekstami do przetłumaczenia dla danego języka, tutaj "en".

`pybabel.exe update -i messages.pot -d translations` - Zaktualizowanie pliku z tekstami do przetłumaczenia.

`pybabel.exe compile -d .\Aplikacja\translations\` - Kompilowanie tłumaczeń.
