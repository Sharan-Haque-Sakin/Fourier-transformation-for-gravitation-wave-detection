import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


L = 2
N=50


def f(x):
    return x**2

a0 = (2/L) * quad(lambda x: f(x) , 0, L )[0]

def a_n(n):

    val = (2/L) * quad(lambda x: f(x) * np.cos((2*np.pi*n*x)/L) , 0 , L)[0]
    return val

def b_n(n):
    val = (2/L) * quad(lambda x: f(x) * np.sin((2*np.pi*n*x)/L) , 0 , L)[0]
    return val

def fourier_series(x,N):
    result = a0/2
    for k in range(1,N+1):
       result += a_n(k) * np.cos((2*np.pi*k*x)/L) + b_n(k) * np.sin((2*np.pi * k * x)/L)

    return result

x = np.linspace(0 , L , 500)

y = fourier_series(x , N)

f_values = np.array([f(x_i) for x_i in x])

plt.plot(x, f_values, color='black', label='f(x)')

plt.plot(x,y, color="red")


plt.plot(x,f(x))

plt.title("Non 2pi periodic function")
plt.xlabel("x values from 0 to L")   
plt.ylabel("y = f(x)")
plt.legend()
plt.show()
