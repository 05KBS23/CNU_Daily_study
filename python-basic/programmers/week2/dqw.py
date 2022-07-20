import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20)
y = np.random.randint(0,20,20)

plt.plot(x,y)

# y축을 20까지 보이게 하는법
plt.axis([0,20,0,20])
plt.yticks([0,5,10,15, 20])
plt.show()