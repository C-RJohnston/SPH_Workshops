#Assignment 1
#Smoothed Particle Hydrodynamics
#Write a basic 1-dimensional SPH code. Explain the individual steps your code is taking

#Implementing the SPH
#1 Gather initial conditions {m,x,v,u,e,...}
#2 calculate densities rho = mW
#3 determine pressure at each particle location
#4 determine pressure gradient
#5 update velocities
#6 update positions
#7 repeat from step 2

import random
import numpy as np

#a function for the smoothing kernel (see lecture 2 page 20)
def spline(r,h):
    """
    Cubic spline smoothing kernel (1D)
    sigma: normalisation constant
    h: smoothing length
    r: r_j-r distance between the particles
    """
    sigma = 2/3
    q = r/h
    #the otherwise case
    if(q>2 or q<0):
        return 0
    #the 0<=q<=1 case
    elif(q<=1):
        return sigma/h*(1-3/2*q**2+3/4*q**3)
    #the 1<=q<=2 cae
    else:
        return sigma*((2-q)**3)/(4*h)

def gradSpline(r,h):
    """
    Gradient of the cubic spline smoothing kernel (1D)
    sigma: normalisation constant
    h: smoothing length
    r: r_j-r distance between the particles

    in 1D dW/dx = (x_j-x)/|x_j-x|*dW/dr
    """
    sigma = 2/3
    q = r/h
    k = r/abs(r)
    #the otherwise case
    if(q>2 or q<0):
        return 0
    #the 0<=q<=1 case
    elif(q<=1):
        return k*sigma/h*(3*q+9/4*q**2)
    #the 1<=q<=2 cae
    else:
        return k*sigma*(-3*(2-q)**2)/(4*h) 


#same as the calculate_property function but using the fact that the two densities cancel
#see lecture 2 page 22
def calculate_density(position,particles):
    density = 0
    for particle in particles:
        r = position - particle['position']
        density +=particle['mass']*spline(r,random.random()) #using a random number for h, refine to improve
    return density

#using the kernel to calculate the quantities, can be used for any fluid quantity
#see lecture 2 page 22
def calculate_property(property,position,particles):
    p = 0
    for particle in particles:
        r = position - particle['position']
        p+=particle['mass']/particle['density']*particle[property]*spline(r,random.random()) #using a random number for h, refine to improve
    return p


def main():
    pass
    


    


if __name__ == "__main__":
    main()