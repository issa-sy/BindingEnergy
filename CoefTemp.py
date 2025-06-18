import numpy as np
import matplotlib.pyplot as plt

# Constantes
kB = 8.617343e-5  # eV/K
D0 = 0.03  # cm²/s (préfacteur)

# Activation energy for Kr
Em_Kr = 2.2  # eV

# Températures en °C
T_C = [1000, 1150, 1250, 1350, 1450, 1600]

# Conversion en Kelvin
T_K = np.array(T_C) + 273.15

# Calcul du coefficient de diffusion D(T) = D0 * exp(-Em / kBT)
D_Kr = D0 * np.exp(-Em_Kr / (kB * T_K))

# Tracé
plt.figure(figsize=(8, 5))
plt.plot(T_C, D_Kr, marker='o', linestyle='--', color='darkblue')
plt.yscale('log')
plt.xlabel("Température (°C)", fontsize=10)
plt.ylabel("Coefficient de diffusion du Kr (cm²/s)", fontsize=10)
#plt.title("Diffusion du krypton dans UO₂")
plt.grid(True, which='both', linestyle='--', linewidth=0.8)
plt.tight_layout()
plt.show()
