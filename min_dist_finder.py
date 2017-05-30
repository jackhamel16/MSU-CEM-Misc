import numpy as np

dots_file = open("../sim_results/run16/dots.dat")

def get_coordinates(dots_file):
    """
    grabs coordinates of dots from a dots file
    returns n x 3 array of coordinates
    """
    dots_line_list = [line for line in dots_file]
    dot_pos_array = np.zeros((50,3))
    
    dot_count = 0
    for line in dots_line_list:
        line_list = line.split()
        dot_pos_array[dot_count][0] = line_list[0]
        dot_pos_array[dot_count][1] = line_list[1]
        dot_pos_array[dot_count][2] = line_list[2]
        dot_count += 1
        if dot_count > 49:
            break
        
    return dot_pos_array
    
def calculate_min_distance(dot_array):
    """
    Calculates the minimum distance between two dots in the distribution
    dot_array n x 3 array of dot positions
    returns minimum distance
    """
    min_distance = 10000000 # Needs to be a value greater than the likely min distance
    
    for dot in dot_array:
        x_dot,y_dot,z_dot = dot[0],dot[1],dot[2]
        for dot in dot_array:
            x_dist = x_dot - dot[0]
            y_dist = y_dot - dot[1]
            z_dist = z_dot - dot[2]
            distance = np.sqrt(x_dist**2+y_dist**2+z_dist**2)
            if (distance != 0) and distance < min_distance:
                min_distance = distance
                
    return min_distance
    
def main():
    dots_file = open("../sim_results/run16/dots.dat")
    
    dot_array = get_coordinates(dots_file)
    dots_file.close()
    
    min_dist = calculate_min_distance(dot_array)
    
    print("Minimum separation in distribution is: ", str(min_dist))
    
    