from pylab import *
from scipy.optimize import fsolve
from matplotlib.patches import Ellipse,Rectangle
from matplotlib.font_manager import FontProperties
import pdb

plt.close('all')
font0 = FontProperties()
font0.set_weight('bold')

im_hoop = imread('hoop_3D_cut.png')

def calc_traj(vi,theta):
  """
  Function to calculate ballistic trajectory
  """
  vyi=vi*sin(theta)
  vxi=vi*cos(theta)
  t=linspace(0,20,10000)
  x=x_0+vxi*t
  y=y_0+vyi*t-.5*9.81*t**2
  return x,y

ft=0.305 # conversion to meters
x_0=0
x_f=20.*ft
y_0=5.*ft
y_f=10.*ft
def in_basket(vi,theta):
  """
  Function to evaluate whether or not a given velocity and angle would score
  """
  x,y=calc_traj(vi,theta)
  return min(sqrt((x-x_f)**2 + (y-y_f)**2))

## Generate angle distributions
angle_choices=array([40.,52,60,80])*pi/180.
angle_delta=3*pi/180.
N=5000
angles=[]
for k in range(len(angle_choices)):
  angles.append(np.random.normal(angle_choices[k],angle_delta,N))

angles=array(angles)

## Calculate optimal velocity
vi=[]
for k in range(len(angle_choices)):
  vi.append(fsolve(in_basket,9,args=(angle_choices[k])))

## Calculate random trajectories
fig,axs=plt.subplots(len(angle_choices),sharex='all',figsize=(6,10))
plt.subplots_adjust(hspace=0)
rim_diameter=18/12.*ft
ball_diameter=8.9/12.*ft
for k in range(len(angle_choices)):
  ## Draw pole
  axs[k].add_artist(Rectangle([(x_f+rim_diameter/2.)/ft,0],width=rim_diameter/4./ft,height=y_f/ft,ec='k',fc='k'))
  ## Draw hoop
  axs[k].add_artist(Rectangle([(x_f-rim_diameter/4.)/ft,y_f/ft],width=rim_diameter*2/ft,height=rim_diameter*2/ft,ec='k',fc='none',lw=2))
  ## Draw rim
  axs[k].add_artist(Ellipse([x_f/ft,y_f/ft],width=rim_diameter/ft,height=.2/ft,angle=0,ec='r',fc='none',lw=2))
  axs[k].axis([0,x_f*1.3/ft,0,y_f*2.4/ft])
  ## Draw trajectories
  make=0
  for i in range(N):
    x,y=calc_traj(vi[k]*np.random.normal(1,.03),angles[k][i])
    place=where((x>x_f*.8) & (y<y_f))[0]
    if len(place>0): place=place[0]
    else: place=0
    overshoot = x[place] - x_f
    if abs(overshoot) < rim_diameter/2. and y[place] >= y_f-ball_diameter/2.:
      col='r'
      make+=1
    else:
      col='b'
    if i<25: axs[k].plot(x[y>0]/ft,y[y>0]/ft,c=col,alpha=.5,ls='dashed')
    #pdb.set_trace()
  axs[k].text(.2/ft,y_f*2/ft,'%0.0f'%(angle_choices[k]*180/pi)+' deg: %0.0f'%(100*float(make)/N)+'% success',fontproperties=font0)

axs[-1].set_xlabel('ft from hoop')
plt.figtext(.03,.5,'ft above ground',rotation='vertical')

plt.savefig('basketball_angles.png',dpi=150)
plt.savefig('basketball_angles.pdf')
