#Actual project file
#This is the main file, it handles I/O, and uses the brain for logic

# from mingus.midi import fluidsynth
# from mingus.containers import Note
# from mingus.containers import NoteContainer
# import mingus.core.chords as chords
# import mingus.core.scales as scales
# from time import sleep
from ImprovBrain import Brain

global brain

def setup():
	global brain
	brain = Brain()

def playNotesInList(listOfNotes):
	"""
	Plays musical notes from a list using mingus/fluidsynth

	Input form example: []
	"""

def main():
	global brain
	while True:
		nextNoteSequence = brain.getBar()


if __name__ == "__main__":
	setup()
	main()