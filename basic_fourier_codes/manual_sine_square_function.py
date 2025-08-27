import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-np.pi , np.pi , 500)
y1 = np.sin(x)
y3 = np.sin(x) + (1/3)*np.sin(3*x) + (1/5)*np.sin(5*x)
y5 = np.sin(x) + (1/3)*np.sin(3*x) + (1/5)*np.sin(5*x) + (1/7)*np.sin(7*x) + (1/9)*np.sin(9*x)

# plt.plot(x, y1, label="1 term")
# plt.plot(x, y3, label="3 terms")
plt.plot(x, y5, label="5 terms")
plt.title("Sine wave")
plt.xlabel("x values from -π to π")
plt.ylabel("y = sin(x)")

plt.show()