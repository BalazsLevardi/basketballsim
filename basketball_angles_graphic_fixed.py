execfile('basketball_angles_graphic_setup.py')

fig,axs=plt.subplots(2,sharex='all',sharey='all',figsize=(5,6.7))
plt.subplots_adjust(hspace=0.1,top=.96,bottom=0.04)

for k in range(2):
  ## Draw hoop
  axs[k].imshow(im_hoop,extent=((x_f-hoop_offset)/ft,(x_f+hoop_width-hoop_offset)/ft,0,hoop_height/ft),aspect='auto')
  ## Draw rondo
  axs[k].imshow(im_rondo,extent=((x_0-rondo_offset)/ft,(x_0+rondo_width-rondo_offset)/ft,0,rondo_height/ft),aspect='auto')
  
  axs[k],axis([(x_0-1)/ft,x_f*1.5/ft,0,y_f*1.8/ft])
  axs[k].set_yticks([])
  axs[k].set_xticks([])




#### Plot fixed velocity
## Get optimal velocity
v_nom = fsolve(in_basket,9,args=(50*pi/180))[0]
angles=array([35,50,65])*pi/180

plt.subplots_adjust(hspace=0.1,top=.9,bottom=0.04)
rim_diameter=18/12.*ft
ball_diameter=8.9/12.*ft
## Draw trajectories
for i in range(len(angles)):
  x,y=calc_traj(v_nom,angles[i])
  if i==1: col='r'
  else: col='b'
  axs[0].plot(x[y>0]/ft,y[y>0]/ft,c=col,ls='dashed')

axs[0].set_title('Different angles - Same velocity')

## Plot angle markers
px=linspace(x_0,x_0+1,2)/ft
py=linspace(y_0,y_0,2)/ft
axs[0].plot(px,py,lw=3,c='k',alpha=.5)
for k in range(len(angles)):
  px2=linspace(x_0,x_0+1*cos(angles[k]),2)/ft
  py2=linspace(y_0,y_0+1*sin(angles[k]),2)/ft
  axs[0].plot(px2,py2,lw=3,c='k',alpha=.5)




#### Plot fixed angle
vs=array([v_nom*.8,v_nom,v_nom*1.2])

plt.subplots_adjust(hspace=0.1,top=.9,bottom=0.04)
rim_diameter=18/12.*ft
ball_diameter=8.9/12.*ft
## Draw trajectories
for i in range(len(vs)):
  x,y=calc_traj(vs[i],angles[1])
  if i==1: col='r'
  else: col='b'
  axs[1].plot(x[y>0]/ft,y[y>0]/ft,c=col,ls='dashed')

axs[1].set_title('Same angle - Different velocities')

## Plot angle markers
px=linspace(x_0,x_0+1,2)/ft
py=linspace(y_0,y_0,2)/ft
axs[1].plot(px,py,lw=3,c='k',alpha=.5)
for k in range(len(angles)):
  px2=linspace(x_0,x_0+vs[k]/vs[1]*cos(angles[1]+.2*(k-1)),2)/ft
  py2=linspace(y_0,y_0+vs[k]/vs[1]*sin(angles[1]+.2*(k-1)),2)/ft
  axs[1].plot(px2,py2,lw=3,c='k',alpha=.5)







plt.savefig('basketball_fixed.pdf',dpi=300)
plt.savefig('basketball_fixed.png',dpi=150)
