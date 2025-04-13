import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
A = 2        # Amplitud
f = 5        # Frecuencia en Hz
phi = np.pi/4  # Fase en radianes
t = np.linspace(0, 1, 1000)  # Tiempo de 0 a 1 seg con 1000 muestras

# Señal
y = A * np.cos(2 * np.pi * f * t + phi)

# Graficación
plt.figure(figsize=(8,4))
plt.plot(t, y, label=r'$y(t) = A \cos(2\pi f t + \phi)$')
plt.axhline(0, color='black', linewidth=0.5)  # Línea en y=0
plt.axvline(0, color='black', linewidth=0.5)  # Línea en t=0
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Senoidal')
plt.legend()
plt.grid()
plt.show()
