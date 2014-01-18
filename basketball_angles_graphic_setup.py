from pylab import *
from scipy.optimize import fsolve
from matplotlib.patches import Ellipse,Rectangle
from matplotlib.font_manager import FontProperties
import pdb

plt.close('all')
font0 = FontProperties()
font0.set_weight('bold')

im_hoop = imread('hoop_3D_cut.png')
hoop_height = y_f*(594./422)
hoop_width = shape(im_hoop)[1]/float(shape(im_hoop)[0])*hoop_height
hoop_offset = hoop_width*(51/258.)

rondo_height = 7*ft
rondo_width = shape(im_rondo)[1]/float(shape(im_rondo)[0])*rondo_height
rondo_offset = rondo_width*(110/218.)
im_rondo = imread('Rondo_cut.png')

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
y_0=7.*ft
y_f=10.*ft
def in_basket(vi,theta):
  """
  Function to evaluate whether or not a given velocity and angle would score
  """
  x,y=calc_traj(vi,theta)
  return min(sqrt((x-x_f)**2 + (y-y_f)**2))
