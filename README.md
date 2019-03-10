# Acoustic Modes Viewer (v0.1.1 alpha)

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
`pip install --index-url=https://test-pypi.org/simple acomod`

## Screenshots

![Screenshot](screenshot.png)

## Authors
Bartosz Lew (bartosz.lew@protonmail.com)
