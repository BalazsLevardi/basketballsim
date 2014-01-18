execfile('basketball_angles_graphic_setup.py')


## Generate angle distributions
angle_choices=array([30.,50,80])*pi/180.
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
fig,axs=plt.subplots(len(angle_choices),sharex='all',sharey='all',figsize=(5,10))
plt.subplots_adjust(hspace=0.05,top=.96,bottom=0.04)
rim_diameter=18/12.*ft
ball_diameter=8.9/12.*ft
for k in range(len(angle_choices)):
  ## Draw hoop
  axs[k].imshow(im_hoop,extent=((x_f-hoop_offset)/ft,(x_f+hoop_width-hoop_offset)/ft,0,hoop_height/ft),aspect='auto')
  ## Draw rondo
  axs[k].imshow(im_rondo,extent=((x_0-rondo_offset)/ft,(x_0+rondo_width-rondo_offset)/ft,0,rondo_height/ft),aspect='auto')
  ## Draw trajectories
  make=0
  for i in range(N):
    x,y=calc_traj(vi[k]*np.random.normal(1,.02),angles[k][i])
    place=where((x>x_f*.8) & (y<y_f))[0]
    if len(place>0): place=place[0]
    else: place=0
    overshoot = x[place] - x_f
    if abs(overshoot) < rim_diameter/2. and y[place] >= y_f-ball_diameter/2.:
      col='r'
      make+=1
    else:
      col='b'
    if i<25: axs[k].plot(x[y>0]/ft,y[y>0]/ft,c=col,alpha=.75-.5*(col=='b'),ls='dashed')
  slabel='%0.0f'%(angle_choices[k]*180/pi)+' degrees:\n %0.0f'%(100*float(make)/N)+'% success'
  #axs[k].text(.2/ft,y_f*2/ft,slabel,fontproperties=font0)
  axs[k].set_ylabel(slabel)
  axs[k],axis([(x_0-1)/ft,x_f*1.5/ft,0,y_f*1.5/ft])
  axs[k].set_yticks([])
  axs[k].set_xticks([])

#axs[-1].set_xlabel('ft from hoop')
#plt.figtext(.03,.5,'ft above ground',rotation='vertical')


plt.savefig('basketball_angles.png',dpi=150)
plt.savefig('basketball_angles.pdf',dpi=300)
