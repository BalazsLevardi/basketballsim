# Basketball Simulation #

A simple simulation of basketball shot trajectories, exploring the optimal angle of release for an NBA shooter.

The included scripts are:

## basketball_angles_graphic_fixed.py ##

Create a simple graphic to illustrate the effect on shot trajectory of angle and initial velocity choice.

See basketball_fixed.pdf

![](https://raw2.github.com/nesanders/basketballsim/master/basketball_fixed.png)

## basketball_angles_optimize.py ##

Simulate shot success rate at different release angles and plot the resulting success curve.  The results show that a release angle of ~50 deg is optimal.

![](https://raw2.github.com/nesanders/basketballsim/master/basketball_optimal.png)

## basketball_angles_graphic.py ##

Illustrate a sample of random trajectories corresponding to different choices in release angle.  The release angle distribution is taken to be normal with a standard deviation of 3 deg, and the release velocity is taken to have a standard deviation of 2% around the optimal value.

![](https://raw2.github.com/nesanders/basketballsim/master/basketball_angles.png)


## basketball_tilt_graphic.py ##

A simple plot illustrating the effective surface area of the basketball hoop corresponding to different release angles.  The ball "sees" a larger hoop when released from higher angles, although the spread in final x-positions is also larger at high angles.  These two effects balance to produce the optimal angle referenced above.

![](https://raw2.github.com/nesanders/basketballsim/master/basketball_tilt.png)


## Caveats ##

Physical factors not accounted for include:

* Ball spin
* Air resistance
* Backboard reflection
* Defender blocking


