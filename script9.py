import numpy as np
import matplotlib.pyplot as plt
x = np.array(np.linspace(-5, 5, 10))
y = x

plt.figure(figsize=(12, 10))
plt.subplot(221)
plt.plot(x, y, color="red", linestyle='-', linewidth=2, marker='o', markersize=2, alpha=1)
plt.show()