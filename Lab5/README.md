# Lab 5 :sunrise_over_mountains:

Celem piątego laboratorium było wykonanie 3 zadań.

## Czynności wstępne

Do czynności wstępnych zaliczyć należy:

- instalację środowiska testowego [DVWA](https://github.com/digininja/DVWA);
- odpowiednie przygotowanie narzędzia BurpSuite w trybie proxy;
- instalacja [SQLMap](https://www.kali.org/tools/sqlmap/).

## Zadanie 1 - Burp Suite

Wykonanie ataków [SQL Injection](https://www.w3schools.com/sql/sql_injection.asp), [XSS](https://sekurak.pl/kilka-slow-o-podatnosci-xss-oraz-polyglot-xss/) oraz [Brute Force](https://pl.wikipedia.org/wiki/Atak_brute_force) w środowisku DVWA. Szczegółowa analiza przechwyconych żądań HTTP oraz celem przeprowadzenia skutecznych ataków właściwa ich modyfikacja.

## Zadanie 2 - SQLMap

Użycie SQLMap do automatycznego wykrycia i eksploitacji podatności SQL Injection w DVWA poprzez wprowadzenie odpowiedniego polecenia SQLMap podając adres URL podatnej aplikacji (adres IP maszyny, na której hostowana jest aplikacja DVWA) zidentyfikowanej w Burp Suite, uzyskanie listy dostępnych baz danych na serwerze oraz wyciągnięcie zawartości tabeli users wraz z hasłami w postaci hashy.

## Zadanie 3 - Medium DVWA

Powtórzenie czynności z zadania 2 na poziomie medium. Identyfikacja różnic w odpowiedzi serwera oraz analiza, jakie mechanizmy zostały wprowadzone w celu ograniczenia podatności.
