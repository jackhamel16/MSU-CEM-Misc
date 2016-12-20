import matplotlib.pyplot as plt


bloch_file = open("../sim_results/run3/bloch.dat")

time_list = []
s_list = []

for line in bloch_file:
    line_list = line.split()
    time_list.append(line_list[0])
    s_list.append(line_list[1:])

bloch_file.close()

count = 0
figure = plt.figure()
axes = figure.add_subplot(111)
axes.set_title("Pseudospin-Z of all system dots")
axes.set_xlabel("Time")
axes.set_ylabel("Pseudospin-Z")

for dot in range(len(s_list)//3):
    dot1 = [time[2+dot*3] for time in s_list]
    axes.plot(dot1)