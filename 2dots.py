#Generates file with two dots for simulation#

file = open("2dots.dat", "w")

res_freq = 2278.9013
decay_cons1 = 10
decay_cons2 = 10
d_str = "5.2917721d-4"
d1 = ['1d0','0d0','0d0']
d2 = ['d0','1d0','0d0']

print("0d0 0d0 0d0", res_freq, decay_cons1, decay_cons2,\
d_str, d1[0], d1[1], d1[2], file=file)
print("0d0 1d0 0d0", res_freq, decay_cons1, decay_cons2,\
d_str, d2[0], d2[1], d2[2], file=file)

file.close()