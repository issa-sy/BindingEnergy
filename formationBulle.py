import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.special import factorial

# Paramètres physiques
a0 = 0.547  # nm
Omega = a0**3 / 4  # nm³
b = 0.116  # nm
Ef_v = 2.5  # eV
r0_kr = 0.2  # nm

# Paramètres thermodynamiques (1250°C)
eta_max = 0.74
T_C = 1250  # Température en °C 
T_K = T_C + 273.15  # Conversion en Kelvin
kT = 8.617333262145e-5 * T_K  # (constante de Boltzmann) x par la tempéature en eV

# Énergie de surface γ(T) - Éq. 18
gamma_Jm2 = 0.85 - 1.4e-4 * T_C  # formule
gamma_eVnm2 = gamma_Jm2 * 1.6e-19 / 1e-18  # Conversion en eV/nm²

# Paramètres du krypton (Kr)
Lambda = 0.00489  # nm la longueur d’onde thermique de de Broglie
beta = 1 / kT
E_inc = 1.3  # eV
gamma_Jm2 = 0.85 - 1.4e-4 * T_K  # J/m²
gamma_eVnm2 = gamma_Jm2 * 1e-18 / 1.60218e-19  # eV/nm²
omega_p = (4/3) * np.pi * r0_kr**3

# Fonction pour le rayon Rn
def rayon(n):
    R = np.zeros_like(n, dtype=float)
    n_bulles = n <= -1
    R[n_bulles] = ((3 * Omega) / (4 * np.pi))**(1/3) * np.abs(n[n_bulles])**(1/3)
    return R, n_bulles

# Calcul du rayon critique Rc (Tolman)
R_1 = 0.2138  # nm
Rc = R_1 * (1 - (Ef_v / (4 * np.pi * R_1**2 * gamma_eVnm2)))

# Énergie de surface
def F_surface(Rn):
    return 4 * np.pi * Rn**2 * gamma_eVnm2 * (1 - Rc / Rn)

# Énergie libre du gaz
def F_gaz(Rn, p=1):
    eta = p * (r0_kr / Rn)**3
    if eta >= eta_max:
        return np.nan
    
    term1 = (eta * (4 - 3 * eta)) / ((1 - eta)**2)
    term2 = np.log(eta)
    term3 = -np.log(omega_p / Lambda**3)
    term4 = -np.log((p**p / factorial(p))**(1/p))
    term5_para = (1 - R_1 / Rn)**3 + (1 - (1 - R_1 / Rn)**3) * np.exp(-beta * E_inc)
    term5 = -np.log(term5_para)
    
    return p * kT * (term1 + term2 + term3 + term4 + term5)

# Énergie totale de la bulle
def F_bulle(n, p=1):
    Rn, _ = rayon(np.array([n]))  
    Rn = Rn[0]  # On récupère le scalaire
    F_total = F_surface(Rn) + F_gaz(Rn, p)
    return F_total if np.isfinite(F_total) else np.nan

# Génération des valeurs de n
n_values = np.arange(-1, -51, -1) # Nombre de lacune on peut le changer de -1 à -inf
R_values, _ = rayon(n_values)
p = 5  # Nombre d'atomes de Kr on peut le changer de 1 à inf

# Calcul de F_surface, F_gaz et F_bulle
F_surface_values = []
F_gaz_values = []
F_bulle_values = []

for n, R in zip(n_values, R_values):
    Fsurf = F_surface(R)
    Fgaz = F_gaz(R, p)
    Fbulle = Fsurf + Fgaz
    if not np.isfinite(Fbulle):
        Fbulle = np.nan
    F_surface_values.append(Fsurf)
    F_gaz_values.append(Fgaz)
    F_bulle_values.append(Fbulle)

# Affichage des résultats
print("| n  | p | R (nm) | F_surface (eV) | F_gaz (eV) | F_bulle (eV) |")
print("|----|---|--------|----------------|------------|--------------|")
for n, R, Fsurf, Fgaz, Fbulle in zip(n_values, R_values, F_surface_values, F_gaz_values, F_bulle_values):
    print(f"| {n:2d} | {p} | {R:.4f} | {Fsurf:.4f} | {Fgaz:.4f} | {Fbulle:.4f} |")
