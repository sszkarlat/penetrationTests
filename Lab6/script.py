from extensions import *
from modules import shared
from modules.callbacks import Iteratorize
from modules.text_generation import encode, generate_reply
import requests

params = {
    "display_name": "ZAP Scanner",
    "is_tab": False,
}

def custom_generate_chat_prompt(user_input, state, **kwargs):
    print("[ZAP Scanner] Otrzymano wiadomość:", user_input)
    return user_input

def input_modifier(string, state):
    print("[ZAP Scanner] Przetwarzam wejście:", string)
    return string

def output_modifier(string, state):
    """Modyfikator wyjścia - sprawdza czy jest komenda do skanowania"""
    print("[ZAP Scanner] Przetwarzam wyjście:", string)
    
    lower_string = string.lower()
    trigger_phrases = [
        "zeskanuj stronę",
        "skanuj stronę",
        "skanuj aplikację",
        "zeskanuj aplikację webową",
        "skanuj aplikację webową",
        "rozpocznij skanowanie"
    ]
    
    if any(phrase in lower_string for phrase in trigger_phrases):
        print("[ZAP Scanner] Wykryto komendę skanowania!")
        # Spróbuj znaleźć URL w tekście
        words = string.split()
        url = None
        for word in words:
            if word.startswith(('http://', 'https://')):
                url = word
                break
        
        if not url:
            url = "http://192.168.1.173/DVWA/vulnerabilities/sqli"
            
        print(f"[ZAP Scanner] Próba skanowania URL: {url}")
            
        try:
            # Wywołanie API skanera
            print(f"[ZAP Scanner] Wysyłam żądanie do API Flask...")
            response = requests.post(
                'http://localhost:5000/api/skanuj',
                json={'url': url},
                headers={'Content-Type': 'application/json'},
                timeout=5
            )
            
            print(f"[ZAP Scanner] Otrzymano odpowiedź: {response.status_code}")
            
            if response.status_code == 200:
                scan_result = (
                    f"\n\n[System] Rozpoczęto skanowanie dla URL: {url}\n"
                    f"Status: Skanowanie w toku\n"
                    f"Raport będzie dostępny w pliku: {response.json().get('raport', 'report.html')}\n"
                    f"Możesz monitorować postęp w konsoli, gdzie uruchomiony jest skrypt Flask."
                )
                return string + scan_result
            else:
                error_msg = (
                    f"\n\n[System] Błąd podczas skanowania: "
                    f"{response.json().get('error', 'Nieznany błąd')}\n"
                    f"Kod błędu: {response.status_code}"
                )
                return string + error_msg
                
        except requests.exceptions.RequestException as e:
            print(f"[ZAP Scanner] Błąd połączenia: {str(e)}")
            error_details = (
                f"\n\n[System] Błąd połączenia ze skanerem: {str(e)}\n"
                f"Upewnij się, że:\n"
                f"1. Serwer Flask działa na porcie 5000\n"
                f"2. OWASP ZAP jest uruchomiony na porcie 8081\n"
                f"3. Ścieżki i porty są prawidłowo skonfigurowane"
            )
            return string + error_details
    
    return string

def bot_prefix_modifier(string, state):
    return string

def register_extension():
    shared.input_hooks.append(input_modifier)
    shared.output_hooks.append(output_modifier)
    shared.bot_prefix_hooks.append(bot_prefix_modifier)

register_extension()
