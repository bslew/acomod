# Acoustic Modes Viewer (v0.1 alpha)

This program is a simple viewer of power spectral density of sound. 
The package provides a module and a program to trace Fourier acoustic modes and resonance frequencies of excited bodies.

## Use cases
* estimate length of an excited metal bar, guitar string, or 
* measure frequency of flute tones, 
* identify resonance frequencies and through provided sound speed the corresponding length scales of mechanical components that generate unwanted resonances (e.g. in a car as a function of speed cs)
* test 1/f noise and microphonic effects in electrical devices the program runs on.


## Features
* Analysis of sound from microphone or from a file (WAV format)
* To analyze transient signals it keeps track of maximal peaks in processed spectra 
* Saves recorded and processed data to files for further analysis
* Outputs list of peak frequencies (f) and corresponding wavelengths (l=cs/f)

### Features that will be implemented 
* Save animations of PSD response for video files (not implemented yet)

## Installation
	`pip3 install acomod`

## Screenshots

![Screenshot](screenshot.png)

## Troubleshooting
##### 	**acoustic_mode_viewer givens core dump on start**<br>
	<br>
	When you pip3 install acomod in virtual environment or locally via --user option Qt platform plugin may fail to be properly initialized due to incorrect configuration of LD_LIBRARY_PATH environment variable (under linux) pointing location of Qt libraries installed most likely somewhere in the system directories. If version of those is not the one required by the PyQt5 the program will fail with<br>
	`"This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem."`, <br>
	a message that typically is not even printed out to the terminal.<br><br><br>
	**Solution**:
		Provide the correct path to the Qt shared libraries: e.g.<br>
				
	`export LD_LIBRARY_PATH=/path/to/venv/lib/python3.6/site-packages/PyQt5/Qt/lib:$LD_LIBRARY_PATH` 
or in case of `pip install acomod --user`
				
			export LD_LIBRARY_PATH=$HOME/.local/lib/python3.6/site-packages/PyQt5/Qt/lib/python3.6/site-packages/PyQt5/Qt/lib:$LD_LIBRARY_PATH
	
## Authors
Bartosz Lew (bartosz.lew@protonmail.com)
