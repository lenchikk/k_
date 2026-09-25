import matplotlib.pyplot as plt
import numpy as np
x = np.array(np.linspace(-5, 5, 10))
y = x

plt.figure(figsize=(12, 10))
plt.plot(x, y, color="green", linestyle='-', linewidth=6, marker='o', markersize=2, alpha=1)
plt.show()