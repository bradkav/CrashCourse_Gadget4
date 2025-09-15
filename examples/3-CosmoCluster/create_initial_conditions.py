#!/usr/bin/env python
# coding: utf-8

# #### Initial conditions
# 
# Code for generating initial conditions files. Inspired by [this file](https://gitlab.mpcdf.mpg.de/vrs/gadget4/-/blob/master/examples/G2-gassphere/create_initial_conditions.py?ref_type=heads). 

# In[1]:


# load libraries
import numpy as np  # load numpy
import h5py    # hdf5 format 
from matplotlib import pyplot as plt

import argparse

import sys
sys.path.append("../..")
import units as u
#Note that the units in this module are defined in cgs units
#(i.e. cm = g = s = 1). So e.g. u.Msun is Solar mass in grams


parser = argparse.ArgumentParser()
parser.add_argument('-delta', '--delta', help='Overdensity parameter, delta', type=np.float64, default=0.0)
args = parser.parse_args()

delta = args.delta

print("> Generating initial conditions for delta = ", delta)

# In[2]:


FloatType = np.float64  # double precision: np.float64, for single use np.float32
IntType = np.int32


# #### Create ICs for a shell of light objects

# In[3]:


#Initial condition parameters
filename = 'IC_cosmo.hdf5'


# In[4]:


number_particles = 1000

#Initialise the vectors of positions, velocities, masses, and particle IDs
Pos = np.zeros((number_particles,3), dtype=FloatType)
Vel = np.zeros((number_particles,3), dtype=FloatType)
Mass = np.zeros((number_particles,1), dtype=FloatType)
ids = np.arange(number_particles)


# In[5]:


#Let's define a space of comoving radius L, which contains a density rho = rho_bg * (1 + delta)

#Cosmological parameters
Omega0 = 0.308
OmegaLambda = 0.692
rho_c0 = 3*(u.h * 100 * (u.km/u.s)/u.Mpc)**2/(8*np.pi*u.G)


#Initial scale factor and density
ai = 1e-2
rhoi = (1 + delta) * rho_c0 * (Omega0 * ai**-3 + OmegaLambda)

#Radius L of the region
L = 1.0*u.kpc
L_phys = ai*L
#print("(Comoving) Radius of the shell in code units:", L/u.Lcode)

#Set the mass of the particles based on the desired density
V = (4*np.pi/3)*(L_phys)**3
m_total = rhoi*V
m = m_total/number_particles

#Set the masses for the objects
Mass[:] = m

#Uniformly sample the positions of the particle within 
#a sphere of radius L
rs = L*(np.random.rand(number_particles))**(1/3)
#rs = L*np.ones(number_particles)
thetas = np.arccos(2*np.random.rand(number_particles) - 1)
phis = 2*np.pi*np.random.rand(number_particles)

xs = rs*np.sin(thetas)*np.cos(phis)
ys = rs*np.sin(thetas)*np.sin(phis)
zs = rs*np.cos(thetas)

#Centre the system at zero
Pos[:,0] = xs - np.mean(xs)
Pos[:,1] = ys - np.mean(ys)
Pos[:,2] = zs - np.mean(zs)


# #### The Initial conditions file
# 
# Now we'll write the initial conditions file. We'll write it in hdf5 format (which is the recommended one). For this, we need to set
# ```
# %---- File formats
# ICFormat             3
# SnapFormat           3 
# ```
# in the `param.txt` file when we run Gadget4.
# 
# **NOTE:** When we run in cosmological mode (`ComovingIntegrationOn 1`), the positions, velocities etc that we pass to Gadget4 (and the numbers that are saving to the snapshot files) are *comoving* coordinates.

# In[6]:


# Open the hdf5 file
IC = h5py.File(filename, 'w')

## Create hdf5 groups
header = IC.create_group("Header")
part0 = IC.create_group("PartType0")
part1 = IC.create_group("PartType1")

## header entries
#This is the number of particles in each Particle Type
#Like we said, we want 0 in Type 0 and number_particles in Type 1.
NumPart = np.array([0,number_particles], dtype=IntType)

#Now we specify a bunch of header parameters
header.attrs.create("NumPart_ThisFile", NumPart)
header.attrs.create("NumPart_Total", NumPart)
header.attrs.create("NumPart_Total_HighWord", np.zeros(2, dtype=IntType) )
header.attrs.create("MassTable", np.zeros(2, dtype=IntType) )
header.attrs.create("Time", 0.0)
header.attrs.create("Redshift", 0.0)
header.attrs.create("BoxSize", 0)
header.attrs.create("NumFilesPerSnapshot", 1)

header.attrs.create("Omega0", 0.308)
header.attrs.create("OmegaB", 0.0482)
header.attrs.create("OmegaLambda", 0.692)
header.attrs.create("HubbleParam", 0.678)

if Pos.dtype == np.float64:
    header.attrs.create("Flag_DoublePrecision", 1)
else:
    header.attrs.create("Flag_DoublePrecision", 0)

## Copy datasets
#Note that we set the datasets in part1, not part0
#because part0 corresponds to hydrodynamical particles
#and we want gravity only.
part1.create_dataset("ParticleIDs", data=ids)
part1.create_dataset("Coordinates", data=Pos/u.Lcode)
part1.create_dataset("Masses", data=Mass/u.Mcode)
part1.create_dataset("Velocities", data=Vel/u.Vcode)

IC.close()

print("> Done.")

