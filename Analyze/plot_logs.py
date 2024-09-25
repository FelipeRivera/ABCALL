import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV
csv_file_path = './logs/log_analysis.csv'

# Lee el archivo CSV
data = pd.read_csv(csv_file_path)

# Configura el tamaño del gráfico
plt.figure(figsize=(12, 8))

# Define el ancho de las barras
bar_width = 0.35
index = range(len(data['Server']))

# Crea una posición para las barras
bar_positions = [i - bar_width/2 for i in index]

# Gráfico de barras para respuestas correctas e incorrectas
plt.bar(bar_positions, data['Correct Responses'], width=bar_width, color='g', label='Correct Responses', alpha=0.7)
plt.bar([p + bar_width for p in bar_positions], data['Incorrect Responses'], width=bar_width, color='r', label='Incorrect Responses', alpha=0.7)

plt.xlabel('Servers')
plt.ylabel('Count')
plt.title('Correct vs Incorrect Responses per Server')
plt.xticks([p + bar_width/2 for p in bar_positions], data['Server'], rotation=45)
plt.legend()
plt.tight_layout()

# Guarda el gráfico
plt.savefig('./logs/log_analysis.png')
plt.show()

print("Gráfico generado y guardado como log_analysis.png.")