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

#a function for the smoothing kernel (see lecture 2 page 20)
def spline(r,h):
    sigma = 2/3
    dims = 1
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

#creates a dictionary of random values to be the initial conditions of the particles
def create_particle():
    position = random.random()*1000
    mass = random.random()
    velocity = random.random()*100
    return {'position':position,'mass':mass,'velocity':velocity,'density':0}

def main():
    #how many particles in the system
    N = 1000
    #speed of sound for calculating pressure, using the speed from dry air
    c = 343
    particles = []
    #generate the list of particles
    for i in range(0,N):
        particles.append(create_particle())
    #generate the densities for each particle
    for particle in particles:
        particle['density'] = calculate_density(particle['position'],particles)
    


    


if __name__ == "__main__":
    main()