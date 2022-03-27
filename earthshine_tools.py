import matplotlib.pylab as plt
import numpy as np

# Something new!
from scipy.interpolate import interp1d


def neutrino_cross_section(energy):

    data=np.loadtxt("cross_section.csv",dtype=float,delimiter=",",unpack=True)
    x=data[1]
    y=data[0]*1e-38

    # Assume the cross section is flat 
    x = np.append(x,[1000])# Units are GeV
    y = np.append(y,y[-1]) # Units are cm^2 / nucleon

    data_min_energy = min(x)
    data_max_energy = max(x)

    if min(energy)<data_min_energy or max(energy)>data_max_energy:
        print("The energy range is outside of where the measurements took place!")
        print(f"measurements: {data_min_energy} - {data_max_energy}")
        print(f"energy:       {min(energy)} - {max(energy)}")
        exit()

    yfunction_xsec = interp1d(x,y)

    xpts = energy
    ypts = yfunction_xsec(energy)

    # Return the interpolated xsec and the measurments (x,y)
    return ypts,x,y
