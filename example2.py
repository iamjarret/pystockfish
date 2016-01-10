# -*- coding: utf-8 -*-

from pystockfish import *
import pprint

solver = Engine(depth=20)

solver.setfenposition("r2qkb1r/pb3ppp/1pn2n2/3pp1B1/3P4/2N1PN2/PP3PPP/2RQKB1R w Kkq e6 0 9")
best_move = solver.bestmove()

pprint.pprint(best_move)

#output:
#
#{'info': {'depth': 20,
#          'multipv': 1,
#          'nodes': 8465413,
#          'nps': 539610,
#          'pv': ['d4e5',
#                 'h7h6',
#                 'g5f6',
#                 'g7f6',
#                 'c3d5',
#                 'f8b4',
#                 'd5b4',
#                 'd8d1',
#                 'c1d1',
#                 'c6b4',
#                 'f1b5',
#                 'b7c6',
#                 'b5c6',
#                 'b4c6',
#                 'e5f6',
#                 'a8d8',
#                 'd1d8',
#                 'c6d8',
#                 'e1e2',
#                 'h8g8',
#                 'h1c1',
#                 'g8g2',
#                 'c1c7',
#                 'g2g6',
#                 'c7e7',
#                 'e8f8',
#                 'e7a7',
#                 'g6f6',
#                 'f3e5'],
#          'score': {'cp': 311},
#          'seldepth': 38,
#          'tbhits': '0',
#          'time': 15688},
# 'move': 'd4e5',
# 'ponder': 'h7h6'}
