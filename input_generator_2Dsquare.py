# This will generate dots in a 2D square #

### Algorithm ###
#   initialize number of dots and distance between dots
#   define function to calculate list of coordinates based on above parameters
#   Plot points for confirmation of shape
#   Create output file
#   write formatted points to file
### Algorithm End ###

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import os

sq_side = int(input("Enter square side dot count: "))
sq_height = float(input("Enter height of square ("+u'\u03BC' + "m): "))
dot_dist = float(input("Enter dot distance (.005-5 " + u'\u03BC' + "m): "))
trans_freq = 2278.9013 
decay_c1 = 10
decay_c2 = 10
dipole_str = 5.2917721e-4
dipole_x = 1
dipole_y = 0
dipole_z = 0

def create_dots(sq_side, dot_dist):
    x_pre = np.linspace(0,sq_side*dot_dist,num=sq_side)-(sq_side*dot_dist)/2
    y_pre = x_pre[:]
    x,y = np.meshgrid(x_pre,y_pre)
    return(x,y)
    
#def file_writer(position,tf,dc1,dc2,ds,dx,dy,dz):
#    file_name = input("Enter save name: ")
##    path = os.path.join("../simulation/Maxwell-bloch/dots_files/"+file_name)
#    file = open(file_name, "w")
#    for dot in position:
#        print("{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}\
#{:15.8f}{:15.8f}{:15.8f}"\
#              .format(dot[0],dot[1],dot[2],tf,dc1,dc2,ds,dx,dy,dz),file = file)
#    file.close()  
    
x,y=create_dots(sq_side,dot_dist)
dot_x = []
dot_y = []
dot_z = [sq_height]*sq_side**2
# Fill dot_x and dot_y with positions
for row in range(sq_side):
    column = 0
    for x_val in x[row]:
        dot_x.append(x_val)
        dot_y.append(y[row,column])
        column += 1
position = list(zip(dot_x,dot_y,dot_z))
#file_writer(position)
# Creates plot to check dot positions
fig = plt.figure()
axes = fig.add_subplot(111,projection='3d')
axes.scatter(x,y,dot_z,marker='.')
plt.show()