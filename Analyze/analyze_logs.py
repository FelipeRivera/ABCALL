import re
import csv
from collections import defaultdict

# Ruta del archivo de log
log_file_path = '/Users/feliperivera/Desktop/MicroExp/logs/validator.log'

# Expresiones regulares para extraer datos
pattern_warning = re.compile(r'WARNING - Incorrect response from server: (.+)')
pattern_info = re.compile(r'INFO - Server with correct response: (.+)')

# Inicializa contadores
incorrect_responses = defaultdict(int)
correct_responses = defaultdict(int)

# Lee y procesa el archivo de log
try:
    with open(log_file_path, 'r') as file:
        for line in file:
            if 'WARNING' in line:
                match = pattern_warning.search(line)
                if match:
                    server = match.group(1)
                    incorrect_responses[server] += 1
            elif 'INFO' in line:
                match = pattern_info.search(line)
                if match:
                    server = match.group(1)
                    correct_responses[server] += 1
except FileNotFoundError:
    print(f"El archivo {log_file_path} no se encuentra.")
    exit(1)
except Exception as e:
    print(f"Ocurrió un error al procesar el archivo de log: {e}")
    exit(1)

# Guarda los datos procesados en un archivo CSV
csv_file_path = '/Users/feliperivera/Desktop/MicroExp/logs/log_analysis.csv'
try:
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['Server', 'Correct Responses', 'Incorrect Responses']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        all_servers = set(correct_responses.keys()).union(set(incorrect_responses.keys()))
        for server in all_servers:
            writer.writerow({
                'Server': server,
                'Correct Responses': correct_responses.get(server, 0),
                'Incorrect Responses': incorrect_responses.get(server, 0)
            })

    print(f"Análisis de logs completado. Datos guardados en {csv_file_path}.")
except Exception as e:
    print(f"Ocurrió un error al guardar el archivo CSV: {e}")