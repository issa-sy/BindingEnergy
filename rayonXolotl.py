import numpy as np
import matplotlib.pyplot as plt

# Paramètres physiques
a = 0.547  # paramètre de maille en nm
omega = 0.25 * a**3  # volume atomique effectif (nm³)
four_pi = 4 * np.pi

# Rayon fixe pour les cas particuliers
R_xe = 0.22  # impureté (Xe), j = 0
R_interstitiel = a / 2           # j = 1
R_vacance = a * np.sqrt(2) / 2   # j = -1

# Domaine de j
n_vals = np.arange(-50, 51)
R_vals = np.zeros_like(n_vals, dtype=float)

# Conditions
mask_xe = n_vals == 0
mask_inter = n_vals == 1
mask_vac = n_vals == -1
mask_autres = ~(mask_xe | mask_inter | mask_vac)

# Application des formules
R_vals[mask_xe] = R_xe
R_vals[mask_inter] = R_interstitiel
R_vals[mask_vac] = R_vacance

# Pour tous les autres n ≠ -1, 0, 1
n_autres = n_vals[mask_autres]
R0 = a * np.sqrt(2) / 2
R_vals[mask_autres] = R0 + ( (3 * omega * np.abs(n_autres) / four_pi)**(1/3) - (3 * omega / four_pi)**(1/3) )

# Tracé du diamètre (2R)
D_vals = 2 * R_vals

# Tracé
plt.figure(figsize=(10, 6))
plt.plot(n_vals[mask_autres], D_vals[mask_autres], 'o', label='Complexes n<0 bulle/cavite n>0 boucle', color='blue', markersize=4)
plt.plot(n_vals[mask_xe], D_vals[mask_xe], 'o', label='Impureté (n=0)', color='orange', markersize=6)
plt.plot(n_vals[mask_inter], D_vals[mask_inter], 'o', label='Interstitiel (n=1)', color='green', markersize=6)
plt.plot(n_vals[mask_vac], D_vals[mask_vac], 'o', label='Lacune (n=-1)', color='red', markersize=6)

plt.axvline(0, linestyle='--', color='black')

# Labels
plt.xlabel("n")
plt.ylabel("Diamètre 2R (nm)")
plt.title("Diamètre des amas selon le type de défaut (xolotl)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


