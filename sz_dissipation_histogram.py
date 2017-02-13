"""
This program will plot a 3D histogram to show the dissipation of energy
direction over time.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def create_data_structure(dots_file, bloch_file):
    """
    This function takes the dots and Bloch data files and functionally stores
    the data under a variable.
    DATA FORMAT:
    [x_pos,y_pos,z_pos,dist_from_origin,[pseudospin_array]]
    parameters are the open, readable files for dots and bloch files.
    returns the data formatted like above and an array of times.
    """
    master_list = []
    dots_data_raw = [line.split() for line in dots_file]
    bloch_data_raw = [line.split() for line in bloch_file]
    dot_count = 0
    time_array = np.array([line[0] for line in bloch_data_raw])
    for dot in dots_data_raw:
    
        x_pos,y_pos,z_pos = float(dot[0]),float(dot[1]),float(dot[2])
        dist = np.sqrt(x_pos**2+y_pos**2+z_pos**2)
    
        time_count = 0 #counts timesteps in bloch data
    
        s_array = np.zeros((len(bloch_data_raw),3)) # stores s data from bloch file
        
        for time in bloch_data_raw:
            
            sx = time[1+dot_count*3]
            sy = time[2+dot_count*3]
            sz = time[3+dot_count*3]
            
            s_array[time_count][0] = float(sx)
            s_array[time_count][1] = float(sy)
            s_array[time_count][2] = float(sz)
    
            time_count += 1
    
        dot_list = [x_pos,y_pos,z_pos,dist,s_array] #formatted like in doc string
        master_list.append(dot_list)
    
        dot_count += 1 # counts the amount of dots completed
        
    return master_list, time_array
    

####### TEST AREA ####### 
    
    
dots_file = open("../sim_results/run14/dots.dat")
bloch_file = open("../sim_results/run14/bloch.dat")
master_list,time_array = create_data_structure(dots_file,bloch_file) 


"""
Algorithm idea
    define shells
        find max distance from origin
        create shells from origin with specified width until farthest dist encompassed
    group dots into new lists according to shell theyre within
    create 2d array with each col a time and each row an ave sz of a shell
    create plot with x as shell y as time, and z as ave sz
"""

# Below is code for defining shells

number_of_shells = 30
shell_array = np.arange(1,number_of_shells+1)

dist_sorted_list = sorted(master_list, key=lambda l: l[3])
max_dist = dist_sorted_list[-1][3]
shell_width = max_dist/number_of_shells
#create data structure to hold dots based on shell they are within
# shell_data = [[shell1],[shell2],...,[shelln]] shell1 is innermost 
shell_data = []
shell_min = 0
shell_max = shell_width
shell_count = 0
while shell_count < number_of_shells:
    for dot in dist_sorted_list:
        current_shell_list = []
        if shell_min < dot[3] <= shell_max:
            #only need to take the sz value
            current_shell_list.append(dot[4][2])
    shell_data.append(current_shell_list)
    shell_count += 1
    shell_min += shell_width
    shell_max += shell_width
#########################################
"""
Groups sz data from each dot into their respective shells
"""
shell_min = 0
shell_max = shell_width
shell_data = [] #becomes a list of current_shells
for i in range(number_of_shells):
    current_shell = [] #list of sz data from each dot in that shell
    for dot in dist_sorted_list:
        if shell_min < dot[3] <= shell_max:
            current_shell.append(dot[4][:,2])
    shell_data.append(current_shell)
    shell_min += shell_width
    shell_max += shell_width
#########################################
"""
forms the average sz array needed for plotting
"""
ave_sz_array = np.zeros((number_of_shells,len(time_array)))
current_shell = 0 # 0 refers to innermost shell
for shell in shell_data:
    if len(shell) == 0:
        current_shell += 1
        continue
    current_shell_ave_sz = np.zeros(len(time_array))
    for timestep in range(len(time_array)):
        ave_sz = sum([sz_data[timestep] for sz_data in shell])/len(shell)
        current_shell_ave_sz[timestep] = ave_sz
    ave_sz_array[current_shell,:] = current_shell_ave_sz
    current_shell += 1
    
##########################################
"""
Plots wireframe plot
"""
fig = plt.figure()
axes = fig.add_subplot(111,projection="3d")

shell_grid = np.zeros((number_of_shells,len(time_array)))
time_grid = np.zeros((number_of_shells,len(time_array)))

for count in range(len(shell_grid)):
    shell_grid[count][:] = count+1

for count in range(len(time_grid)):
    time_grid[count][:] = time_array

axes.plot_wireframe(shell_grid,time_grid,ave_sz_array,rstride=1,cstride=10)
plt.show()














