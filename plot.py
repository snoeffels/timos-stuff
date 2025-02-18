import os
import numpy as np
import matplotlib.pyplot as plt

# Verzeichnis, in dem sich die ASCII-Dateien befinden
location = "./asc"

# Dateien im Ordner auflisten
files = [f for f in os.listdir(location) if not f.startswith('.')]
num_files = len(files)

groups = [[] for _ in range(num_files)]
for i, file in enumerate(files):
    groups[i % num_files].append(file)

# Arrays zum Speichern erstellen
data_arrays = [np.zeros(1024) for _ in range(num_files)]

# Daten verarbeiten
wavelength = None
for idx, group in enumerate(groups):
    for file in group:
        filepath = os.path.join(location, file)
        data = np.loadtxt(filepath, delimiter=",")
        data_arrays[idx] += data[:, 1]

    if wavelength is None:
        wavelength = data[:, 0]  # Wellenlängen speichern

    mean_values = data_arrays[idx] / len(group)
    groups[idx] = np.column_stack((wavelength, mean_values))

# Plot erstellen
colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k'] * (num_files // 7 + 1)
plt.figure(figsize=(10, 6))

for idx, group_data in enumerate(groups):
    plt.plot(group_data[:, 0], group_data[:, 1], colors[idx], label=f'Group {idx + 1}')

# Legende erstellen
plt.legend()

# Achsenbeschriftungen hinzufügen
plt.xlabel('x-Achse (Wellenlänge in nm)')
plt.ylabel('y-Achse (Counts)')

# Titel hinzufügen
plt.title('Gemittelte Counts für Z=500')

# Diagramm speichern
plt.savefig("plot.png")
