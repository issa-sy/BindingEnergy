import numpy as np
import matplotlib.pyplot as plt
import pandas as pd  # Bibliothèque pour l'export Excel

# Paramètres physiques
a0 = 0.547  # nm
Omega = a0**3 / 4  # nm³
b = 0.116  # nm
mu_GPa = 87  # GPa
mu = 87 
Ef_I = 10  # eV (énergie de formation d'un SIA, valeur arbitraire)

# Fonction pour le rayon Rn (Éq. non numérotée dans l'image)
def rayon(n):
    R = np.zeros_like(n, dtype=float)
    n_boucles = n >= 1
    R[n_boucles] = (Omega / (np.pi * b))**0.5 * (n[n_boucles])**0.5
    return R, n_boucles

# Génération des valeurs de n
n_values = np.arange(1, 51, 1)  # n = 1 à 50
R_values, _ = rayon(n_values)

# Calcul de δ pour n=1 (condition initiale)
R1 = 0.3351  # R1 pour n=1
delta = R1 * (1 - (Ef_I / (2 * np.pi * mu * b**2 * R1)))



# Énergie de formation F (Éq. 22)
def energie_formation(Rn):
    return 2 * np.pi * mu * b**2 * Rn * (1 - delta / Rn )

F_values = energie_formation(R_values)

# Affichage sous forme de tableau
print("| n | R (nm) | F (eV) |")
print("|---|-------|--------|")
for n, R, F in zip(n_values, R_values, F_values):
    print(f"| {n} | {R:.4f} | {F:.4f} |")
"""
# Création d'un DataFrame pandas pour l'export
data = {
    "n": n_values,
    "R (nm)": R_values,
    "F (eV)": F_values
}
df = pd.DataFrame(data)

# Export vers un fichier Excel
output_file = "energies_formation_boucles.xlsx"
df.to_excel(output_file, index=False, sheet_name="Résultats")

print(f"Les résultats ont été exportés dans {output_file}")"""