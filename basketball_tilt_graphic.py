from pylab import *
from matplotlib.patches import Ellipse,Rectangle

angles = 90 - array([0,20,52,90])

plt.close('all')

fig,axs=plt.subplots(1,len(angles),figsize=(5*len(angles)/2.,5))
for i in range(len(angles)):
  angoff=cos(pi/190.*(90-angles[i]))
  ## Draw pole
  axs[i].add_artist(Rectangle([0,0],width=18/12./4.,height=10*angoff,ec='k',fc='k'))
  ## Draw backboard
  bbwidth=18/12.*3
  axs[i].add_artist(Rectangle([-bbwidth/2.,10*angoff],width=bbwidth,height=bbwidth*angoff/2,ec='k',fc='none',lw=2))
  ## Draw rim
  rh=18/12.*(1-angoff)
  axs[i].add_artist(Ellipse([0,10*angoff-rh/2.],width=18/12.,height=rh,ec='r',fc='none',lw=2))
  
  axs[i].set_xticks([])
  axs[i].set_yticks([])
  axs[i].set_xlabel(str(90-angles[i])+' deg')
  axs[i].axis([-5,5,0,14])


plt.savefig('basketball_tilt.png',dpi=150)
plt.savefig('basketball_tilt.pdf')
