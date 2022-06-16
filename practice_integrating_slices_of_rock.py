import earthshine_tools as etools 

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate as integrate

################################################################################

energy = np.linspace(1,100,100)

density = 3000 * 6e26 # Number of nucleons per m3?
#density_m3 = density_kg * ( 6e26 # Number of nucleons per kg

length = 1 # length of "target" in meters?
area_of_CMS = 21*15 # 21m x 15m

################################################################################
y_xsec_new,a,b = etools.neutrino_cross_section(energy)
y_flux_new,a,b = etools.neutrino_flux(energy)

#print(density, length)
#print()
#print(y_xsec_new)
#print()
#print(y_flux_new)

# Let's do this for multiple slices of rock
N_int = np.zeros(len(energy)) # # of muons integrated for all slices of rock

# d will represent the distance from CMS
for d in range(200,198,-1):

    N = density*length*y_flux_new*y_xsec_new

    # Loop over each entry in N *and* energy
    print("---")
    for a,b,c in zip(energy, N, N_int):
        print(a,b,c)
        # Figure out for each energy, what it got shifted to and
        # *then* add it to the new decreased energy in N_int

    N_int += N
    

    #print("---------------")
    #print(N)
    #print(N_int)

plt.plot(energy,N_int, 'o')
plt.yscale('log')
plt.show()


# Now do for CMS 
#N_CMS = N*area_of_CMS

N_CMS = N_int*area_of_CMS
N_CMS_month = N_CMS * 3e7 /  12

'''
plt.figure()
plt.plot(energy, N)
plt.plot(energy, N_CMS)
plt.plot(energy, N_CMS_month)
plt.xscale('log')
plt.yscale('log')

integrated = integrate.trapz(N_CMS_month, energy)
print(f"The integrated number is {integrated}")

#plt.show()
'''
