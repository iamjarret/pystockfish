"""
    pystockfish
    ~~~~~~~~~~~~~~~

    Wraps the Stockfish chess engine.  Assumes stockfish is
    executable at the root level.

    Built on Ubuntu 12.1 tested with Stockfish 120212.
    
    :copyright: (c) 2013 by Jarret Petrillo.
    :license: GNU General Public License, see LICENSE for more details.
"""

import subprocess
from random import randint

class Match:
	'''
	The Match class setups a chess match between two specified engines.  The white player
	is randomly chosen.

	deep_engine = Engine(depth=20)
	shallow_engine = Engine(depth=10)
	engines = {
		'shallow': shallow_engine,
		'deep': deep_engine,
		}

	m = Match(engines=engines)

	m.move() advances the game by one move.
	
	m.run() plays the game until completion or 200 moves have been played,
	returning the winning engine name.
	'''
	def __init__(self, engines):
		random_bin = randint(0,1)
		self.white = engines.keys()[random_bin]
		self.black = engines.keys()[not random_bin]
		self.white_engine = engines.get(self.white)
		self.black_engine = engines.get(self.black)
		self.moves = []
		self.white_engine.newgame()
		self.black_engine.newgame()
		self.winner = None
		self.winner_name = None

	def move(self):
		if len(self.moves)>200:
			return False
		elif len(self.moves) % 2:
			active_engine = self.black_engine
			active_engine_name = self.black
			inactive_engine = self.white_engine
			inactive_engine_name = self.white
		else:
			active_engine = self.white_engine
			active_engine_name = self.white
			inactive_engine = self.black_engine
			inactive_engine_name = self.black
		active_engine.setposition(self.moves)
		movedict=active_engine.bestmove()
		bestmove = movedict.get('move')
		info = movedict.get('info')
		ponder = movedict.get('ponder')
		self.moves.append(bestmove)
		
		if ponder != '(none)': return True
		else:
			mateloc = info.find('mate')
			if mateloc>=0:
				matenum = int(info[mateloc+5])
				if matenum>0:
					self.winner_engine = active_engine
					self.winner=active_engine_name
				elif matenum<0: 
					self.winner_engine=inactive_engine
					self.winner=inactive_engine_name
			return False

	def run(self):
		'''
		Returns the winning chess engine or "None" if there is a draw.
		'''
		while self.move(): pass
		return self.winner

class Engine(subprocess.Popen):
	'''
	This initiates the Stockfish chess engine with Ponder set to False.
	'param' allows parameters to be specified by a dictionary object with 'Name' and 'value'
	with value as an integer between 0 and 200.

	i.e. the following explicitely sets the default parameters
	{
		'Mobility (Middle Game)': 100,
		'Mobility (Endgame)': 100,
		'Passed Pawns (Middle Game)': 100,
		'Passed Pawns (Endgame)': 100,
		'Space': 100,
		'Aggressiveness': 100,
		'Cowardice': 100
	}

	If 'rand' is set to False, any options not explicitely set will be set to the default 
	value of 100.

	-----
	USING RANDOM PARAMETERS
	-----
	Rand allows an engine's parameters to be randomly chosen when initialized.  This makes it easy
	to run automated matches against slightly different engines.

	If 'rand' is set to True, any of the above parameters not explicitely set will be randomly chosen
	from a uniform distribution between rand_min and rand_max.

	rand_min and rand_max are integers set between 0 and 200.
	The reason this option exists is because engine parameters effect the engine's strength
	nontrivially.  Depth should be the main determinator of engine strength; rand is 
	used so that matches are not between clone engines.	
	'''
	def __init__(self, depth=2, ponder=False, param={}, rand=False, rand_min=90, rand_max=110):
		subprocess.Popen.__init__(self, 
			'stockfish',
			universal_newlines=True,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,)
		self.depth = str(depth)
		self.ponder = ponder
		self.put('uci')
		if not ponder:
			self.setoption('Ponder', False)

		if rand:
			base_param= {
			'Mobility (Middle Game)': randint(rand_min,rand_max),
			'Mobility (Endgame)': randint(rand_min,rand_max),
			'Passed Pawns (Middle Game)': randint(rand_min,rand_max),
			'Passed Pawns (Endgame)': randint(rand_min,rand_max),
			'Space': randint(rand_min,rand_max),
			'Aggressiveness': randint(rand_min,rand_max),
			'Cowardice': randint(rand_min,rand_max)
			}
		else:
			base_param={
			'Mobility (Middle Game)': 100,
			'Mobility (Endgame)': 100,
			'Passed Pawns (Middle Game)': 100,
			'Passed Pawns (Endgame)': 100,
			'Space': 100,
			'Aggressiveness': 100,
			'Cowardice': 100
			}

		base_param.update(param)
		self.param = base_param
		for name,value in base_param.items():
			self.setoption(name,value)

	def newgame(self):
		'''
		Calls 'ucinewgame' - this should be run before a new game
		'''
		self.put('ucinewgame')
		self.isready()

	def put(self, command):
		self.stdin.write(command+'\n')

	def flush(self):
		self.stdout.flush()

	def setoption(self,optionname, value):
		self.put('setoption name %s value %s'%(optionname,str(value)))
		stdout = self.isready()
		if stdout.find('No such')>=0:
			raise ValueError(stdout)

	def setposition(self, moves=[]):
		'''
		Move list is a list of moves (i.e. ['e2e4', 'e7e5', ...]) each entry as a string.  Moves must be in full algebraic notation.
		'''
		self.put('position startpos moves %s'%self._movelisttostr(moves))

	def go(self):
		self.put('go depth %s'%self.depth)

	def _movelisttostr(self,moves):
		'''
		Concatenates a list of strings
		'''
		movestr = ''
		for h in moves:
			movestr += h + ' '
		return movestr.strip()

	def bestmove(self):
		last_line = ""
		self.go()
		while True:
			text = self.stdout.readline().strip()
			split_text = text.split(' ')
			if split_text[0]=='bestmove':
				return {'move': split_text[1],
						'ponder': split_text[3],
						'info': last_line
						}
			last_line = text

	def isready(self):
		'''
		Used to synchronize the python engine object with the back-end engine.  Sends 'isready' and waits for 'readyok.'
		'''
		self.put('isready')
		lastline = ''
		while True:
			text = self.stdout.readline().strip()
			if text == 'readyok':
				return lastline
			lastline = text

