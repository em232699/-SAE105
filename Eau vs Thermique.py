import csv
import matplotlib.pyplot as plt

liste_dates = []
liste_eau = []
liste_thermique = []

fic1 = open('eau.csv', 'r', encoding='utf-8-sig')
donnees1 = csv.DictReader(fic1, delimiter=';')
for ligne in donnees1:
    if ligne['Valeur (TWh)']:
        date = ligne['Date']
        val = float(ligne['Valeur (TWh)'].replace(',', '.'))
        if date in liste_dates:
            index = liste_dates.index(date)
            liste_eau[index] = liste_eau[index] + val
        else:
            liste_dates.append(date)
            liste_eau.append(val)
fic1.close()

for i in range(len(liste_dates)):
    liste_thermique.append(0.0)

fic2 = open('thermique renouvelable.csv', 'r', encoding='utf-8-sig')
donnees2 = csv.DictReader(fic2, delimiter=';')
for ligne in donnees2:
    if ligne['Valeur (TWh)']:
        date_ligne = ligne['Date']
        val = float(ligne['Valeur (TWh)'].replace(',', '.'))
        if date_ligne in liste_dates:
            index = liste_dates.index(date_ligne)
            liste_thermique[index] = liste_thermique[index] + val
fic2.close()

plt.figure(figsize=(10, 6))

plt.plot(liste_dates, liste_eau, color='blue', label="Eau (Hydraulique)")
plt.plot(liste_dates, liste_thermique, color='red', label="Thermique Renouvelable")

plt.title("Comparaison Production Eau vs Thermique Renouvelable")
plt.xlabel("Date")
plt.ylabel("Production (TWh)")
plt.xticks(liste_dates[::12], rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()