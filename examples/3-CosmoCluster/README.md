### Cosmo Cluster Example

Another simple example, this time for of a cluster of light objects, uniformly distributed in a sphere. In this case, we'll set `ComovingIntegrationOn` to `1`, so that cosmological evolution (i.e. Hubble expansion) is included. 

Note that Gadget4 does not include a period of radiation domination (i.e. Omega_r = 0); the cosmology includes only matter and Lambda. 

For cosmological integration, the time parameter is not physical time, but the scale factor `a`. We'll start at `a = 1e-2` (z ~ 100) and end at `a = 3e-2` (z ~ 33). The timestep parameters (e.g. max timestep) are not in physical time but in units of `ln(a)`.

**Instructions**:
- Compile Gadget4 using the `Config.sh` file in this directory
- Move the Gadget4 executable to this directory
- Run `python3 create_initial_conditions.py` to generate the initial conditions file `IC_cosmo.hdf5` (you can also use the `create_initial_conditions.ipynb` notebook)
- Run `mpirun -np N ./Gadget4 param.txt` (where `N` is the number of cores to run on) to get the simulation results.
- You can use the `analyze_snapshots.ipynb` folder to analyze the results.

By default, the `create_initial_conditions.py` script will generate a cluster of objects with the same mean density as the background matter density. You should find that when you look at the snapshots, the system does not collapse under gravity (i.e. the comoving radius remains constant). 

However, you can pass the `-delta` flag, in order to generate a cluster of objects with an over-density or an underdensity. Try:
```
python3 create_initial_conditions.py -delta -0.5
```
to generate initial conditions with an underdensity and then see how the system evolves. Then try:
```
python3 create_initial_conditions.py -delta 0.5
```
for a system with an overdensity.