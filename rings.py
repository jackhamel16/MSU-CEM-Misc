###### This plots concentric rings ######

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


radius_start = 2
radius_step = .5
dots_per_ring = 8


def create_ring(radius,dots_per_ring):
    """
    Generates dot positions in a ring based on inputs in parametric.
    radius: radius of the ring, int or float
    dots_per_ring: name says it all, int or float
    Returns: list of tuple, each tuple is a dot
    """
    theta_step = (2*np.pi)/dots_per_ring
    theta = 0
    dots = np.empty(0)
    for i in range(dots_per_ring):
        dot = (theta,radius)
        dots.append(dot)
        theta += theta_step
    return para_to_cart(dots)
    
def para_to_cart(para_list):
    """
    Converts tuples in a list to cartesian from parametric.
    para_list: list of tuples in parametric coordinates
    Returns: List of tuples in cartesian coordinates
    """
    dots = []
    for dot_para in para_list:
        dot_cart = (dot_para[1]*np.cos(dot_para[0]),\
                    dot_para[1]*np.sin(dot_para[0]))
        dots.append(dot_cart)
    return dots
    
#def make_concentric_rings(r, r_step, dots_per_ring, num_of_rings):
#    dots = []
#    for i in num_of_rings:
#        radius = r-r_step*i
#        ring_dots_list = create_ring(radius,dots_per_ring)
#        for dot_tuple in ring_dots_list
    
    
    
    
dots_cart_test = create_ring(radius_start,dots_per_ring)


x = []
y = []
for dot in dots_cart_test:
    x.append(dot[0])
    y.append(dot[1])


#def create_ring(radius,dots_per_ring):
#    """
#    Generates dot positions in a ring based on inputs in parametric.
#    radius: radius of the ring, int or float
#    dots_per_ring: name says it all, int or float
#    Returns: list of tuple, each tuple is a dot
#    """
#    theta_step = (2*np.pi)/dots_per_ring
#    theta = 0
#    dots = []
#    for i in range(dots_per_ring):
#        dot = (theta,radius)
#        dots.append(dot)
#        theta += theta_step
#    return para_to_cart(dots)
#    
#def para_to_cart(para_list):
#    """
#    Converts tuples in a list to cartesian from parametric.
#    para_list: list of tuples in parametric coordinates
#    Returns: List of tuples in cartesian coordinates
#    """
#    dots = []
#    for dot_para in para_list:
#        dot_cart = (dot_para[1]*np.cos(dot_para[0]),\
#                    dot_para[1]*np.sin(dot_para[0]))
#        dots.append(dot_cart)
#    return dots
#    
##def make_concentric_rings(r, r_step, dots_per_ring, num_of_rings):
##    dots = []
##    for i in num_of_rings:
##        radius = r-r_step*i
##        ring_dots_list = create_ring(radius,dots_per_ring)
##        for dot_tuple in ring_dots_list
#    
#    
#    
#    
#dots_cart_test = create_ring(radius_start,dots_per_ring)
#
#
#x = []
#y = []
#for dot in dots_cart_test:
#    x.append(dot[0])
#    y.append(dot[1])

z = 0
fig = plt.figure()
axes = fig.add_subplot(111,projection='3d')
axes.scatter(x,y,z,marker='.')
plt.show()