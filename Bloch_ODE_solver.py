import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def calculate_E_field(E_0,freq,t,t_0):
    """
    Calculates electric field at dipole moment operator.
    E_initial is the E field at previous time
    freq is frequency of E field
    t is current time
    t_0 is previous time
    Returns: E field as a float
    """
    sigma = 0.1
    
    E = E_0 * np.cos( freq * t ) * np.exp( -(t - t_0)**2 / (2 * sigma**2) )
    return E
    
def calculate_E_field_rot(E_0,freq,t,t_0):
    """
    Calculates electric field at dipole moment operator in rotating frame.
    E_initial is the E field at previous time
    freq is frequency of E field
    t is current time
    t_0 is previous time
    Returns: E field as a float
    """
    sigma = 0.1
    
    E = E_0 * np.exp( -(t - t_0)**2 / (2 * sigma**2) )
    return E
    
def plot_E(E_0,E_freq,trans_freq,t_0,time_list): 
    """
    Plots the Electric field of pulse with respect to time
    """
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.set_xlabel('Time')
    axes.set_ylabel('E-Field Magnitude')
    axes.set_title('Pulse E-Field')
    axes.plot(time_list,calculate_E_field(E_0,E_freq,time_list,t_0))
    plt.show()
    
def calculate_pseudospin_euler(trans_freq,dipole_mom,s_initial,t_step,E):
    """
    Calculates pseudospin at current time using euler integrator
    trans_freq is transition frequency between energy levels
    dipole_mom is the dipole moment operator of the atom
    s_intial is the psuedospin vector from previous time
    t_step is the time step amount
    Returns: column vector of pseudospin, x,y,z
    """
    plancks = 0.658211928 # meV * ps
    x = 2 * dipole_mom * E / plancks
    ohm_matrix = np.matrix([[0,-trans_freq,0],[trans_freq,0,x],[0,-x,0]])
#    print(ohm_matrix)
    s = t_step * ohm_matrix * s_initial + s_initial
    return s
    
def calculate_pseudospin_rk4\
(trans_freq,dipole_mom,s_initial,t,t_step,E_freq,E_0,t_0):
    """ Calculates pseudospin at current time using euler integrator
    trans_freq is transition frequency between energy levels
    dipole_mom is dipole moment operator of atom
    s_initial is pseudospin vector at previous time
    t is current time
    t_step is the time step amount
    E_freq is frequency of pulse's E field
    E_0 is max amplitude of E field
    t_0 is 
    """
    plancks = 0.658211928 # meV * ps
    
    E_t = calculate_E_field(E_0,E_freq,t,t_0) # E-field at t
    E_half = calculate_E_field(E_0,E_freq,t+t_step/2,t_0) # E-field at half step
    E_full = calculate_E_field(E_0,E_freq,t+t_step,t_0) # E-field at full step
    
    x_t = 2 * dipole_mom * E_t / plancks
    x_half = 2 * dipole_mom * E_half / plancks
    x_full = 2 * dipole_mom * E_full / plancks
    
    ohm_matrix_t = np.matrix([[0,-trans_freq,0],[trans_freq,0,x_t],[0,-x_t,0]])
    ohm_matrix_half = \
    np.matrix([[0,-trans_freq,0],[trans_freq,0,x_half],[0,-x_half,0]])
    ohm_matrix_full = \
    np.matrix([[0,-trans_freq,0],[trans_freq,0,x_full],[0,-x_full,0]])
    
    k1 = ohm_matrix_t * s_initial
    k2 = ohm_matrix_half * (s_initial + t_step*k1/2)
    k3 = ohm_matrix_half * (s_initial + t_step*k2/2)
    k4 = ohm_matrix_full * (s_initial + t_step*k3)
    
    return s_initial + t_step/6 * ( k1 + 2*k2 + 2*k3 + k4)
    
def calculate_pseudospin_rot_rk4\
(trans_freq,dipole_mom,s_initial,t,t_step,E_freq,E_0,t_0):
    """ Calculates pseudospin in rotating frame at current time using rk4 integrator
    trans_freq is transition frequency between energy levels
    dipole_mom is dipole moment operator of atom
    s_initial is pseudospin vector at previous time
    t is current time
    t_step is the time step amount
    E_freq is frequency of pulse's E field
    E_0 is max amplitude of E field
    t_0 is 
    """
    plancks = 0.658211928 # meV * ps
    
    E_t = calculate_E_field_rot(E_0,E_freq,t,t_0) # E-field at t
    E_half = calculate_E_field_rot(E_0,E_freq,t+t_step/2,t_0) # E-field at half step
    E_full = calculate_E_field_rot(E_0,E_freq,t+t_step,t_0) # E-field at full step
    
    x_t = 2 * dipole_mom * E_t / plancks
    x_half = 2 * dipole_mom * E_half / plancks
    x_full = 2 * dipole_mom * E_full / plancks
    
    ohm_matrix_t = np.matrix([[0,trans_freq-E_freq,0],[E_freq-trans_freq,0,x_t],[0,-x_t,0]])
    ohm_matrix_half = \
    np.matrix([[0,trans_freq-E_freq,0],[E_freq-trans_freq,0,x_half],[0,-x_half,0]])
    ohm_matrix_full = \
    np.matrix([[0,trans_freq-E_freq,0],[E_freq-trans_freq,0,x_full],[0,-x_full,0]])
    
    k1 = ohm_matrix_t * s_initial
    k2 = ohm_matrix_half * (s_initial + t_step*k1/2)
    k3 = ohm_matrix_half * (s_initial + t_step*k2/2)
    k4 = ohm_matrix_full * (s_initial + t_step*k3)
    
    return s_initial + t_step/6 * ( k1 + 2*k2 + 2*k3 + k4)
    
def plot_pseudospin(s_list):
    """
    Plots the pseudospin vecotr in 3d
    """
    sx = [float(s[0]) for s in s_list]
    sy = [float(s[1]) for s in s_list]
    sz = [float(s[2]) for s in s_list]
        
    fig = plt.figure()
    axes = fig.add_subplot(111,projection='3d')
    axes.set_ylabel('y')
    axes.set_xlabel('x')
    axes.set_zlabel('z')
    axes.set_title('Pseudospin Vector')
    axes.plot(sx,sy,sz)
    plt.show()
    return sx,sy,sz
    
def plot_pseudospin_time(s_list,time_list):
    """
    Plots the z-component of pseudospin with respect to time
    """
    sz = [float(s[2]) for s in s_list]
        
    fig = plt.figure()
    axes = fig.add_subplot(111)
    axes.set_ylabel('Pseudospin Z-Component')
    axes.set_xlabel('Time')
    axes.plot(time_list,sz)
    plt.show()

##### Main functions solve Bloch equations using Euler or RK4 integrators #####
    
def main_euler():
    """
    This organizes all constants and runs all functions with Euler integrator.
    """
    E_0 = 15000
    E_freq = 3.4e2 # 1/ps
    trans_freq = 3.4e2 # 1/ps
    dipole_mom = 10 * 5.29177*10**-5 # micro meters
    s_initial = np.matrix([[0],[0],[-1]]) # ground state
    time_step = 1/(200 * trans_freq) # ps
    stop_time = 1 # ps
    t_0 = 0.5 # ps, time at which pulse has max amplitude
    time_list = np.arange(0,stop_time,time_step)
    s_list = []
    # loop through time and calculate pseudospin at each time
    for time in time_list:
        E = calculate_E_field( E_0, E_freq, time, t_0 )
        s_future = calculate_pseudospin_euler\
        ( trans_freq, dipole_mom, s_initial, time_step, E )
        s_list.append(s_future)
        s_initial = s_future
    if True:    
        plot_E(E_0,E_freq,trans_freq,t_0,time_list)
        plot_pseudospin_time(s_list,time_list)
    plot_pseudospin(s_list)
    
def main_rk4():
    """
    Organizes constants and runs functions with rk4 integrator.
    """
    E_0 = 15000
    E_freq = 3.4e2 # 1/ps
    trans_freq = 3.4e2 # 1/ps
    dipole_mom = 10 * 5.29177*10**-5 # micro meters
    s_initial = np.matrix([[0],[0],[-1]]) # ground state
    time_step = 1/(20 * trans_freq) # ps
    stop_time = 1 # ps
    t_0 = 0.5 # ps, time at which pulse has max amplitude
    time_list = np.arange(0,stop_time,time_step)
    s_list = []
    
    for time in time_list:
        s_future = calculate_pseudospin_rk4\
            (trans_freq,dipole_mom,s_initial,time,time_step,E_freq,E_0,t_0)
        s_list.append(s_future)
        s_initial = s_future
        
    if True:
        plot_E(E_0,E_freq,trans_freq,t_0,time_list)
        plot_pseudospin_time(s_list,time_list)
    plot_pseudospin(s_list)    
    
def main_rot_rk4():
    """
    Organizes constants and runs functions with rk4 integrator and calculates
    in rotating frame.
    """
    E_0 = 15000
    E_freq = 3.4e2 # 1/ps
    trans_freq = 3.4e2 # 1/ps
    dipole_mom = 10 * 5.29177*10**-5 # micro meters
    s_initial = np.matrix([[0],[0],[-1]]) # ground state
    time_step = 1/(20 * trans_freq) # ps
    stop_time = 1 # ps
    t_0 = 0.5 # ps, time at which pulse has max amplitude
    time_list = np.arange(0,stop_time,time_step)
    s_list = []
    
    for time in time_list:
        s_future = calculate_pseudospin_rot_rk4\
            (trans_freq,dipole_mom,s_initial,time,time_step,E_freq,E_0,t_0)
        s_list.append(s_future)
        s_initial = s_future
        
    if True:
        plot_E(E_0,E_freq,trans_freq,t_0,time_list)
        plot_pseudospin_time(s_list,time_list)
    plot_pseudospin(s_list)     
    
print("{:42s}{:>10s}".format("Pseudospin using Euler: ","main_euler()"))
print("{:42s}{:>10s}".format("Pseudospin using RK4: ","main_rk4()"))    
print("{:42s}{:>10s}".format("Pseudospin in rotating frame using rk4: "\
      ,"main_rot_rk4()"))    
    
