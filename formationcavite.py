import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

# Paramètres physiques
a0 = 0.547  # nm
Omega = a0**3 / 4  # nm³
b = 0.116  # nm
Ef_v = 2.5  # eV (énergie de formation d'un défaut Schottky)
T = 1250+273  # °C (température)

# Énergie de surface γ (Éq. 19) en J/m², convertie en eV/nm²
gamma_Jm2 = 0.85 - 1.4e-4 * T  # J/m²
gamma_eVnm2 = gamma_Jm2 * 1e-18 / 1.60218e-19  # Conversion en eV/nm²


# Fonctions pour le rayon Rn selon la valeur de n
def rayon(n):
    R = np.zeros_like(n, dtype=float)
    
    # Pour les bulles (n <= -1)
    n_bulles = n <= -1
    R[n_bulles] = ((3 * Omega) / (4 * np.pi))**(1/3) * np.abs(n[n_bulles])**(1/3)
    return R, n_bulles

# Calcul de Rc (rayon critique de Tolman)
Ra = 0.2138  # Approximation: rayon d'une lacune seule 
Rc = Ra * (1 - (Ef_v / (4 * np.pi * Ra**2 * gamma_eVnm2)))


# Énergie de surface F_surface (Éq. 17)
def energie_surface(Rn):
    return 4 * np.pi * Rn**2 * gamma_eVnm2 * (1 - Rc / Rn)

# Génération des valeurs de n de -1 à -50
n_values = np.arange(-1, -51, -1)  # n = -1, -2, ..., -50
# Calcul des rayons correspondants
R_values, _ = rayon(n_values)

# Calcul des énergies de formation
F_values = energie_surface(R_values)

# Affichage des valeurs (optionnel)
print("| n | R (nm) | F_surface (eV) |")
print("|---|---|---|")
for n, R, F in zip(n_values, R_values, F_values):
    print(f"| {n} | {R:.4f} | {F:.4f} |")
"""# Création d'un DataFrame pandas pour l'export
data = {
    "n": n_values,
    "R (nm)": R_values,
    "F (eV)": F_values
}
df = pd.DataFrame(data)

# Export vers un fichier Excel
output_file = "energies_formation_cavites.xlsx"
df.to_excel(output_file, index=False, sheet_name="Résultats")

print(f"Les résultats ont été exportés dans {output_file}")"""