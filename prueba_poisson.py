from scipy.stats import poisson
import matplotlib.pyplot as plt

"""
DISTRIBUCION DE POISSON 
La distribución de Poisson describe la probabilidad de que ocurra un número específico de eventos en un intervalo de tiempo fijo o un área fija.
    X → es una variable aleatoria que sigue una distribución de Poisson
    k → es el número de veces que se produce un suceso
    P(X = k) → es la probabilidad de que un suceso ocurra k veces
    e → es la constante de Euler (aproximadamente 2,718)
    λ → lambda es el número medio de veces que se produce un suceso
    ! → es la función factorial
"""

# Parámetros y cálculo de probabilidad
mu = 5
k= 3

k_resaltar = k
poison_calculo = poisson.pmf(k=k, mu=mu)
print(round(poison_calculo, 4))

# ************************************************************************************
prob_resto = 1 - poison_calculo

# Configuración del gráfico circular
etiquetas = [f'P(X = {k_resaltar})\nλ = {mu}', 'Otras probabilidades']
colores = ['#ff9999', '#66b3ff']
explode = (0.1, 0)  # Separación del sector resaltado

plt.pie([poison_calculo, prob_resto],
        labels=etiquetas,
        colors=colores,
        explode=explode,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        textprops={'fontsize': 10}
    )

plt.title('Distribución de Poisson: Probabilidad P(X=3) vs Total\n', fontsize=14)
plt.axis('equal')  # Gráfico perfectamente circular
plt.show()