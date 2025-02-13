# Lab 4 :e-mail:

Celem czwartego laboratorium było przeprowadzenie skanowania portów i wykrycia podstawowych podatności na dedykowanych maszynach wirtualnych oraz zrozumienie sposobu działania procesu skanowania. Kolejnym etapem było zrozumienie etapu analizy wykrytych podatności oraz wykorzystanie zdobytej wiedzy w procesie [eksploitacji](https://pl.wiktionary.org/wiki/exploitowanie). Ostatnią krokiem było poznanie „ręcznego” sposobu ataku na sieci komputerowe, jego weryfikacja przy pomocy oprogramowania [Wireshark](https://pl.wikipedia.org/wiki/Wireshark), a także przeprowadzenie prostej i skutecznej [kampanii phishingowej](https://exatel.pl/uslugi/cyberbezpieczenstwo/phishing/).

## Zadanie 1 - [Nmap](https://www.kali.org/tools/nmap/)

Skanowanie portów na dwóch uprzednio do tego przygotowanych maszynach z Linuxem oraz Windowsem. Dodatkowo skanowanie

## Zadanie 2 - [OpenVAS](https://www.openvas.org), [Nessus](<https://en.wikipedia.org/wiki/Nessus_(software)>)

Skanowanie maszyn pod kątem znalezienia wszelkich podatności przy wykorzystaniu narzędzi OpenVAS lub Nessus. Dodatkowo należało zidentyfikować znalezione podatności oraz sprawdzić ich CVE.

## Zadanie 3 - Szukanie podatności

Wyszukanie podatności dla urządzeń typu firewall firmy CheckPoint lub Cisco lub PaloAlto w 2024 roku. Ocena znalezionych podatności w oparciu o CVSS.

## Zadanie 4 - Active Directory

Analiza podatności usługi katalogowej Active Directory (Microsoft), które znajdują się w [bazie MITRE](https://attack.mitre.org) i które zostały oznaczone numerem CVE w 2024 roku. Przygotowanie rekomendacji dla organizacji chcącej wdrożyć AD w sieci, która nie posiada połączenia z publiczną siecią Internet.

## Zadanie 5 - Metasploit

Użycie narzędzia [Metasploit](https://docs.metasploit.com) do przeprowadzenia procesu eksploitacji z wykorzystaniem podatności na usługę SMB. Jako efekt uzyskania dostępu do zaatakowanej maszyny należało wykonać wybrane komendy dostępne w [Meterpreter]().

## Zadanie 6 - MiTM, ARP Spoofing

Przeprowadzenie ataku [MiTM](https://pl.wikipedia.org/wiki/Atak_man_in_the_middle) przy pomocy metody [ARP Spoofing](https://pl.wikipedia.org/wiki/ARP_spoofing) we własnym środowisku lokalnym. Wykonanie procedury [DNS Cache Poisoning](https://pl.wikipedia.org/wiki/Zatruwanie_DNS), która w efekcie zamiast konkretnego adresu witryny (np. www.onet.pl) wyświetlić miała dowolną nieprawdziwą stronę.

## Zadanie 7 - Kampania Phishingowa

Przeprowadzenie kampanii phishingowej przy pomocy narzędzia [Gophish](https://getgophish.com). W raporcie zawarto zarówno:

- darmowy hosting realizowany w oparciu o stronę [cba.pl](https://www.cba.pl);
- lokalny hosting przy pomocy serwera Apache na jednej z maszyn wirtualnych

Celem zadania było:

- wysłanie maila z linkiem do ofiary;
- wyświetlenie po stronie ofiary fałszywej strony logowania;
- zebranie w danych logowania wykorzystywanych w procesie uwierzytelniania.
