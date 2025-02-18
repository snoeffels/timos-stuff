import numpy as np
import matplotlib.pyplot as plt

def polynom(x, x0, a, b, c):
    return a * (x - x0) ** 2 + b * (x - x0) + c

def voigt(x, x0, w, a):
    return a / (1 + ((x - x0) / w) ** 2)

def full_fit(x, x0p, a, b, c, x01, w1, a1, x02, w2, a2):
    return polynom(x, x0p, a, b, c) + voigt(x, x01, w1, a1) + voigt(x, x02, w2, a2)

# Wertebereich für x definieren
x = np.linspace(390, 410, 1000)

a = 0.001
b = 0.1
c = 2000
x0p = 400
x01 = 395
w1 = 1
a1 = 2
x02 = 405
w2 = 0.5
a2 = 6

# Figure 1
plt.figure(1)
plt.plot(x, full_fit(x, x0p, a, b, c, x01, w1, a1, x02, w2, a2))
plt.title("Full Fit Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("full_fit.png")

# Figure 2
plt.figure(2)
plt.plot(x, voigt(x, x01, w1, a1))
plt.title("Voigt Function Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("voigt.png")

# Berechnung der Summe der Voigt-Funktion
counts_voigt1 = np.sum(voigt(x, x01, w1, a1))
print("Sum of Voigt Function Values:", counts_voigt1)
