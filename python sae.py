import csv
import matplotlib.pyplot as plt

liste_dates = []
liste_nuc = []
liste_fichiers_renouvelables = []

fic1 = open('nucleaire.csv', 'r', encoding='utf-8-sig')
donnees1 = csv.DictReader(fic1, delimiter=';')
for ligne in donnees1:
    if ligne['Valeur (TWh)']:
        liste_dates.append(ligne['Date'])
        val = ligne['Valeur (TWh)'].replace(',', '.')
        liste_nuc.append(float(val))
fic1.close()

for i in range(len(liste_dates)):
    liste_fichiers_renouvelables.append(0.0)

fichiers = ['eau.csv', 'solaire.csv', 'vent.csv', 'thermique renouvelable.csv']

for i in fichiers:
    fic = open(i, 'r', encoding='utf-8-sig')
    donnees = csv.DictReader(fic, delimiter=';')
    for ligne in donnees:
        if ligne['Valeur (TWh)']:
            date_ligne = ligne['Date']
            val = float(ligne['Valeur (TWh)'].replace(',', '.'))
            if date_ligne in liste_dates:
                index = liste_dates.index(date_ligne)
                liste_fichiers_renouvelables[index] = liste_fichiers_renouvelables[index] + val
    fic.close()

plt.figure(figsize=(10, 6))

plt.plot(liste_dates, liste_nuc, color='red', label="Nucléaire")
plt.plot(liste_dates, liste_fichiers_renouvelables, color='blue', label="Renouvelable")

plt.title("Production Électrique")
plt.xlabel("Date")
plt.ylabel("Production (TWh)")
plt.xticks(liste_dates[::12], rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
