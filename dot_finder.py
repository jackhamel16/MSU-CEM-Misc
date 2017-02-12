# Finds two lowest sz values at a given timestep, then finds
# the corresponding dots and their positions

import matplotlib.pyplot as plt
import numpy as np

def get_bloch_data():
    """
    Opens a bloch.dat file and extracts the time data and s data from it
    file_name is the name of the path to the file / file name
    returns list of the time at each step and a list of s data
    """
    time_list = []
    s_list = []
    
    bloch_file_name = "../sim_results/run12/bloch.dat"
    bloch_file = open(bloch_file_name)

    for line in bloch_file:
        line_list = line.split()
        time_list.append(line_list[0])
        s_list.append(line_list[1:])
        
    bloch_file.close()
        
    return time_list, s_list

def plot_dots(s_list):
    """
    Plots sz comp of pseduospin of each dot at each timestep
    Also prints the dot count
    """
    figure = plt.figure()
    axes = figure.add_subplot(111)
    axes.set_title("Pseudospin-Z of all system dots")
    axes.set_xlabel("Timestep")
    axes.set_ylabel("Pseudospin-Z")
    
    count = 0
    for dot in range(len(s_list[0])//3):
        dot1 = [float(time[2+dot*3]) for time in s_list]
        axes.plot(dot1)
        count += 1
    print("Dot count: "+str(count))
    
def find_min_sz():
    """
    Finds minimum two sz values at a specific timestep
    """
    time_list, s_list = get_bloch_data()
    
    timestep = 500
    sz = []
    s_min = (1,0)
    s_min2 = (1,0)
    for i,s in enumerate(s_list[timestep-1]):
        if (i+1)%3==0:
            if float(s)<s_min[0]:
                s_min = float(s),(i+1)/3-1
            elif float(s)<s_min2[0] and float(s)>s_min[0]:
                s_min2 = float(s),(i+1)/3-1
                
    return s_min,s_min2
    
def find_dot():
    """
    Finds the dots that correspond to specific pseudospins
    """
    s1,s2 = find_min_sz()
    
    dots_file_name = "../sim_results/run12/dots.dat"
    dots_file = open(dots_file_name)
    
    dots = []
    
    for line,contents in enumerate(dots_file):
        if line == s1[1] or line == s2[1]:
            position = tuple([float(pos) for pos in contents.split()[0:3]])
            dots.append(position)
    return dots
    
def calc_dist(dots):
    dot1 = dots[0]
    dot2 = dots[1]
    
    x_dist = dot1[0] - dot2[0]
    y_dist = dot1[1] - dot2[1]
    z_dist = dot1[2] - dot2[2]

    return np.sqrt(x_dist**2+y_dist**2+z_dist**2)


def main():
    
    bloch_file_name = "../sim_results/run12/bloch.dat"