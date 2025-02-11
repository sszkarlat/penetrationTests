import time
from flask import Flask, request, jsonify
from zapv2 import ZAPv2

app = Flask(__name__)

def skanowanie(zap, target_url, target, context_name, scan_policy_name):
    core = zap.core
    context = zap.context
    ascan = zap.ascan

    # Nowa sesja
    core.new_session('DVWA_session', overwrite=True)

    # Nowy kontekst
    context_id = context.new_context(contextname=context_name)

    # Konfiguracja kontekstu
    context.include_in_context(context_name, target_url + '/vulnerabilities.*')

    exclude_patterns = [
        '/login.php', '/logout.php', '/setup.php', '/security.php',
        '/instructions.php', '/phpinfo.php', '/about.php'
    ]

    for pattern in exclude_patterns:
        context.exclude_from_context(context_name, f'\\Q{target_url}{pattern}\\E')
    
    # Spider
    core.access_url(url=target, followredirects=True)
    time.sleep(2)
    spider = zap.spider
    scan_id = spider.scan(url=target, recurse=True)
    print(f'Spider rozpoczęty, scan_id: {scan_id}')
    while int(spider.status(scan_id)) < 100:
        print(f'Spider postep: {spider.status(scan_id)}%')
        time.sleep(2)

    print('Koniec spider')

    # Aktywne skanowanie
    print(f'Rozpoczęcie aktywnego skanowania...')
    active_scan = ascan.scan(url=target, contextid=context_id, recurse=True, scanpolicyname=scan_policy_name)
    print(f"Otrzymano scan_id: {active_scan}")
    if 'scan' in active_scan:
        scan_id = active_scan['scan']
        print(f"ID skanowania: {scan_id}")
    else:
        print("Brak poprawnego scan_id w odpowiedzi.")
        return

    while int(ascan.status(scan_id)) < 100:
        print(f'Postęp aktywnego skanowania: {ascan.status(scan_id)}%')
        time.sleep(2)
    print('Aktywne skanowanie zakończone')



def analiza_wynikow(zap):
    core = zap.core
    html_report = core.htmlreport()
    report_filename = "report.html"
    with open(report_filename, "w", encoding="utf-8") as report_file:
        report_file.write(html_report)
    print(f'Zapisano raport jako {report_filename}')

@app.route('/scan', methods=['POST'])
def scan():
    try:
        # Odbieranie danych z POST request
        data = request.json
        zap_api = data.get('zap_api', 'your_default_zap_api')
        zap_address = data.get('zap_address', 'http://127.0.0.1:8081')
        dvwa_url = data.get('dvwa_url', 'http://192.168.1.173/DVWA')
        target = data.get('target', 'http://192.168.1.173/DVWA/vulnerabilities/sqli')
        context_name = data.get('context_name', 'DVWA_scriptBased')
        scan_policy_name = data.get('scan_policy_name', 'SQL Injection')

        # Inicjalizacja ZAP
        zap = ZAPv2(apikey=zap_api, proxies={"http": zap_address, "https": zap_address})

        # Skany
        skanowanie(zap, dvwa_url, target, context_name, scan_policy_name)

        # Analiza wyników
        analiza_wynikow(zap)

        return jsonify({"status": "success", "message": "Scan and report completed successfully."}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
