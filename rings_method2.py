""" Plots rings by checking if points on a plane are within the desired ring,
then plots those points. """

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

###### FUNCTIONS ######

def create_plane (max_rad,dot_dist):
    """ 
    Creates a plane of dots that encapsulates the rings.
    max_rad: radius of max ring, int or float.
    dot_dist: distance between dots, int or float.
    Returns: meshgrid arrays of the plane dots' x and y positions.
    """
    length = max_rad*2
    dot_count = length/dot_dist+1
    x = np.linspace(0,length,dot_count) - max_rad
    y = x[:]
    X,Y = np.meshgrid(x,y)
    return X,Y

def check_membership(dot_x,dot_y,max_rad,min_rad):
    """
    Checks to see if all dots in the plane are in rings and adds them to list.
    dot_x: meshgrid array of plane dots' x positions.
    dot_y: meshgrid array of plane dots' y positions.
    max_rad: radius of max ring, int or float.
    min_rad: radius of min ring, int or floar.
    Returns: 2 column array of [dot x pos, dot y pos].
    """
    ring_dots = []
    dot_count = 0
    for i,x in np.ndenumerate(dot_x):
        y = dot_y[i]
        dot_rad = np.sqrt(x**2+y**2)
        if dot_rad>=min_rad and dot_rad<=max_rad:
            # dot is within rings.
            ring_dots.append((x,y))
            dot_count += 1
    return np.array(ring_dots),dot_count

def write_file(dot_x,dot_y,dot_z,tf,dc1,dc2,ds,dx,dy,dz):
    file_name = input("Enter save name: ")
#    path = os.path.join("../simulation/Maxwell-bloch/dots_files/"+file_name)
    file = open(file_name, "w")
    for i,dot in np.ndenumerate(dot_x):
        print("{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}\
{:15.8f}{:15.8f}{:15.8f}"\
              .format(dot_x[i],dot_y[i],float(dot_z),tf,dc1,dc2,ds,dx,dy,dz),file = file)
    file.close()

###### END FUNCTIONS ######    

""" Here I set up ring size and call functions to do work """   
# These variables set parameters of the ring to be made
MAX_RAD = 4
MIN_RAD = 3
DOT_DIST = .5
MAX_RAD2 = 2
MIN_RAD2 = 1
DOT_DIST2 = .5

trans_freq = 2278.9013 
decay_c1 = 10
decay_c2 = 10
dipole_str = 5.2917721e-4
dipole_x = 1
dipole_y = 0
dipole_z = 0

x,y=create_plane(MAX_RAD,DOT_DIST)
good_dots,dot_count = check_membership(x,y,MAX_RAD,MIN_RAD)

x2,y2=create_plane(MAX_RAD2,DOT_DIST2)
good_dots2,dot_count2 = check_membership(x2,y2,MAX_RAD2,MIN_RAD2)

print(dot_count+dot_count2)

dots_z = 0
good_dots_x1 = good_dots[:,0]
good_dots_y1 = good_dots[:,1]

good_dots_x2 = good_dots2[:,0]
good_dots_y2 = good_dots2[:,1]

good_dots_x = np.concatenate((good_dots_x1,good_dots_x2))
good_dots_y = np.concatenate((good_dots_y1,good_dots_y2))

write_file(good_dots_x, good_dots_y, dots_z, trans_freq, decay_c1, decay_c2,\
           dipole_str, dipole_x, dipole_y, dipole_z)

""" Here, everything is prepped to be plotted and then plotted """
# Prepping data for plotting
ring_curves_x = np.linspace(-MAX_RAD,MAX_RAD,1000)
def pos_y_ring(x,r):
    return np.sqrt(r**2-x**2)
def neg_y_ring(x,r):
    return -np.sqrt(r**2-x**2)
# Plotting data
fig = plt.figure()
axes = fig.add_subplot(111)
axes.scatter(good_dots_x,good_dots_y,marker='.')
axes.plot(ring_curves_x,pos_y_ring(ring_curves_x,MAX_RAD),'b-')
axes.plot(ring_curves_x,neg_y_ring(ring_curves_x,MAX_RAD),'b-')
axes.plot(ring_curves_x,pos_y_ring(ring_curves_x,MIN_RAD),'b-')
axes.plot(ring_curves_x,neg_y_ring(ring_curves_x,MIN_RAD),'b-')
#if ring_count == 2:
axes.scatter(good_dots_x2,good_dots_y2,marker='.')
axes.plot(ring_curves_x,pos_y_ring(ring_curves_x,MAX_RAD2),'b-')
axes.plot(ring_curves_x,neg_y_ring(ring_curves_x,MAX_RAD2),'b-')
axes.plot(ring_curves_x,pos_y_ring(ring_curves_x,MIN_RAD2),'b-')
axes.plot(ring_curves_x,neg_y_ring(ring_curves_x,MIN_RAD2),'b-')

plt.show()


