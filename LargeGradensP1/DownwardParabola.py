import numpy as np
import matplotlib.pyplot as plt

def parabola(w):
    a = -1
    b = 60
    c = 0

    return a * w**2 + b*w + c

w = np.linspace(-10, 70, 300)

y = parabola(w)

plt.plot(w, y, label="downward opening parabola")
plt.title("Downward opening Parabola")
plt.xlabel("W")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.ylim(-200, 1000)
plt.legend()
plt.savefig("downwardOpeningParabola.png")

