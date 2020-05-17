import os, path, random, soundlib
from events import Event
from stringtables.downloads import Downloadables

__FILEPATH__	= path.path(__file__).dirname()
DOWNLOADLIST_PATH	= os.path.join(__FILEPATH__ + '/download/download.txt')

def load():
	setDL()
    
def setDL():
	downloadables = Downloadables()
	with open(DOWNLOADLIST_PATH) as f:
		for line in f:
			line = line.strip()
			if not line:
				continue
			downloadables.add(line)
		    
@Event('round_end')
def round_end(args):
	for userid in soundlib.getUseridList():
		pow = random.randint(1, 17)        
		if pow == 1:
			soundlib.playgamesound(userid, 'round_end_sound/deluxe16.mp3') 
		if pow == 2:
			soundlib.playgamesound(userid, 'round_end_sound/deluxe18.mp3')
		if pow == 3:
			soundlib.playgamesound(userid, 'round_end_sound/deluxe20.mp3') 
		if pow == 4:
			soundlib.playgamesound(userid, 'round_end_sound/deluxe31.mp3')
		if pow == 5:
			soundlib.playgamesound(userid, 'round_end_sound/deluxe43.mp3') 
		if pow == 6:
			soundlib.playgamesound(userid, 'round_end_sound/res_ctwin4.mp3')
		if pow == 7:
			soundlib.playgamesound(userid, 'round_end_sound/res_twin1.mp3') 
		if pow == 8:
			soundlib.playgamesound(userid, 'round_end_sound/res_twin7.mp3')
		if pow == 9:
			soundlib.playgamesound(userid, 'round_end_sound/rumble_intro.mp3') 
		if pow == 10:
			soundlib.playgamesound(userid, 'round_end_sound/shesafreak.mp3')
		if pow == 11:
			soundlib.playgamesound(userid, 'round_end_sound/ufk3.mp3') 
		if pow == 12: 
			soundlib.playgamesound(userid, 'round_end_sound/ufk4.mp3')
		if pow == 13:
			soundlib.playgamesound(userid, 'round_end_sound/ufk5.mp3') 
		if pow == 14:
			soundlib.playgamesound(userid, 'round_end_sound/ufk6.mp3')
		if pow == 15:
			soundlib.playgamesound(userid, 'round_end_sound/ufk7.mp3') 
		if pow == 16:
			soundlib.playgamesound(userid, 'round_end_sound/ufk8.mp3')
		if pow == 17:
			soundlib.playgamesound(userid, 'round_end_sound/ufk13.mp3')          