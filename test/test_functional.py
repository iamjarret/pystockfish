from pystockfish import *


def quick_checkmate_test():
    # 1. e4 e5 2. Bc4 Nc6 3. Qf3 d6
    e1 = Engine(depth=6)
    e2 = Engine(depth=6)

    # match creation must be before calling setposition as Match.__init__ resets position
    m = Match(engines={"e1": e1, "e2": e2})

    e1.setposition(['e2e4', 'e7e5', 'f1c4', 'b8c6', 'd1f3', 'd7d6'])
    e2.setposition(['e2e4', 'e7e5', 'f1c4', 'b8c6', 'd1f3', 'd7d6'])

    m.run()
    assert m.winner in {"e1", "e2"}
 
