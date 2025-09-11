#### Some help with installation

I'm running on MacOSX.

Start by getting the code:
```
git clone http://gitlab.mpcdf.mpg.de/vrs/gadget4
cd gadget4
```

Let's try and run a specific example, such as [`examples/DM-L50-N128`](https://gitlab.mpcdf.mpg.de/vrs/gadget4/-/tree/master/examples/DM-L50-N128?ref_type=heads). 

You need a Config.sh file before you can compile, so lets take the one from [`examples/DM-L50-N128`](https://gitlab.mpcdf.mpg.de/vrs/gadget4/-/tree/master/examples/DM-L50-N128?ref_type=heads) and copy it into the main gadget4 directory.

Create a file Makefile.systype by copying it from Template-Makefile.systype and uncomment your system (e.g. "Generic-gcc").

Run "make" in the main directory of gadget4. 

You'll probably get a lot of errors, so you'll have to install the relevant packages and make sure that the compiler flags are pointing to the right places. You can edit the relevant piece in [`buildsystem/Makefile.comp.gcc`](https://gitlab.mpcdf.mpg.de/vrs/gadget4/-/tree/master/buildsystem?ref_type=heads) and [`buildsystem/Makefile.gen.libs`](https://gitlab.mpcdf.mpg.de/vrs/gadget4/-/tree/master/buildsystem?ref_type=heads).

Alternatively, I'm using conda to manage my environment. You can create a new environment (which should allow you to compile gadget4 straightforwardly), using the environment file [`gadget4.txt`](gadget4.txt) in this folder. 

Create the environment and then activate it with: 
```
conda env create --file gadget4.txt
conda activate gadget4
```

Once you've successfully run the "make" command, you should have a `Gadget4` executable. 

Copy the Gadget4 executable into an example directory (examples/DM-L50-N128) and then run:
```
mpirun -np 1 ./Gadget4 param.txt 
```
(which will run on a single processor).

The full simulation will take ages (I think it's a galaxy simulation), but it should successfully run, indicating that the compile was successful. 
