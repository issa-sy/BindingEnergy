import numpy as np
import math

# Constantes physiques
kB = 8.617343e-5  # eV/K
D0 = 0.03  # cm²/s (préfacteur)

# Données du tableau
defauts = {
    "V": {"n": -1, "p": 0, "Em": 3.0, "D_300": 1.2e-52, "D_1423": 7.1e-13},
    "I": {"n": 1, "p": 0, "Em": 0.7, "D_300": 5.2e-14, "D_1423": 1.0e-4},
    "Kr": {"n": 0, "p": 1, "Em": 2.2, "D_300": 3.3e-39, "D_1423": 4.8e-10},
    "V2Kr": {"n": -2, "p": 1, "Em": 4.5, "D_300": 7.6e-78, "D_1423": 3.5e-18}
}

T_vals = [300,1523]  # Températures en K

print("Vérification des coefficients de diffusion :")
for nom, data in defauts.items():
    Em = data["Em"]
    for T in T_vals:
        D_calc = D0 * math.exp(-Em / (kB * T))
        #D_ref = data[f"D_{T}"]
        #erreur = abs(D_calc - D_ref) / D_ref * 100 if D_ref != 0 else np.nan
        print(f"{nom} à {T}K : D_calc = {D_calc:.2e} cm²/s %")
