from pystockfish import *

results = {}
games_shallow_win_or_draw={}
for depth_var in range(5,10):
	for i in range(5):
		engines = {
		'shallow': Engine(depth=depth_var, rand=False),
		'deep': Engine(depth=10, rand=False),
		}
		m = Match(engines=engines)
		winner = m.run()
		if winner == 'deep':
			results[depth_var]=results.get(depth_var,0)+1
		elif winner == None:
			results[depth_var]=results.get(depth_var,0)+0.5
			print "draw", "white: %s \n" % m.white, movelisttostr(m.moves)
		else:
			print 'shallow', "white: %s \n" % m.white, movelisttostr(m.moves)
		print i
	print results