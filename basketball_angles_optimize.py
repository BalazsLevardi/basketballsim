execfile('basketball_angles_graphic_setup.py')


## Generate angle distributions
angle_choices=array(arange(30,71,4))*pi/180.
angle_delta=3*pi/180.
N=5000
angles=[]
for k in range(len(angle_choices)):
  angles.append(np.random.normal(angle_choices[k],angle_delta,N))

angles=array(angles)
make=zeros(len(angles))

## Calculate optimal velocity
vi=[]
for k in range(len(angle_choices)):
  vi.append(fsolve(in_basket,9,args=(angle_choices[k])))

for k in range(len(angles)):
  make[k]=0
  for i in range(N):
    x,y=calc_traj(vi[k]*np.random.normal(1,.02),angles[k][i])
    place=where((x>x_f*.8) & (y<y_f))[0]
    if len(place>0): place=place[0]
    else: place=0
    overshoot = x[place] - x_f
    if abs(overshoot) < rim_diameter/2. and y[place] >= y_f-ball_diameter/2.:
      col='r'
      make[k]+=1


plt.figure(figsize=(6,6))
x,y=angle_choices*180/pi , make/float(N)
f=polyfit(x,y,4)
px=linspace(35,65,1000)
plt.plot(px,polyval(f,px),lw=3,c='r')
plt.xlabel('Launch angle (deg)')
plt.ylabel('Success rate')

plt.savefig('basketball_optimal.pdf',dpi=300)

