from mingus.midi import fluidsynth
from mingus.containers import Note
from mingus.containers import NoteContainer
import mingus.core.chords as chords
import mingus.core.scales as scales
from time import sleep

# initialize fluidsynth
def init_program():
	fluidsynth.init("soundfontfiles/velocitygrand.sf2", "coreaudio")

def play_c5_scale():
	c5scale = [Note(x+"-5") for x in "CDEFGAB"]
	c5scale.append(Note("C-6"))

	for note in c5scale:
		fluidsynth.play_Note(note)
		sleep(0.5)

def play_all_major_chords():
	s = scales.Ionian("C",1).ascending() # ["C","D","E",...,"C"]
	for root_note in s:
		# Create a Container(multiple notes to be played simultaneously)
		nc = NoteContainer(chords.major_triad(root_note))
		fluidsynth.play_NoteContainer(nc)
		sleep(0.75)

if __name__ == "__main__":
	init_program()
	play_all_major_chords()