
SETUP

This program requires:
     - The mingus python libray
     - FluidSynth
     - A soundfont file(set of sounds to play with)


To install Mingus(which belongs to PyPi), I reccomend using pip in a virtual environment(so as not to clutter your system version of python):
	
	pip install mingus

On OSX I used homebrew to install FluidSynth(Note: this is not the python library named pyFluidSynth, this is FluidSynth itself):

	brew install fluidsynth

Soundfont files can be found all over. Think of them as the kit, or set of sounds for each note, that FluidSynth uses to play the notes that mingus calls upon it to play