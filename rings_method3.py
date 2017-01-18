""" Plots rings by checking if points on a plane are within the desired ring,
then plots those points. Also appends them to a file"""

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

def check_membership(plane_x,plane_y,max_rad,min_rad):
    """
    Checks to see if all dots in the plane are in rings and adds them to list.
    plane_x: meshgrid array of plane dots' x positions.
    plane_y: meshgrid array of plane dots' y positions.
    max_rad: radius of max ring, int or float.
    min_rad: radius of min ring, int or floar.
    Returns: 2 column array of [dot x pos, dot y pos].
    """
    ring_dots_x = []
    ring_dots_y = []
    dot_count = 0
    
    for i,x in np.ndenumerate(plane_x):
        y = plane_y[i]
        dot_rad = np.sqrt(x**2+y**2)
        if dot_rad>=min_rad and dot_rad<=max_rad: #checks radial dist from origin
            # dot is within rings.
            ring_dots_x.append(x)
            ring_dots_y.append(y)
            dot_count += 1
    
    return np.array(ring_dots_x),np.array(ring_dots_y),dot_count

def write_file(dot_x,dot_y,dot_z,tf,dc1,dc2,ds,dx,dy,dz):
    """
    Appends dot positions to a file with all other needed data
    This can be ran on a file multiple times to keep adding rings
    """
    file_name = input("Enter save name: ")
    file = open(file_name, "a")
    
    for i,dot in np.ndenumerate(dot_x):
        print("{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}\
              {:15.8f}{:15.8f}{:15.8f}".format(dot_x[i],dot_y[i],\
              float(dot_z),tf,dc1,dc2,ds,dx,dy,dz),file = file)
    
    file.close()

def plot_rings(x,y):
    """
    Plots rings as a scatter plot
    """
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.scatter(x,y)
    
###### END FUNCTIONS ###### 


def main():
    """
    Runs whole program
    """
    TRANS_FREQ = 2278.9013 
    DECAY1 = 10
    DECAY2 = 10
    DIPOLE_STR = 5.2917721e-4
    DIPOLE_X = 1
    DIPOLE_Y = 0
    DIPOLE_Z = 0
    
    MAX_RAD = 0.7
    MIN_RAD = 0.6
    DOT_DIST = 0.05 #distance in x and y ddirections between dots
    DOT_Z = 0
    
    plane_x, plane_y = create_plane(MAX_RAD, DOT_DIST)
    # check_membership uses meshgrids as arguements so we create them here
    
    dot_x, dot_y, dot_count = \
    check_membership(plane_x, plane_y, MAX_RAD, MIN_RAD)
    print("Dot count: "+str(dot_count))
    
    plot_rings(dot_x,dot_y)
    
    write_file(dot_x,dot_y,DOT_Z,TRANS_FREQ,DECAY1,DECAY2,\
    DIPOLE_STR,DIPOLE_X,DIPOLE_Y,DIPOLE_Z)
    
    
    