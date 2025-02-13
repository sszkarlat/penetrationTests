# Lab 6 :zap:

Laboratorium 6 zostało podzielone na trzy zadania.

## Zadanie 1

Instalacja narzędzia [OWASP ZAP](https://www.zaproxy.org) i test procesu logowania na wybranej witrynie internetowej ze szczegółowym wyjaśnieniem wszystkich elementów Request’a.

## Zadanie 2

Utworzenie skryptu w języku Python ([biblioteka zapv2](https://www.zaproxy.org/docs/api/)) przeprowadzającego automatyczny skan podatności DVWA/sqli pod kątem SQL Injection oraz generowanie raportu w formacie html przy pomocy narzędzia ZAP. Do konfiguracji ZAP należało wygenerować klucz API, z kolei kod musiał zostać podzielony na dwie funkcje: skanowanie oraz analiza_wynikow.

## Zadanie 3

Przystosowanie narzędzia open-webui z wykorzystaniem modelu językowego AI - llama3.1:8b, do uruchomienia skryptu z Zadania 2 np. po wprowadzeniu przez użytkownika wyrażenia: _skanuj aplikację webową lub \_skanuj aplikację webową <parametr>_, gdzie parametrem jest przekazany do skryptu adres URL.
