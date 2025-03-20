from mingus.containers import Note, NoteContainer
from mingus.midi import fluidsynth
import time


fluidsynth.init("SynthModule.sf2")  # You need a soundfont file

def play_chord(tones: list[str]):
    fluidsynth.stop_everything()
    fluidsynth.play_NoteContainer(NoteContainer(tones))
    print(f"Playing chord{tones}")

