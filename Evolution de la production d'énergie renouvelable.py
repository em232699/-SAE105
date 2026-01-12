import csv
import matplotlib.pyplot as plt
from datetime import datetime


fichiers = ['hydro.csv', 'solaire.csv', 'eolienne.csv', 'thermique.csv']

plt.figure(figsize=(12, 6))

toutes_les_dates = []

for nom_fich in fichiers:
    liste_dates = []
    liste_valeurs = []

    fic = open(nom_fich, 'r', encoding='utf-8-sig')
    donnees = csv.DictReader(fic, delimiter=';')

    for ligne in donnees:
        if 'Production' in ligne['Filière'] and ligne['Valeur (TWh)']:

            date = datetime.strptime(ligne['Date'], "%Y-%m")
            liste_dates.append(date)

            val = float(ligne['Valeur (TWh)'].replace(',', '.'))
            liste_valeurs.append(val)

    fic.close()

    if liste_dates:
        donnees_triees = sorted(zip(liste_dates, liste_valeurs))
        liste_dates, liste_valeurs = zip(*donnees_triees)

        plt.plot(liste_dates, liste_valeurs, label=nom_fich.replace('.csv', ''))

        toutes_les_dates = liste_dates

plt.xticks(toutes_les_dates[::12], rotation=45)  
plt.legend()
plt.xlabel("Date")
plt.ylabel("Production (TWh)")
plt.title("Évolution des productions d'énergie renouvelable")
plt.grid(True)
plt.tight_layout()  
plt.show()
