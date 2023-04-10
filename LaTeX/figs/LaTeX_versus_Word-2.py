import matplotlib.pyplot as plt
import numpy as np
plt.xkcd()

x = np.linspace(0,5,1000)
y1 = x**3+x**2 +1
y2 = x**2 +1
y3 = 1+ 8*(1-np.exp(-x))

plt.figure(figsize=(8,6))
plt.plot(x,y1,'--', label = "Word (Ciencias Naturales)", linewidth=3)
plt.plot(x,y2,'--', label = "Word (Ciencias Sociales)", linewidth=3)
plt.plot(x,y3, label = "LaTeX", linewidth=3)

plt.xlim(0,4.5)
plt.ylim(0,10)
plt.xticks(range(5),['cartas','ensayos', 'artículos', 'tesis', 'libros'], fontsize=10)
plt.yticks([])
plt.xlabel("Complejidad del documento $\longrightarrow$")
plt.ylabel("Esfuerzo $\longrightarrow$")
plt.legend(fontsize=14)
plt.savefig('LaTeX_vs_Word-2.pdf')
plt.savefig('LaTeX_vs_Word-2.png')

