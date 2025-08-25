import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return 1 if 0 < x < np.pi else -1

def a_n(n):

    integral, _= quad(lambda x: f(x)*np.cos(n*x), -np.pi , np.pi)

    return integral/np.pi

def b_n(n):
    integral, _= quad(lambda x: f(x)*np.sin(n*x), -np.pi , np.pi)
    return integral/np.pi

def fourier_series(x,N):
    integral,  _= quad(lambda x: f(x), -np.pi , np.pi)
    a0 = (1/(2*np.pi)) * integral
    
    result = a0
    for k in range (1,N+1):
        
        result += a_n(k)*np.cos(k*x) + b_n(k)*np.sin(k*x)

    return result

x = np.linspace(-np.pi , np.pi , 500)

for N in [1,5,20,50]:
    y = fourier_series(x,N)
    plt.plot(x,y,label=f"{N} terms")    

plt.title("Square wave using Fourier series")
plt.xlabel("x values from -π to π")   
plt.ylabel("y = f(x)")
plt.legend()
plt.show()