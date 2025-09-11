import numpy as np


#%---- System of units
#UnitLength_in_cm         3.085678e24        ;  Mpc / h
#UnitMass_in_g            1.989e43           ;  1.0e10 Msun / h
#UnitVelocity_in_cm_per_s 1e5                ;  1 km/sec
#GravityConstantInternal  0

#Define cgs units as the basis
cm = 1.0
g = 1.0
s = 1.0

h = 0.678
Lcode = 3.085678e24*cm/h
Mcode = 1.989e43*g/h
Vcode = 1e5*cm/s
Tcode = Lcode/Vcode

m = 1e2*cm
km = 1e3*m
pc = 3.0857e16*m
kpc = 1e3*pc
Mpc = 1e6*pc
au =  1.495978707e11*m

kg = 1e3*g
Msun = 1.989e+33*g

yr = 60*60*24*365.25*s
kyr = 1e3*yr
Myr = 1e6*yr

G = 6.67430e-11 * m**3 / kg / s**2