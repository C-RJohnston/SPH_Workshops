import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from dataclasses import dataclass
import copy
import time
#c struct like object to store particle data
@dataclass
class Particle:
    position: np.array
    mass: float
    velocity: np.array
    smoothing_length: float = 0.0

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

def particles_over_width(r2,r1,N_Total):
    return (np.sin(r2)-r2*np.cos(r2)-np.sin(r1)+r1*np.cos(r1))*N_Total/np.pi

def generate_particle(total_mass,total_particles,radius):
    """
    Generate a particle in a random position inside the sphere
    with a mass of mass/particles and a random velocity
    """
    #generate a random polar co-ordinate inside the sphere of given radius uses the Box-Muller algorithm for uniformity
    r = np.random.rand()**(1/3)*radius
    costheta = np.random.uniform(-1,1)
    theta = np.arccos(costheta)
    phi = np.random.random()*2*np.pi
    
    #converts polar to cartesian
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    #vectorise postion
    position = np.array([x,y,z])
    #calculate mass
    mass = total_mass/total_particles
    #generate random normalised velocities
    velocity = np.random.rand(1,3)
    return Particle(position,mass,velocity)

def return_radius(particle):
    return (particle.position[0]**2+particle.position[1]**2+particle.position[2]**2)**0.5

def density_at_radius(radius,particles):
    """
    Calculates the density of particles at a given radius in the polytrole
    radius: given radius 0<radius<pi
    particles: array of particles
    """
    m = particles[0].mass
    #removes all the particles outside the test radius
    particles_at_radius = [p for p in particles if return_radius(p)<radius]
    return len(particles_at_radius)*m/(4/3*np.pi*radius**3)
    


    



def q4():
    N =1000
    R = np.pi
    MASS = 4*np.pi**2
    particles = []
    x = []
    y = []
    z = []
    for i in range(0,N):
        particle = generate_particle(MASS,N,R)
        x.append(particle.position[0])
        y.append(particle.position[1])
        z.append(particle.position[2])
        particles.append(particle)


    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(x,y,z)
    plt.show()
    plt.scatter(x,y)
    plt.show()

    radii = np.arange(1/N,R,1/N)
    N_at_r = [len([p for p in particles if return_radius(p)<r]) for r in radii]
    analytic_N_at_r = [particles_over_width(r,0,N) for r in radii]
    plt.plot(radii,N_at_r)
    plt.plot(radii,analytic_N_at_r)
    plt.show()

    # densities = [density_at_radius(r,particles) for r in radii]
    # analytic_densities = [particles_over_width(r,0,N)*(MASS/N)/(4/3*np.pi*(r**3)) for r in radii]

    # plt.plot(radii,analytic_densities)
    # plt.plot(radii,densities)
    # plt.show()





def main():
    q4()

if __name__ == "__main__":
    main()
