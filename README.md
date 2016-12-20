# MSU-EMresearch-Misc

This repository is a storage space for various scripts written for use in EM research at MSU.

Current files:

Bloch_ODE_solver.py : Complete

	Solves the Bloch equations numerically using different integrators.	
	Plots the results as well.

emission_plotter.py : WIP

	Runs and plots Fourier Transform of three components of the electric
	field at the posiion of one of the dots from the sim results. Uses 
	emission.dats as source file.

input_generator_2Dsquare : Complete

	Creates a plane of dots parallel in xy-plane.  Some functions commented 
	out right now.

plane_plotter : Complete

	Generates a plane using mathematical equation of a plane.  Prints to a
	file for sim use and plots plane.

rings.py : Complete

	Plots a rings in xy-plane using parametric equations. Writes to file
	for sim use.

rings_method2.py : Complete

	Plots two rings in xy-plane by checking if points in the plane are
	members of the rings, then saving them to a file for sim use.

sz_plotter.py : Complete (additional functions may be added)
	
	Plots the value of sz for EACH dot in simulation with respect to timesteps.

bloch_data_grabber.py : Complete (additional functions may be added)

	Grabs the pseudospin data from all dots at any timestep.  this is useful in
	checking if the simulation is running as expected at different times.


np and plt are python modules.
