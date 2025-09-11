### Cluster Example

Another simple example, this time for of a cluster of light objects, uniformly distributed in a sphere.

This simulation runs in Newtonian space (i.e. no cosmological expansion) with vacuum boundary conditions (NOT periodic).

**Instructions**:
- Compile Gadget4 using the `Config.sh` file in this directory
- Move the Gadget4 executable to this directory
- Run `python3 create_initial_conditions.py` to generate the initial conditions file `IC_cluster.hdf5` (you can also use the `create_initial_conditions.ipynb` notebook)
- Run `mpirun -np N ./Gadget4 param.txt` (where `N` is the number of cores to run on) to get the baseline simulation results
- Run `mpirun -np N ./Gadget4 param_soft.txt`. This corresponds to a simulation with a much larger softening length (`SofteningComovingClass0` in the parameter file)
- Run `mpirun -np N ./Gadget4 param_lores.txt`. This simulation uses lower resolution timesteps (controlled by `ErrTolIntAccuracy` in the parameter file)

You will then have a few new output folders, for the three sets of simulations.

You can use the `analyze_snapshots.ipynb` folder to analyze the results and compare the results of the different simulations. 
