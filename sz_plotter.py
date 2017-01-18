import matplotlib.pyplot as plt
import numpy as np

def get_bloch_data(file_name):
    """
    Opens a bloch.dat file and extracts the time data and s data from it
    file_name is the name of the path to the file / file name
    returns list of the time at each step and a list of s data
    """
    time_list = []
    s_list = []
    
    bloch_file = open(file_name)

    for line in bloch_file:
        line_list = line.split()
        time_list.append(line_list[0])
        s_list.append(line_list[1:])
        
    bloch_file.close()
        
    return time_list, s_list

def plot_sz(s_list):
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
    
def main():
    """
    Runs two functions above and produces a plot of the sz component of each\
    dot throughout all simulation time
    """
    bloch_file_name = "../sim_results/run8/bloch.dat"
    time_list, s_list = get_bloch_data(bloch_file_name)
    
    plot_sz(s_list)