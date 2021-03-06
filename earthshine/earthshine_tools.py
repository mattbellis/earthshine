import matplotlib.pylab as plt
import numpy as np

# Something new!
from scipy.interpolate import interp1d


def neutrino_cross_section(energy):

    data=np.loadtxt("cross_section.csv",dtype=float,delimiter=",",unpack=True)
    x=data[1]
    y=data[0]*1e-38

    # Assume the cross section is flat 
    x = np.append(x,[10000])# Units are GeV
    y = np.append(y,y[-1]) # Units are cm^2 / nucleon

    data_min_energy = min(x)
    data_max_energy = max(x)

    if min(energy)<data_min_energy or max(energy)>data_max_energy:
        print("The energy range is outside of where the measurements took place!")
        print(f"measurements: {data_min_energy} - {data_max_energy}")
        print(f"energy:       {min(energy)} - {max(energy)}")
        exit()

    yfunction_xsec = interp1d(x,y)

    ypts = yfunction_xsec(energy)

    # Return the interpolated xsec and the measurments (x,y)
    return ypts,x,y


def neutrino_flux(energy):

    data = np.loadtxt("flux_curve.csv", dtype= float,delimiter=",", unpack=True)

    x = data[0] 
    y = data[1]

    print
    print(x)
    print(y)

    xscaled = 10**x # Plot has data on a log scale
    yscaled = (y* 1e-9) #For scaling when I digitized the curve
    yscaled /= (xscaled**2) # Weird units when data are plotted

    #print(min(x),max(x))
    #print(min(y),max(y))

    # Use the logs of the original data to get a smooth function for the interpolation
    #yfunction_flux = interp1d(x,y,kind='linear')
    yfunction_flux = interp1d(np.log10(xscaled),np.log10(yscaled),kind='linear')

    # We want to pass in to the function the log of the energy
    ypts = yfunction_flux(np.log10(energy))

    # We then back out the flux values like the original
    ypts = 10**ypts

    return ypts,xscaled,yscaled

def time_dil(energy, mass):
    # Let's use units of eV
    # E --> eV
    # p --> eV*c
    # m --> eV*c^2
    p = np.sqrt(energy**2 - mass**2)
    beta = p/energy
    gamma = 1/np.sqrt(1 - beta**2)
    return beta, gamma



#########################################################
def my_beta(mass,ke):

  etot = mass + ke
  p = np.sqrt(etot**2 - mass**2)

  beta = p/etot

  return beta
##########################################################

###############################################################
# We'll pass in the energy and mass in eV
#
# Everything else will be calculated in SI units, save for the
# density
###############################################################
def bethe_formula(ke, mass, Z=10, A=18, rho=1):
  
  m_e = 9.1e-31   # kg
  r_e = 2.8e-15 # meters
  c = 3e8         # m/s
  N_A = 6.022e23

  A *= 0.001 # Convert the atomic weight to kg

  z = 1     # electrons
  echarge = 1.6e-19

  # Let energy be in eV
  beta = my_beta(mass,ke)
  gamma = 1/np.sqrt(1-beta**2)
  
  I = 10 * Z * 1.6e-19

  term1 = 4*np.pi*N_A*(r_e**2)*m_e*(c**2)*(Z/A)*(z**2/beta**2)

  term2 = np.log((2*m_e*(c**2)*(beta**2)*(gamma**2))/I) - (beta**2)
  
  dedx = term1*term2
  
  dedx *= rho

  # dedx is in Joules/m so let's convert it to eV/m
  dedx /= 1.6e-19

  return dedx
##############################################################

def energy_loss_per_distance_traveled(ke_i, distance_traveled, step_size=0.01, mass=105e6, Z=30, A=60, rho=2000):

  d = 0
  ke = ke_i
  ke_prev = ke_i
  while ke>1e6 and d<distance_traveled:

    dedx=bethe_formula(ke,mass=mass, Z=Z, A=A, rho=rho)
    dedx *= step_size

    ke_prev = ke
    ke -= dedx

    d += step_size

    if ke<0:
      ke = ke_prev
      break
  #print(ke_i/1e9, (ke/1e9))
  return ke

#################################################################
def energy_loss_per_distance_traveled(ke_i, distance_traveled, step_size=0.01, mass=105e6, Z=30, A=60, rho=2000):

  d = 0
  ke = ke_i
  ke_prev = ke_i
  while ke>1e6 and d<distance_traveled:

    dedx=bethe_formula(ke,mass=mass, Z=Z, A=A, rho=rho)
    dedx *= step_size

    ke_prev = ke
    ke -= dedx

    d += step_size

    if ke<0:
      ke = ke_prev
      break
  #print(ke_i/1e9, (ke/1e9))
  return ke


#################################################################
def find_the_number(value_to_find,values):
  # This algorithm will not return a valid number if the entry
  # is in the last "1/2" of the lowest bin
  # 
  # For the energy purposes, this is OK because those muons are not
  # going to be detected, at least for the energies we are simulating. 

  nvalues=len(values)
  width= values[1]-values[0]
  #print(f"width of bins= {width}")

  i = None
  central = None

  found_a_bin = False
  for i in range(nvalues):
    central=values[i]
    lo=central-(width/2)
    hi=central+(width/2)
    #print("in find_the_number function")
    #print(value_to_find, central, lo,hi)
    
    if value_to_find>lo and value_to_find<hi:
      #print(i,central)
      found_a_bin = True
      break

  idx = i
  if found_a_bin is False:
      idx = None

  return idx, central


#################################################################
def solid_angle(length, width, radius):
  term1=length*width
  term2=np.sqrt((length**2+4*radius**2)*(width**2+4*radius**2))
  term3=4*np.arcsin(term1/term2)
  return term3



