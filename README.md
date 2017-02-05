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
	members of the rings, then writing them to a file for sim use.
	
rings_method3.py : Complete

	Plots one ring in xy-plane at any z value by checking if points in the same plane are
	members of the rings, then appending them to a file for sim use.  Infinite rings can be
	put in one file with this script.

sz_plotter.py : Complete (additional functions may be added)
	
	Plots the value of sz for EACH dot in simulation with respect to timesteps.

bloch_data_grabber.py : Complete (additional functions may be added)

	Grabs the pseudospin data from all dots at any timestep.  this is useful in
	checking if the simulation is running as expected at different times.

uniform_dist_generator.py : Complete

	Generates dots in a specified cube using uniform random distribution algorithm in numpy.
	Writes to a file for use in sim.

dot_finder.py : WIP

	Finds the two lowest sz values at a specific timestep.  Then finds the corresponding
	dots and their positions.  Needs to be generalized still and better organized/commented.


