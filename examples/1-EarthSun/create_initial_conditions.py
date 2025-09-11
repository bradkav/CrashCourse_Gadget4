#!/usr/bin/env python
# coding: utf-8

# #### Initial conditions
# 
# Code for generating initial conditions files. Inspired by [this file](https://gitlab.mpcdf.mpg.de/vrs/gadget4/-/blob/master/examples/G2-gassphere/create_initial_conditions.py?ref_type=heads). 

# In[1]:


# load libraries
import numpy as np  # load numpy
import h5py    # hdf5 format 

import sys
sys.path.append("../..")
import units as u
#Note that the units in this module are defined in cgs units
#(i.e. cm = g = s = 1). So e.g. u.Msun is Solar mass in grams


# In[2]:


FloatType = np.float64  # double precision: np.float64, for single use np.float32
IntType = np.int32


# #### Create ICs for a single light object orbiting a much heavier object

# In[3]:


#Initial condition parameters
filename = 'IC_binary.hdf5'


# In[4]:


number_particles = 2

#Initialise the vectors of positions, velocities, masses, and particle IDs
Pos = np.zeros((number_particles,3), dtype=FloatType)
Vel = np.zeros((number_particles,3), dtype=FloatType)
Mass = np.zeros((number_particles,1), dtype=FloatType)
ids = np.arange(number_particles)

#Set the masses for the Earth and Sun
m1 = 1*u.Msun
m2 = 1e-6*u.Msun
Mass[0, :] = m1
Mass[1, :] = m2

#Separation of the binary
r = 1.0*u.au

#Initial position and velocity of Earth
Pos[1,:] = np.array([r, 0, 0])

v_orb = np.sqrt(u.G*m1/r)
Vel[1,:] = np.array([0, v_orb, 0])

#Check the orbital timescale in code units
#which will be useful for knowing how long
#to run the simulation!
Torb = (2*np.pi*r/v_orb)/u.Tcode

print("Earth's orbital period, in code units:", Torb)


# #### The Initial conditions file
# 
# Now we'll write the initial conditions file. We'll write it in hdf5 format (which is the recommended one). For this, we need to set
# ```
# %---- File formats
# ICFormat             3
# SnapFormat           3 
# ```
# in the `param.txt` file when we run Gadget4.

# In[5]:


# Open the hdf5 file
IC = h5py.File(filename, 'w')

## Create hdf5 groups
header = IC.create_group("Header")
part0 = IC.create_group("PartType0")
part1 = IC.create_group("PartType1")


# The hdf5 file consists of several 'groups'.
# 
# The "Header" group contains meta-information about the simulation, like particle numbers etc.
# 
# The different "PartType0", "PartType1", "PartType2", etc groups contain initial conditions for the different Particle Types in Gadget4. The number of particle types is controlled by the `NTYPES` parameter in the `Config.sh` file. Having different particle types can be useful to keep track of several different classes of particles (DM, Stars, etc).
# 
# Type 0 particles are always hydrodynamical particles (i.e. gas). We don't want any of them, so we will put our particles in the `part1` object (for "PartType1"). 

# In[6]:


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

header.attrs.create("Omega0", 0.0)
header.attrs.create("OmegaB", 0.0)
header.attrs.create("OmegaLambda", 0.0)
header.attrs.create("HubbleParam", 1.0)

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


# ## Important
# 
# Note that when we copy the positions, velocities and masses over into the initial conditions file, we divide by `u.Lcode` etc in order to get them into code units!
