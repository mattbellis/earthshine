import sys
import matplotlib.pylab as plt
import numpy as np
import earthshine as etools

mass = 0.105e9 # Mass of muon in eV/c^2
ke = 1e9 # units of eV, so 1e9 eV = 1 GeV

# Copper
dedx = etools.bethe_formula(ke,mass,Z=29,A=63,rho=9000)
print(f"For a muon with 1 GeV of kinetic energy in copper,   dE/dx is {dedx/1e6/1e3:.2f} MeV/mm")

# Aluminum
dedx = etools.bethe_formula(ke,mass,Z=13,A=27,rho=2700)
print(f"For a muon with 1 GeV of kinetic energy in aluminum, dE/dx is {dedx/1e6/1e3:.2f} MeV/mm")

# Water
dedx = etools.bethe_formula(ke,mass,Z=10,A=18,rho=1000)
print(f"For a muon with 1 GeV of kinetic energy in water,    dE/dx is {dedx/1e6/1e3:.2f} MeV/mm")

# SiO2, Si Z=14, O Z=8
dedx = etools.bethe_formula(ke,mass,Z=30,A=60,rho=2000)
print(f"For a muon with 1 GeV of kinetic energy in Si02,    dE/dx is {dedx/1e6/1e3:.2f} MeV/mm")


# Make a plot
ke = np.linspace(1e6,1e9,10000)
dedx = etools.bethe_formula(ke,mass,Z=30,A=60,rho=2000)

plt.plot(ke,dedx)
plt.xscale('log')
plt.yscale('log')



# You need this command when running from a script to get the plots to show up.
plt.show()



