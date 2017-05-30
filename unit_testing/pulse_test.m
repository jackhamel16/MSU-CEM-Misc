syms t
r = sym(zeros(1,3));

amp = 15589.2260227;
delay = 5;
width = 227.89013;
freq = 2278.9013;
wavevector = [1 0 0];
polarization = [1 0 0];
dot_pos = [ 1 1 1 ];
dot_freq = 2278.9013;
t = 5.2;


arg = dot(wavevector,dot_pos) - freq * (t-delay);
pulse = amp/2 .* polarization .* exp(-(arg/width)^2/2);

% Pulse-dot interaction
dipole = [1 2 3];
hbar = 1;
dt = 0.2;

interaction = dot(pulse,dipole) / hbar