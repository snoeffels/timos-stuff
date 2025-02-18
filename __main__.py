import os
import numpy as np
import matplotlib.pyplot as plt

# Verzeichnis, in dem sich die ASCII-Dateien befinden
location = "./asc"

# Dateien im Ordner auflisten
files = [f for f in os.listdir(location) if not f.startswith('.')]
num_files = len(files)

# in drei Gruppen einteilen
group1 = files[0::3]  # Gruppe 1
# group2 = files[1::3]  # Gruppe 2
# group3 = files[2::3]  # Gruppe 3

# Arrays zum Speichern erstellen
empty1 = np.zeros(1024)
# empty2 = np.zeros(1024)
# empty3 = np.zeros(1024)

# Schleife zum Aufaddieren der Gruppe 1
for file in group1:
    filepath = os.path.join(location, file)
    data = np.loadtxt(filepath, delimiter=",")
    empty1 += data[:, 1]
wavelength = data[:, 0]  # Vektor mit allen Wellenlängen
mean_values1 = empty1 / len(group1)
final1 = np.column_stack((wavelength, mean_values1))

# Schleife zum Aufaddieren der Gruppe 2
# for file in group2:
#     filepath = os.path.join(location, file)
#     data = np.loadtxt(filepath)
#     empty2 += data[:, 1]
# mean_values2 = empty2 / len(group2)
# final2 = np.column_stack((wavelength, mean_values2))

# Schleife zum Aufaddieren der Gruppe 3
# for file in group3:
#     filepath = os.path.join(location, file)
#     data = np.loadtxt(filepath)
#     empty3 += data[:, 1]
# mean_values3 = empty3 / len(group3)
# final3 = np.column_stack((wavelength, mean_values3))

# Plot erstellen
plt.plot(final1[:, 0], final1[:, 1], 'b', label='1st shot')
# plt.plot(final2[:, 0], final2[:, 1], 'r', label='2nd shot')
# plt.plot(final3[:, 0], final3[:, 1], 'g', label='3rd shot')

# Legende erstellen
plt.legend()

# Achsenbeschriftungen hinzufügen
plt.xlabel('x-Achse (Wellenlänge in nm)')
plt.ylabel('y-Achse (Counts)')

# Titel hinzufügen
plt.title('Gemittelte Counts für Z=500')

# Diagramm anzeigen
plt.savefig("plot.png")  # Speichert das Diagramm als PNG
