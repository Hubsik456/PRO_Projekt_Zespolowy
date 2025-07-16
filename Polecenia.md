# **Polecenia**

Poniżej znajdują się polecenia terminalowe, które pomogą Ci podczas pracy z tym projektem. Zwróc szczególną uwagę na to w jakich lokalizacjach są wywoływane te polecenia.

Przetestowane w MS Power Shell.

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

v1 - Nie działa

`PS D:\Python - Flask\PRO_Projekt_Zespolowy\Tłumaczenia> pybabel.exe extract -F .\Babel.cfg -k _l -o Tłumaczenia.pot ..\Flask_Aplikacja\` - Wygenerowanie pliku szablonu tłumaczeń. Ten plik będzie wykorzystywany przez następne polecnie. **Nie edytować tego pliku.**

`PS D:\Python - Flask\PRO_Projekt_Zespolowy\Tłumaczenia> pybabel.exe init -i .\Tłumaczenia.pot -d . -l en` - Wygenerowanie pliku który trzeba ręcznie przetłumaczyć. Wygenerowane na podstawie pliku `Tłumaczenia.pot` z poprzedniego polecenia. **To polecenie służy do generowania tłumaczeń dla danego język, tylko za pierwszym razem.** Do aktualizacji pliku z tłumaczeniami o dodane w międzyczasie `_("...")` i `_l("...")` służy poniższe polecenie.

`PS D:\Python - Flask\PRO_Projekt_Zespolowy\Tłumaczenia> pybabel.exe update -i .\Tłumaczenia.pot -d .` - Aktualizacja plików z tłumaczeniami. **To polecenie służy do aktualizacji tłumaczeń, kiedy już jakie istnieją**. Wtedy pojawią się w nim dodane w międzyczacie `_("...")` i `_l("...")`.

---

v2 - Też nie działa

`PS D:\Python - Flask\PRO_Projekt_Zespolowy> pybabel.exe extract -F .\Babel.cfg -k _l -o messages.pot .`

`PS D:\Python - Flask\PRO_Projekt_Zespolowy> pybabel.exe init -i .\messages.pot -d translations -l en`

`PS D:\Python - Flask\PRO_Projekt_Zespolowy> pybabel.exe compile -d .\translations\`

---

v3 - Też nie działa

`PS D:\Python - Flask\PRO_Projekt_Zespolowy> pybabel extract -F babel.cfg -k _l -o messages.pot .`

`PS D:\Python - Flask\PRO_Projekt_Zespolowy> pybabel init -i messages.pot -d Flask_Aplikacja/translations -l en`

`pybabel compile -d Flask_Aplikacja/translations`
