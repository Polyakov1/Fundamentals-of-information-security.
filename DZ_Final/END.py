 import nmap3
import json

host_for_scan = '127.0.0.1'
# host_for_scan = '192.168.100.1'
# host_for_scan = '86.57.251.89'

nmap_obj = nmap3.Nmap()

# Сканирование хоста
print("[*] Scanning...\n")
results = nmap_obj.scan_host(host_for_scan)

# Вывод результатов сканирования хоста
print(f"{results['runtime']['summary']} \n"
      f"equivalent command: {results['stats']['args']} \n")

print(f"name_host: {results[host_for_scan]['hostname'][0]['name']} \n"
      f"ipv4: {results[host_for_scan]['ipv4'][0]}, mac: {results[host_for_scan]['macaddress'][0]} \n")

print("=" * 100)

# Сканирование портов
print("[*] Scanning ports...\n")
results2 = nmap_obj.scan_subnet(host_for_scan)

# Вывод результатов сканирования портов
print(f"{results2['runtime']['summary']} \n"
      f"equivalent command: {results2['stats']['args']} \n")

# Вывод информации о открытых портах
ports_open = results2[host_for_scan]['ports']
for port in ports_open:
      print(f"port: {port['portid']} state: {port['state']} reason: {port['reason']}")

print(f"\n{results2['task_results'][0]['extrainfo']} scanning complete \n")
