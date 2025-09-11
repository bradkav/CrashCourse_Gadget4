# load libraries
import sys  # load sys; needed for exit codes
import numpy as np  # load numpy
import h5py  # load h5py; needed to read snapshots
import csv
import os

import units as u

#matplotlib.rc_file_defaults()
FloatType = np.float64

#loads the gadget snapshot name
def load_snapshot(fname, sort=True, cgs_units=True):
    try:
        data = h5py.File(fname, "r")
    except:
        print("Could not open file: " + fname + " !")
        sys.exit(1)

    time = FloatType(data["Header"].attrs["Time"])
    Pos = np.array(data["PartType1"]["Coordinates"], dtype = FloatType) 
    Vel = np.array(data["PartType1"]["Velocities"], dtype = FloatType)
    ParticleIDs = np.array(data["PartType1"]["ParticleIDs"])
    
    #If this flag is set, convert from code units to cgs units
    if (cgs_units):
        time *= u.Tcode
        Pos  *= u.Lcode
        Vel  *= u.Vcode
    
    #The order of the particles in the snapshots is not conserved,
    #so let's sort the particles so that the i-th entry in the
    #array always corresponds to the same particle
    if sort == True:
        sortargs = np.argsort(ParticleIDs)
    else:
        sortargs = np.arange(len(ParticleIDs))
    return time, Pos[sortargs,:], Vel[sortargs,:], ParticleIDs

#Load a list of snapshots (labelled by i_list) and concatenate
#them into a big array of positions with dimensions (N_snapshots, N_particles, 3)
#Also outputs the list of times of the snapshots
def load_all_snapshots(fname_root, i_list, cgs_units = True):
    for i, i_file in enumerate(i_list):
        filename = os.path.join(fname_root, 'snapshot_%03d.hdf5' % i_file)
        t, Pos, _, _ = load_snapshot(filename, sort=True, cgs_units=cgs_units)
        if i == 0:
            ts = []
            N_part = len(Pos)
            Pos_full = np.zeros((len(i_list), N_part, 3))
        
        ts.append(t)
        Pos_full[i,:,:] = Pos
    ts = np.array(ts)
    return ts, Pos_full