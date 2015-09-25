------------
PYSTOCKFISH
------------

This wraps the Stockfish chess engine for easy integration into python.  Stockfish must
be executable at the root level.

Built on Ubuntu 12.1 tested with Stockfish 120212.

Information on the open-source Stockfish chess engine can be found at:
http://www.stockfishchess.org

--------
EXAMPLE:
--------
This is a Python console example.
```python
>>> from pystockfish import *  
>>> deep = Engine(depth=20)  
>>> deep.setposition(['e2e4'])  
>>> deep.bestmove()  
{'info': 'info depth 10 seldepth 13 score cp -40 nodes 33303 nps 951514 time 35 multipv 1 pv b8c6 g1f3 g8f6 b1c3 e7e5 f1b5 f8d6 e1g1 e8g8 d2d4 e5d4 f3d4 a7a6', 'ponder': 'g1f3', 'move': 'b8c6'}  

>>> deep.setposition(['e2e4','e7e5'])  
>>> deep.bestmove()  
{'info': 'info depth 10 seldepth 2 score cp 40 nodes 4230 nps 1057500 time 4 multipv 1 pv g1f3 g8f6 b1c3 b8c6 f1b5 f8d6 e1g1 e8g8 d2d4 e5d4 f3d4 a7a6', 'ponder': 'g8f6', 'move': 'g1f3'}  

>>> shallow = Engine(depth=10)  
>>> match = Match(engines={'deep': deep, 'shallow':shallow})  
>>> match.run()  
'deep'
```

bestmove() returns a dictionary object with the engine output as "info", the best move as 'move', and the opponents response as 'ponder.'
match.run() prints the name of the winning engine or "None" if there is a draw.

--------------
INSTALLATION:
--------------

This assumes that the command 'stockfish' is executable.
If you are running Ubuntu, run 'sudo apt-get install stockfish'

--------
DETAILS:
--------
The Engine class initiates the Stockfish chess engine with `Ponder` set to `False`.
`param` allows parameters to be specified by a dictionary object of `optionname` and `value`,
with value as an integer between 0 and 200.

i.e. the following explicitely sets the default parameters
```python
	{
		"Contempt Factor": 0,
		"Min Split Depth": 0,
		"Threads": 1,
		"Hash": 16,
		"MultiPV": 1,
		"Skill Level": 20,
		"Move Overhead": 30,
		"Minimum Thinking Time": 20,
		"Slow Mover": 80,
	}
```
If `rand` is set to `False`, any options not explicitely set will be set to the default 
value.

-------------------------
USING RANDOM PARAMETERS
-------------------------
Rand allows an engine's parameters to be randomly chosen when initialized.  This makes it easy
to run automated matches against slightly different engines.

If 'rand' is set to True, any of the above parameters not explicitely set will be randomly chosen
from a uniform distribution between rand_min and rand_max.

rand_min and rand_max are integers set between -10 and 10.
The option exists so that chess matches can be easily setup between non-idential engines.

*warning: Stockfish option names vary by version number.

-------------
Update Notes
-------------
* Version 0.1.5
* Pytockfish now complies with both: *Python2* and *Python3*.
