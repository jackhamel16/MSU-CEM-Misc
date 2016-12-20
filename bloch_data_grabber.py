
"""
grabs data from bloch.dat
"""

bloch_file = open("../sim_results/bloch.dat")

time_list = []
s_list = []

for line in bloch_file:
    line_list = line.split()
    time_list.append(line_list[0])
    s_list.append(line_list[1:])

bloch_file.close()
# s components at first time step
sx = [float(x) for i,x in enumerate(s_list[0]) if i in range(0,300,3)]
sy = [float(x) for i,x in enumerate(s_list[0]) if i in range(1,300,3)]
sz = [float(x) for i,x in enumerate(s_list[0]) if i in range(2,300,3)]

