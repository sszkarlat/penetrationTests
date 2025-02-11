# Lab 4
Celem czwartego laboratorium jest przeprowadzenie skanowania portów i wykrycia podstawowych podatności na dedykowanych maszynach wirtualnych oraz zrozumienie sposobu działania procesu skanowania. Kolejnym etapem jest zrozumienie etapu analizy wykrytych podatności oraz wykorzystanie tej wiedzy w procesie eksploitacji. Ostatnią kwestią jest poznanie „ręcznego” sposobu ataku na sieci komputerowe, jego weryfikacja przy pomocy oprogramowania Wireshark, a także przeprowadzenie prostej i skutecznej kampanii phishingowej.

## Zadanie 1 - Nmap
Skanowanie portów na dwóch uprzednio do tego przygotowanych maszynach z Linuxem oraz Windowsem. Dodatkowo skanowanie 

## Zadanie 2 - OpenVAS, Nessus
Skanowanie maszyn pod kątem znalezienia wszelkich podatności przy wykorzystaniu narzędzi OpenVAS lub Nessus. Dodatkowo należało zidentyfikować znalezione podatności oraz sprawdzić ich CVE.

## Zadanie 3 - Szukanie podatności
Wyszukanie podatności dla urządzeń typu firewall firmy CheckPoint lub Cisco lub PaloAlto w 2024 roku. Ocena znalezionych podatności w oparciu o CVSS.

## Zadanie 4 - Active Directory
Analiza podatności usługi katalogowej Active Directory (Microsoft), które znajdują
się w bazie MITRE i które zostały oznaczone numerem CVE w 2024 roku. Przygotowanie rekomendacji dla organizacji chcącej
wdrożyć AD w sieci, która nie posiada połączenia z publiczną siecią Internet.

## Zadanie 5 - Metasploit
Użycie narzędzia Metasploit do przeprowadzenia procesu exploitacji z wykorzystaniem podatności na usługę SMB. Jako efekt uzyskania dostępu do zaatakowanej maszyny należało wykonać wybrane komendy dostępne w Meterpreter.

## Zadanie 6 - MiTM, ARP Spoofing
Przeprowadzenie ataku MiTM przy pomocy metody ARP Spoofing we własnym środowisku lokalnym. Wykonanie procedury DNS Cache Poisoning, która w efekcie zamiast konkretnego adresu witryny (np. www.onet.pl) wyświetlić miała dowolną nieprawdziwą stronę. 

## Zadanie 7 - Kampania Phishingowa
Przeprowadzenie kampanii phishingowej przy pomocy narzędzia Gophish. W raporcie zawarto zarówno:
* darmowy hosting realizowany w oparciu o stronę cba.pl;
* lokalny hosting przy pomocy serwera Apache na jednej z maszyn wirtualnych

Celem zadania było:
* wysłanie maila z linkiem do ofiary;
* wyświetlenie po stronie ofiary fałszywej strony logowania;
* zebranie w danych logowania wykorzystywanych w procesie uwierzytelniania.