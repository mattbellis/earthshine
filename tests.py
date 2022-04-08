import earthshine_tools as etools 

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate as integrate

#'''
# Energy region that we are interested in (for example)
energy = np.linspace(1.0,200,200) # 1 to 200 GeV in 200 evenly-spaced steps
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
#print(len(flux),len(energy))
#print(energy)
#print(flux)
#print(flux*(energy**2))

plt.figure(figsize=(12,8))

plt.subplot(1,2,1)
# Draw the original points
plt.plot(xdata_flux,ydata_flux*(xdata_flux**2),'o')
# Draw the interpolated line
plt.plot(energy,flux*(energy**2),'v-')
plt.xlabel(r"E$_\nu$ (GeV)")
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
plt.xlabel(r"E$_\nu$ (GeV)")
plt.ylabel("")
plt.ylabel(r"$\Phi_\nu$ [GeV$^{-1}$ cm$^{-2}$ s$^{-1}$]",fontsize=14)
plt.yscale('log')
plt.xscale('log')

plt.title(r"Flux without E$^2$ term")
##"""


################################################################################

energy = np.linspace(1,100,1000)

density = 3000 * 6e26 # Number of nucleons per m3?
#density_m3 = density_kg * ( 6e26 # Number of nucleons per kg

length = 100 # length of "target" in meters?
area_of_CMS = 12*15 # 21m x 15m

################################################################################
y_xsec_new,a,b = etools.neutrino_cross_section(energy)
y_flux_new,a,b = etools.neutrino_flux(energy)

#print(density, length)
#print()
#print(y_xsec_new)
#print()
#print(y_flux_new)

N = density*length*y_flux_new*y_xsec_new

# Now do for CMS 
N_CMS = N*area_of_CMS
N_CMS_month = N_CMS * 3e7 /  12

plt.figure()
plt.plot(energy, N)
plt.plot(energy, N_CMS)
plt.plot(energy, N_CMS_month)
plt.xscale('log')
plt.yscale('log')

integrated = integrate.trapz(N_CMS_month, energy)
print(f"The integrated number is {integrated}")

#plt.show()
################################################################################
#'''


c= 3e8 # m/s
mass_muon= 105e6 # Mass of muon in eV / c^2
energy = 1e9 # eV

beta, gamma = etools.time_dil(energy, mass_muon)

velocity=beta*c
#print(velocity)

t=np.linspace(0,.01,10000) # Seconds
tau = 2.2e-6 # Lifetime of muon in seconds 2.2 microsections

plt.figure()

for energy in range(10,110,10):
    print(energy)
    energy *= 1e9

    d=(velocity*t)/1000 #kilometers

    beta, gamma = etools.time_dil(energy, mass_muon)

    N = np.exp(-t/(tau*gamma))

    plt.plot(d, N,label=fr"$E_\mu =$ {energy/1e9:0.0f} GeV")

plt.xlabel('Distance (km)')

plt.legend(fontsize=8)

plt.show()
