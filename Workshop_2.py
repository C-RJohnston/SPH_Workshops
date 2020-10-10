#Question 3: Produce a histogram of N(eta) against eta using equation 4

import numpy as np
from matplotlib import pyplot as plt

def eta_range(step):
    return np.arange(0,np.pi,step,dtype=float)

def q3():
    step = 0.01
    total = 100000
    etas = eta_range(step)
    N = [0]
    for i in range(0,len(etas)):
        if(i+1 == len(etas)): 
            break
        e2 = etas[i+1]
        e1 = etas[i]
        N.append((np.sin(e2)-e2*np.cos(e2)-np.sin(e1)+e1*np.cos(e1))/np.pi*total)
    plt.plot(etas,N)
    plt.show()

def q4():
    


def main():
    q3()

if __name__ == "__main__":
    main()
