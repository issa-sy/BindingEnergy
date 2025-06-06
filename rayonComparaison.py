import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Paramètres physiques 
# -------------------------------
a = 0.547  # nm (paramètre de maille)
Omega = a**3 / 4  # nm³
b = 0.116  # nm vecteur de Bergers
omega = 0.25 * a**3  # volume atomique 
four_pi = 4 * np.pi

# -------------------------------
# 1. Résultats de Skorek 
# -------------------------------
def rayon_skorek(n):
    R = np.zeros_like(n, dtype=float)
    n_bulles = n <= -1
    n_interstitiel = n == 0
    n_boucles = n >= 1

    R[n_bulles] = ((3 * Omega) / (4 * np.pi))**(1/3) * np.abs(n[n_bulles])**(1/3)
    R[n_interstitiel] = (Omega / (np.pi * b))**0.5 #pour xolotl j'ai mis directement 0,2 
    R[n_boucles] = (Omega / (np.pi * b))**0.5 * np.sqrt(n[n_boucles])
    
    return 2 * R  # diamètre

# -------------------------------
# 2. Résultats de Xolotl 
# -------------------------------
def rayon_xolotl(n):
    R = np.zeros_like(n, dtype=float)
    R_xe = 0.2 #nm
    R_inter = a / 2
    R_vac = a * np.sqrt(2) / 2
    R0 = R_vac

    mask_xe = n == 0
    mask_inter = n == 1
    mask_vac = n == -1
    mask_autres = ~(mask_xe | mask_inter | mask_vac)

    R[mask_xe] = R_xe
    R[mask_inter] = R_inter
    R[mask_vac] = R_vac
    n_autres = np.abs(n[mask_autres])
    R[mask_autres] = R0 + ( (3 * omega * n_autres / four_pi)**(1/3) - (3 * omega / four_pi)**(1/3) )
    
    return 2 * R  # diamètre

# -------------------------------
# Valeur de n
# -------------------------------
n_vals = np.arange(-50, 51)

# Calcul des diamètres
D_skorek = rayon_skorek(n_vals)
D_xolotl = rayon_xolotl(n_vals)

# -------------------------------
# Tracé comparatif
# -------------------------------
plt.figure(figsize=(10, 6))
plt.plot(n_vals, D_skorek, 'o', color='green', label='Résultats de Skorek', markersize=4)
plt.plot(n_vals, D_xolotl, 'o', color='red', label='Résultats de Xolotl', markersize=4)

plt.axvline(0, linestyle='--', color='black')

plt.xlabel("n")
plt.ylabel("Diamètre 2R (nm)")
plt.title("Comparaison des diamètres des amas : Skorek vs Xolotl")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
