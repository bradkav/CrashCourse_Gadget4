# CrashCourse_Gadget4
Files and details for a 'crash course' on [Gadget4](https://wwwmpa.mpa-garching.mpg.de/gadget4/).


### Contents:
- [Installation](/installation/): Some quick hints for compiling Gadget4. Includes an environment file for creating a conda environment which _should_ have all the correct packages for compiling and running Gadget4
- [Examples](/examples/): Some simple examples to get us started. In each example folder, you should find a Config.sh file to be used for compiling Gadget4, and code for generating the initial conditions, running Gadget4 and analysing the output. 
- [analysis.py](analysis.py): Some useful code for loading in the snapshot files (and other tools). This code is adapted (by me) from some of the Gadget4 examples, but it isn't part of the official Gadget4 codebase.
- [units.py](units.py): A module with unit definitions. Gadget4 has its own internal units for mass, time, velocity, length etc (which you can change in the `param.txt` file if you want). Having these 'internal' units defined somewhere (alongside standard cgs units) is very useful for unit conversions for generating initial conditions and loading snapshots.
- [Notes.pdf](Notes.pdf): A few slides with some quick hints about how to use Gadget4. These are not comprehensive and they are probably best used as an 'overview' for understanding some of the examples. 