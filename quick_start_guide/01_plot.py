import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

fig, ax = plt.subplots()
ax.plot([1,2,3,4], [1,4,2,3])
ax.plot([1,2,3,4], [4,2,1,1])
ax.set_title('Mantra')
ax.set_xlabel('yolo')
ax.set_ylabel('on ne vit que une fois')
plt.show()
