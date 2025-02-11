# Lab 5
Celem piątego laboratorium było wykonanie 3 zadań.

## Czynności wstępne
Do czynności wstępnych zaliczyć należy:
* instalację środowiska testowego DVWA;
* odpowiednie przygotowanie narzędzia BurpSuite w tybie proxy;
* instalacja SQLmap.

## Zadanie 1 - Burp Suite
Wykonanie ataków SQL Injection, XSS oraz Brute Force w środowisku DVWA. Szczegółowa analiza przechwyconych żądań HTTP oraz celem przeprowadzenia skutecznych ataków właściwa ich modyfikacja.

## Zadanie 2 - SQLMap
Użycie SQLMap do automatycznego wykrycia i eksploitacji podatności SQL Injection w DVWA poprzez wprowadzenie odpowiedniego polecenia sqlmap podając adres URL podatnej aplikacji (adres IP maszyny, na której hostowana jest aplikacja DVWA) zidentyfikowanej w Burp Suite, uzyskanie listy dostępnych baz danych na
serwerze oraz wyciągnięcie zawartości tabeli users wraz z hasłami w postaci zahashowanej. 

## Zadanie 3 - Medium DVWA
Powtórzenie czynnności z zadania 2 na poziomie medium. Identyfikacja różnic w odpowiedzi serwera oraz analiza, jakie mechanizmy zostały wprowadzone w celu ograniczenia podatności.