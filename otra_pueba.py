import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Datos de las puntuaciones para cada aspecto
datos = {
    'Inteligencia': [5, 5, 4],
    'Creatividad': [5, 4, 4],
    'Series y Películas': [5, 5, 5],
    'Salidas Tranquilas': [5, 5, 5],
    'Lectura': [2, 3, 3],
    'Comida Dulce': [4, 5, 5],
    'Honestidad': [5, 5, 5],
    'Expresión de Sentimientos': [2, 4, 4],
    'Animales': [5, 5, 5],
    'Atención': [5, 5, 4],
    'Planes a Futuro': [5, 5, 5]
}

# Calcular la media y la desviación estándar para cada aspecto
stats = {}
for key, values in datos.items():
    media = np.mean(values)
    std_dev = np.std(values, ddof=1)  # Use ddof=1 to get sample standard deviation
    stats[key] = (media, std_dev)

# Generar y graficar la campana de Gauss
x = np.linspace(0, 15, 1000)

plt.figure(figsize=(10, 8))

for aspect, (media, std_dev) in stats.items():
    y = norm.pdf(x, media, std_dev)
    plt.plot(x, y, label=f'{aspect} (μ={media:.2f}, σ={std_dev:.2f})')

# Añadir etiquetas y leyenda
plt.xlabel('Puntuación')
plt.ylabel('Densidad de probabilidad')
plt.title('Campana de Gauss para cada aspecto')
plt.axvline(x=13, color='g', linestyle='--', label='13-15: Aceptable')
plt.axvline(x=10, color='b', linestyle='--', label='10-12: Posiblemente aceptable')
plt.axvline(x=7, color='r', linestyle='--', label='7-9: No aceptable')
plt.legend()
plt.grid(True)

plt.show()