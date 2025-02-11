import time
from zapv2 import ZAPv2


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
    print(f'Spider')
    while int(spider.status(scan_id)) < 100:
        print(f'Spider postep: {spider.status(scan_id)}%')
        time.sleep(2)
    print('Koniec spider')

    # Aktywne skanowanie
    scan_id = ascan.scan(url=target, contextid=context_id, recurse=True, scanpolicyname=scan_policy_name)
    print(f'Rozpoczecie aktywnego skanowania')
    while int(ascan.status(scan_id)) < 100:
        print(f'Postep aktywnego skanowania: {ascan.status(scan_id)}%')
        time.sleep(2)
    print('Aktywne skanowanie zakonczone')


def analiza_wynikow(zap):
    core = zap.core
    html_report = core.htmlreport()
    report_filename = "report.html"
    with open(report_filename, "w", encoding="utf-8") as report_file:
        report_file.write(html_report)
    print(f'Zapisano raport jako {report_filename}')


def main():
    zap_api = 'jh6em125d4lifm0ugqscs0vmh8'
    zap_address = 'http://127.0.0.1:8081'
    dvwa_url = 'http://192.168.158.147/DVWA'
    target = 'http://192.168.158.147/DVWA/vulnerabilities/sqli'
    context_name = 'DVWA_scriptBased'
    scan_policy_name = 'SQL Injection'

    zap = ZAPv2(apikey=zap_api, proxies={"http": zap_address, "https": zap_address})

    skanowanie(zap, dvwa_url, target, context_name, scan_policy_name)
    analiza_wynikow(zap)

if __name__ == "__main__":
    main()

