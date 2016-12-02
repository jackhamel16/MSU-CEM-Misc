##### Plots plane in 3D space using eq of a plane ######

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import os

side_count = int(input("Enter n dots for n x n square: "))
dist = float(input("Enter x,y distance between dots: "))
eq_constants = input("Enter a,b,c,d for ax+by+cz=d as a,b,c,d: ").split(',')
trans_freq = 2278.9013 
decay_c1 = 10
decay_c2 = 10
dipole_str = 5.2917721e-4
dipole_x = 1
dipole_y = 0
dipole_z = 0

def calculate_dot_pos(side_count, dist, abcd):
    length = side_count * dist - dist
    x = np.linspace(-length/2,length/2,side_count)
    y = np.linspace(-length/2,length/2,side_count)
    X,Y = np.meshgrid(x,y)
    a = float(abcd[0])
    b = float(abcd[1])
    c = float(abcd[2])
    d = float(abcd[3])
    Z = (d + a*X + b*Y)/c
    return X,Y,Z
    
def write_file(position,tf,dc1,dc2,ds,dx,dy,dz):
    file_name = input("Enter save name: ")
#    path = os.path.join("../simulation/Maxwell-bloch/dots_files/"+file_name)
    file = open(file_name, "w")
    for dot in position:
        print("{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}{:15.8f}\
{:15.8f}{:15.8f}{:15.8f}"\
              .format(dot[0],dot[1],dot[2],tf,dc1,dc2,ds,dx,dy,dz),file = file)
    file.close()
    
x,y,z = calculate_dot_pos(side_count,dist,eq_constants)

dot_x = []
dot_y = []
dot_z = []
# Fill dot_x and dot_y with positions
for row in range(side_count):
    column = 0
    for x_val in x[row]:
        dot_x.append(x_val)
        dot_y.append(y[row,column])
        dot_z.append(z[row,column])
        column += 1
position = list(zip(dot_x,dot_y,dot_z))

write_file(position, trans_freq, decay_c1, decay_c2, dipole_str,\
            dipole_x, dipole_y, dipole_z)

fig = plt.figure()

axes = fig.add_subplot(111,projection='3d')
axes.set_ylabel('y')
axes.set_xlabel('x')
axes.set_xlim3d(-5,5)
axes.set_ylim3d(-5,5)
axes.set_zlim3d(-6,6)
axes.scatter(x,y,z,marker='.')
plt.show()