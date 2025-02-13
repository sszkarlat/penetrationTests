# Projekt :bomb:

Tematem projektu było przeprowadzenie pełnego testu penetracyjnego na wybranym systemie.

## Etap 1 - planowanie

Celem pierwszego etapu było:

- identyfikacja środowiska testowego;
- opracowanie umowy o testy penetracyjne (ang. _Rules of Engagement_) z klientem (symulowany scenariusz);
- zdefiniowanie zakresu testu, określając, które komponenty infrastruktury będą podlegać testom, a także rodzaje testów (czarna, biała, szara skrzynka);
- opracowanie harmonogramu działań i identyfikacja niezbędnych, wybranych narzędzi, które będą wykorzystywane.

Wynikiem pierwszego etapu mają być między innymi dokument planowania testu penetracyjnego oraz zakresu działania.

## Etap 2 - Rekonesans

Celem drugiego etapu było:

- przeprowadzenie pasywnego rekonesansu przy użyciu otwartych źródeł informacji (OSINT);
- aktywny rekonesans poprzez skanowanie sieci, portów, usług oraz identyfikację systemów operacyjnych;
- wykorzystanie narzędzi Nmap, Whois itp.

Wynikiem było wykonanie części raportu uwzględniającej zebrane informacje o celu.

## Etap 3 - Identyfikacja luk i analiza podatności

Celem trzeciego etapu było:

- identyfikacja podatności przy użyciu narzędzi takich jak Nessus, OpenVAS, Metasploit, Nmap;
- wykonanie szczegółowej analizy wyników skanowania.

Wynikiem tego etapu miało być wykonanie części raportu z uwzględnieniem analizy wyników skanowania wykrytych podatności.

## Etap 4 - Eksploitacja

Celem czwartego etapu było:

- przeprowadzenie eksploitacji wybranych co najmniej dziesięciu podatności przy użyciu takich narzędzi jak Metasploit, Burp Suite (dla aplikacji webowych);
- sprawdzenie możliwości uzyskania dostępu do systemów, eskalacji uprawnień oraz lateralnego poruszania się po sieci w zależności od przyjętych założeń startowych;
- pokazanie, jakie dane lub zasoby mogą zostać uzyskane przez atakującego.

Wynikiem tej części testów penetracyjnych miała być dokumentacja udanych ataków z opisem podatności, metody eksploitacji oraz uzyskanych wyników.

## Etap 5 - Raportowanie i rekomendacje

Celem ostatniego etapu było:

- wykonanie zestawienia podsumowującego wykryte podatności, z wyszczególnieniem poziomu zagrożenia, stosownym opisem oraz propozycją [mitygacji](https://www.ovhcloud.com/pl/security/anti-ddos/ddos-attack-mitigation/);
- opis zaleceń oraz rekomendacji na podstawie przeprowadzonych testów.
