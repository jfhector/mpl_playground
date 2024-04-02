import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

x = np.linspace(0,2,100)

plt.figure(figsize=(5, 2.7), layout='constrained')
# plt.plot(x, x, label='linear')
# plt.plot(x, x**2, label='quadratic')
# plt.plot(x, x**3, label='cubic')
# plt.plot(x, x**4, label='four')
# plt.plot(x, x**10, label='ten')
plt.plot(x, x**100, label='mille')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple plot')
plt.legend()
