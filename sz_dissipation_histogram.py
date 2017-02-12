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
    returns the data formatted like above.
    """
    master_list = []
    dots_data_raw = [line.split() for line in dots_file]
    bloch_data_raw = [line.split() for line in bloch_file]
    dot_count = 0
    
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
        
    return master_list
    
####### TEST AREA #######
# notes: pulling dots data is working 
# pulling bloch data for dot 1 works but the rest produces an empty array 
    
    
dots_file = open("hist_test_data.dat")
bloch_file = open("../sim_results/run1/bloch.dat")
master_list = create_data_structure(dots_file,bloch_file) 

"""
Algorithm idea
    define shells
        find max distance from origin
        create shells from origin with specified width until farthest dist encompassed
    group dots into new lists according to shell theyre within
    create 2d array with each col a time and each row an ave sz of a shell
    create plot with x as shell y as time, and z as ave sz



# below is code for plotting a histogram

axes = fig.add_subplot(111,projection='3d')



