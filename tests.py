import earthshine_tools as etools 

import matplotlib.pylab as plt
import numpy as np

# Energy region that we are interested in (for example)
energy = np.linspace(1.0,200,2000) # 1 to 100 GeV in 1000 evenly-spaced steps
#energy = np.linspace(10,100,10) # 1 to 100 GeV in 1000 evenly-spaced steps

################################################################################
# Cross section
xsec,xdata,ydata = etools.neutrino_cross_section(energy)

plt.figure()
# Draw the original points
plt.plot(xdata,ydata,'o',label="Measurements")
# Draw the interpolated line
plt.plot(energy,xsec,label='Interpolated region of interest')

plt.xlabel(r"E$\nu$ (GeV)",fontsize=18)
plt.ylabel(r"cm$^2$ / nucleon",fontsize=18)
plt.xscale('log')
plt.legend()

plt.title("xsec")
plt.tight_layout()
################################################################################

# Flux

flux,xdata_flux,ydata_flux = etools.neutrino_flux(energy)
#energy = xdata_flux
#flux,xdata_flux,ydata_flux = etools.neutrino_flux(energy)
print(len(flux),len(energy))
print(energy)
print(flux)
print(flux*(energy**2))

plt.figure(figsize=(12,8))

plt.subplot(1,2,1)
# Draw the original points
plt.plot(xdata_flux,ydata_flux*(xdata_flux**2),'o')
# Draw the interpolated line
plt.plot(energy,flux*(energy**2),'v-')
plt.xlabel("Ev (GeV)")
plt.ylabel(r"E$^2$ $\Phi_\nu$ [GeV cm$^{-2}$ s$^{-1}$]",fontsize=14)
plt.yscale('log')
plt.xscale('log')

plt.title("flux curve fig 17")


#"""
#uncomment to see another fig 17 plot

# Plot the "raw" valyes
plt.subplot(1,2,2)

# Draw the original points
plt.plot(xdata_flux,ydata_flux,'o-')
# Draw the interpolated line
plt.plot(energy,flux,'v')
plt.xlabel("Ev (GeV)")
plt.ylabel("")
plt.ylabel(r"$\Phi_\nu$ [GeV cm$^{-2}$ s$^{-1}$]",fontsize=14)
plt.yscale('log')
plt.xscale('log')

plt.title(r"Flux without E$^2$ term")


################################################################################

energy = np.linspace(1,100,1000)

density = 3000 * 6e26

length = 1 # length of "target" in meters?


y_xsec_new,a,b = etools.neutrino_cross_section(energy)
y_flux_new,a,b = etools.neutrino_flux(energy)

print(density, length)
print()
print(y_xsec_new)
print()
print(y_flux_new)

N = density*length*y_flux_new*y_xsec_new

plt.figure()
plt.plot(energy, N)
plt.xscale('log')
plt.yscale('log')

plt.show()
