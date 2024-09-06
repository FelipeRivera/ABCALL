import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV
csv_file_path = '/Users/feliperivera/Desktop/MicroExp/logs/log_analysis.csv'

# Lee el archivo CSV
data = pd.read_csv(csv_file_path)

# Configura el tamaño del gráfico
plt.figure(figsize=(10, 6))

# Gráfico de barras para respuestas correctas e incorrectas
for server in data['Server']:
    server_data = data[data['Server'] == server]
    plt.bar(server, server_data['Correct Responses'].values[0], color='g', label='Correct Responses', alpha=0.7)
    plt.bar(server, server_data['Incorrect Responses'].values[0], color='r', bottom=server_data['Correct Responses'].values[0], label='Incorrect Responses', alpha=0.7)

plt.xlabel('Servers')
plt.ylabel('Count')
plt.title('Correct vs Incorrect Responses per Server')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

# Guarda el gráfico
plt.savefig('/Users/feliperivera/Desktop/MicroExp/logs/log_analysis.png')
plt.show()

print("Gráfico generado y guardado como log_analysis.png.")