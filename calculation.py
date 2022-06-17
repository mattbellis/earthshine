import earthshine as etools 

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate as integrate

################################################################################

elo = 10
ehi = 500

energy = np.linspace(elo,ehi,50)

density = 3000 * 6e26 # Number of nucleons per m3?
#density_m3 = density_kg * ( 6e26 # Number of nucleons per kg

length = 1 # length of "target" in meters?

CMS_length = 21 # meters
CMS_width = 15 # meters
area_of_CMS = CMS_length*CMS_width 

area_of_CMS /= 2 
# This is just because the cross section "looks" different from
# different angles, so this is just a guesstimate. 


################################################################################
y_xsec_new,a,b = etools.neutrino_cross_section(energy)
y_flux_new,a,b = etools.neutrino_flux(energy)

#print(density, length)
#print()
#print(y_xsec_new)
#print()
#print(y_flux_new)

# Let's do the calculations for many chunks of rock
N_at_CMS = np.zeros(len(energy))

# These will be at different distances from CMS

plt.figure()
for distance in range(1,200,1):

    # Calculate the number of neutrinos coming out for 1 m^2 of rock of length=length
    # per steradian, at some given energy
    N = density*length*y_flux_new*y_xsec_new

    # What is the solid angle at this distance?
    Omega = etools.solid_angle(CMS_length, CMS_width/2, distance)
    N *= Omega

    # How "many" of these 1m^2 chunks are there at distance=distance
    # *below* CMS (hemisphere)
    hemisphere_area = 2*np.pi*(distance**2) # in m^2
    N *= hemisphere_area

    print(f"distance: {distance}   Omega: {Omega}     A_hemi: {hemisphere_area}")

    # Attenuation -- energy loss!
    N_at_CMS_from_this_distance = np.zeros(len(energy))
    for i,e in enumerate(energy):
        ke_final= etools.energy_loss_per_distance_traveled(e*1e9, distance, step_size=0.1)
        ke_final /= 1e9
        idx, central = etools.find_the_number(ke_final, energy)
        #print(e, ke_final, idx, central)
        if idx is not None:
          # N is the number coming out of the 1m^2 rock at distance=distance
          # N_at_CMS is the number of muons measured at CMS as different energies
          N_at_CMS_from_this_distance[idx] += N[i]
        #else:
          #print(e, ke_final, idx, central)

    #print(N_at_CMS_from_this_distance)
    N_at_CMS += N_at_CMS_from_this_distance

    plt.plot(energy,N_at_CMS_from_this_distance,label=f'distance={distance}')
    plt.xscale('log')
    ##plt.yscale('log')
    plt.legend()



# Now do for CMS 
#N_CMS = N*area_of_CMS
N_CMS_month = N_at_CMS * 3e7 /  12

plt.figure()
#plt.plot(energy, N)
plt.plot(energy, N_at_CMS,label='# muons at CMS/s')
plt.plot(energy, N_CMS_month,label='# muons at CMS/month')
plt.xscale('log')
plt.yscale('log')

plt.legend()
integrated = integrate.trapz(N_CMS_month, energy)
print(f"The integrated number is {integrated} per month for an energy range between {elo} and {ehi} GeV")

#plt.show()
