### Earth-Sun Example

A simple example of a binary (like the Earth-Sun system). 

**Instructions**:
- Compile Gadget4 using the `Config.sh` file in this directory
- Move the Gadget4 executable to this directory
- Run `python3 create_initial_conditions.py` to generate the initial conditions file `IC_binary.hdf5` (you can also use the `create_initial_conditions.ipynb` notebook)
- Run `mpirun -np N ./Gadget4 param.txt` (where `N` is the number of cores to run on)

You will then have a new `output` folder, which contains all the snapshots from the simulation. 

You can use the `analyze_snapshots.ipynb` folder to analyze the results.

**Notes**:
- In the initial conditions file, we calculate the orbital period of the system as ~6.9e-13 in code units, which is why we set `TimeMax` to this value in the `param.txt` file.
- We set `ComovingIntegrationOn` to `0` in the `param.txt` file because we don't want to include the Hubble expansion. 