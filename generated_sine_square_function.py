import numpy as np 
import matplotlib.pyplot as plt 

def fourier_square_wave(x,N): # Adjusting domain with fourier known formula
    y=np.zeros_like(x)
    
    for k  in range(1,N+1):

       n = 2*k - 1
       y += (1/n)*np.sin(n*x)

    return y*(4/np.pi)


x = np.linspace(-np.pi , np.pi , 500)

for N in [1,5,20,50]:
    y = fourier_square_wave(x,N)
    plt.plot(x,y,label=f"{N} terms")

plt.title("Square wave using Fourier series")
plt.xlabel("x values from -π to π")
plt.ylabel("y = f(x)")

plt.show()