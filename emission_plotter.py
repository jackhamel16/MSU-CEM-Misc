import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def extract_emission_data(data_list,file):
    """ Takes the eyesore data from emissions.dat and saves it into a list of
    a list representing each line.
    data_list: initialized outside of function and mutated by function.
    file: open emissions.dat file
    """
    for line in file:
        line_list = [float(line[0:26].strip())] # this is the time value and is at index 0 of line_list
        for i in range(26,len(line),54):
            E_vector_strs = line[i:i+54].strip('() ').split(',')
            E_vector_flts = []
            if '\n' not in E_vector_strs: # ['\n'] forms every line, but we dont want it
                for i,num in enumerate(E_vector_strs):
                    # adds each vector component to line_list after making elements into floats
                    E_vector_flts.append(float(num.strip()))
            if len(E_vector_flts) > 0: # empty lists are formed above, but we dont want those
                line_list.append(E_vector_flts)
        data_list.append(line_list)
        
def extract_dot(data_list,dot):
    """
    Extracts data about the E-field at any one dot
    data_list is the list created by extract_data function
    returns an array of the time at each step and array of corresponding fields
    """ 
    mod = (dot-1)*3 # used in loop below to select data on specified dot
    time_array = []
    dot_data = []
    for row in data_list:
        dot_E = np.array([row[1+mod],row[2+mod],row[3+mod]]) #time, E_field x,y,z
        dot_data.append(dot_E)
        time_array.append(row[0])
    time_array = np.array(time_array)
    return time_array,np.array(dot_data)

def plot_ft(ft_list):
    dt = get_dt()
    
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.plot(abs(ft_list))
    tick_locs = [x for x in np.arange(0,161+161/10,161/10)]
#    tick_lbls = [x for x in np.arange(0,dt+dt*dt/10,dt/10)]
    tick_lbls = [x for x in np.arange(0,1.1,0.1)]
    plt.xticks(tick_locs, tick_lbls)
    axes.set_xlabel("Percent of {:.6f} Hz".format(dt))
    plt.show()
    
def get_dt():
    """ 
    Looks in simulation.log for dt value of simulation run
    returns dt from line 13 of file
    """
    file = open("../simulation/Maxwell-Bloch/simulation.log")
    count = 0
    for line in file:
        if count == 13: # dt on this line
            dt = float(line.strip().split()[1])
            file.close()
            return dt
        count+=1
    
def base_main():
    """
    Organizational function. Call to plot E-field four trans
    """
    DOT_NUM = 1
    file = open("../simulation/Maxwell-Bloch/emission.dat")
    emissions_list = []
    
    extract_emission_data(emissions_list,file)
    file.close()
    time_array, dot1_info = extract_dot(emissions_list,DOT_NUM)
    
    Ex = [e[0][0] for e in dot1_info] # real x components of E-field at each time step
    Ey = [e[1][0] for e in dot1_info] # real y components of E-field at each time step
    Ez = [e[2][0] for e in dot1_info] # real z components of E-field at each time step
    
    trans_Ex = np.fft.fft(Ex)
        
    plot_ft(trans_Ex)
    
def loop_main():
    """
    Will loop through every dot in sim and plot 
    """