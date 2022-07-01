import earthshine as etools 

import matplotlib.pylab as plt
import numpy as np
import scipy.integrate as integrate

################################################################################

elo = 10
ehi = 500

energy = np.linspace(elo,ehi,50)

density = 1.6e30 # Number of nucleons per m3?
#density_m3 = density_kg * ( 6e26) # Number of nucleons per kg

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
for distance in range(1,10,1):

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
        ke_final= etools.energy_loss_per_distance_traveled(e*1e9, distance, step_size=.1)
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
    plt.xlabel("energy")
    plt.ylabel("number")
    plt.title("energy vs number at CMS (per second)")
    plt.savefig("energy_vs_number_per_second")
    ##plt.yscale('log')
    #plt.legend()



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
plt.title("Number at CMS per month")
plt.savefig("integrated_number per month.png")

################################################################################


#plt.show()
en=np.arange(1,201)
print(en)
enlist=en.tolist()
'''
#print(enlist)
xsec_for_mult_plot=yfunction_xsec[enlist]
flux_for_mult_plot=yfunction_flux[enlist]
mult_plot= xsec_for_mult_plot*flux_for_mult_plot
plt.plot(mult_plot,enlist)
plt.show()
'''

flux_new=etools.neutrino_flux(enlist)
#fluxy=ypts
xsec_new=etools.neutrino_cross_section(enlist)
plt.figure()
#print(ypts)
#print(flux_new[0])
tot= flux_new[0]*xsec_new[0]*density*en[-1]
#print(tot)
plt.plot(en, tot)
#plt.xscale("log")
plt.yscale("log")
plt.xlabel("energy")
plt.ylabel("flux*cross section")
plt.show()

#print(en[-1])


################################################################################

distance1= 0 

N= density*length*y_flux_new*y_xsec_new
Omega=etools.solid_angle(CMS_length, CMS_width/2, distance)
N*=Omega
hemisphere_area=2*np.pi*(distance**2)
N*=hemisphere_area
print(f"distance: {distance1}   Omega: {Omega}.   A_hemi: {hemisphere_area}")
N_at_CMS_from_this_distance1=np.zeros(len(energy))
for i,e in enumerate(energy):
  ke_final=etools.energy_loss_per_distance_traveled(e*1e9, distance1, step_size=.1)
  ke_final/=1e9
  idx, central= etools.find_the_number(ke_final, energy)
  if idx is not None:
    N_at_CMS_from_this_distance1[idx]+= N[i]
    #x1.append(N_at_CMS_from_this_distance1[idx])
N_at_CMS+= N_at_CMS_from_this_distance1
#plt.plot(energy, N_at_CMS_from_this_distance1, label=f"distance={distance1}")
plt.xscale("log")
plt.legend()
N_CMS_month= N_at_CMS*3e7/12

distance2= 20
N= density*length*y_flux_new*y_xsec_new
Omega=etools.solid_angle(CMS_length, CMS_width/2, distance)
N*=Omega
hemisphere_area=2*np.pi*(distance**2)
N*=hemisphere_area
print(f"distance: {distance1}   Omega: {Omega}.   A_hemi: {hemisphere_area}")
N_at_CMS_from_this_distance2=np.zeros(len(energy))
for i,e in enumerate(energy): 
  ke_final=etools.energy_loss_per_distance_traveled(e*1e9, distance2, step_size=.1)
  ke_final/=1e9
  idx, central= etools.find_the_number(ke_final, energy)
  if idx is not None:
    N_at_CMS_from_this_distance2[idx]+= N[i]
    #x1.append(N_at_CMS_from_this_distance1[idx])
N_at_CMS+= N_at_CMS_from_this_distance1
#plt.plot(energy, N_at_CMS_from_this_distance1, label=f"distance={distance1}")
plt.xscale("log")
plt.legend()
N_CMS_month= N_at_CMS*3e7/12


N_at_CMS_from_this_distance_tot= N_at_CMS_from_this_distance1+N_at_CMS_from_this_distance2

plt.plot(energy, N_at_CMS_from_this_distance1, label=f"Distance= {distance1}")

plt.plot(energy, N_at_CMS_from_this_distance2, label=f"Distance= {distance2}")
plt.plot(energy, N_at_CMS_from_this_distance_tot, label="sum") 
plt.xscale("log")
plt.legend()
plt.xlabel("energy (eV)")
plt.ylabel("Number at CMS")
plt.show()

##########################################################################################



