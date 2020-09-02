import random, soundlib
from events import Event
from stringtables.downloads import Downloadables

SOUNDS	= ['round_end_sound/deluxe16', 'round_end_sound/deluxe18', 'round_end_sound/deluxe20', 'round_end_sound/deluxe31', 'round_end_sound/deluxe43', 'round_end_sound/res_ctwin4', 'round_end_sound/res_twin1', 'round_end_sound/res_twin7', 'round_end_sound/rumble_intro', 'round_end_sound/shesafreak', 'round_end_sound/ufk3', 'round_end_sound/ufk4', 'round_end_sound/ufk5', 'round_end_sound/ufk6', 'round_end_sound/ufk7', 'round_end_sound/ufk8', 'round_end_sound/ufk13']

def load():
	setDL()
    
def setDL():
	dl = Downloadables()
	dl.add_directory('sound/round_end_sound')
		    
@Event('round_end')
def round_end(args):
	for userid in soundlib.getUseridList(): 
		soundlib.playgamesound(userid, random.choice(SOUNDS) + '.mp3')       
