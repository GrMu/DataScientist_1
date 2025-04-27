import matplotlib.pyplot as plt
import numpy as np
# print(matplotlib.__version__)

x = np.array([0,1,2,3])
y = np.array([0,2,5,8])
z = x**2
plt.figure(figsize=(8,5))
plt.xlabel('X-as')
plt.ylabel('Y-as')
plt.title('Een lijngrafiek')
plt.legend(title='parabool')
plt.grid(True)
plt.plot(x,z, '*')
plt.show()

