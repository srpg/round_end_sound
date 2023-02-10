import random, os
from core import GAME_NAME
from events import Event
from engines.sound import Sound
from stringtables.downloads import Downloadables
from filters.players import PlayerIter

sounds_path = os.listdir(f"{GAME_NAME}/sound/round_end_sound")

def load():
	dl = Downloadables()
	dl.add_directory('sound/round_end_sound')
		    
@Event('round_end')
def round_end(args):
	sounds = []
	for sound in sounds_path:
		sounds.append(sound)
	sound_to_play = random.choice(sounds)
	for player in PlayerIter('human'):
		Sound(f'round_end_sound/{sound_to_play}').play(player.index)