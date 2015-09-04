from setuptools import setup

setup(
    name="pystockfish",
    author='Jarret Petrillo',
    author_email="iamjarret@gmail.com",
    version="0.1.5",
    license="GPL3",
    keywords="chess stockfish",
    url='http://www.github.com/iamjarret/pystockfish/',
    py_modules=["pystockfish"],
    description="Wraps the open-source Stockfish chess engine for easy integration into python.",
    long_description='''
    This integrates the Stockfish chess engine with python.  It allows the engine to be used
    by invoking an easy-to-use Engine class with synchronization handled automatically.

    >>> from pystockfish import *
    >>> deep = Engine(depth=20)
    >>> deep.setposition(['e2e4'])
    >>> deep.bestmove()
    {'info': 'info depth 10 seldepth 13 score cp -40
    nodes 33303 nps 951514 time 35 multipv 1 pv b8c6 g1f3 g8f6
    b1c3 e7e5 f1b5 f8d6 e1g1 e8g8 d2d4 e5d4 f3d4 a7a6',
    'ponder': 'g1f3',
    'move': 'b8c6'}
    >>> deep.setposition(['e2e4','e7e5'])
    >>> deep.bestmove()
    {'info': 'info depth 10 seldepth 2 score cp 40
    nodes 4230 nps 1057500 time 4 multipv 1 pv g1f3 g8f6
    b1c3 b8c6 f1b5 f8d6 e1g1 e8g8 d2d4 e5d4 f3d4 a7a6',
    'ponder': 'g8f6',
    'move': 'g1f3'}

    The package also implements a Match class to play chess two engines against one another.
    ''',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: Unix",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ])