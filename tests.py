import earthshine_tools as etools 

import matplotlib.pylab as plt
import numpy as np

# Energy region that we are interested in (for example)
energy = np.linspace(1,100,1000) # 1 to 100 GeV in 1000 evenly-spaced steps

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

plt.show()


