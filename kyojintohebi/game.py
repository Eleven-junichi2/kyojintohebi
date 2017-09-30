# -*- coding: utf-8 -*-
"""
Created on Thu 08/31/2017

@Author Junichi Suetsugu (末次 淳一)
"""

from kyojintohebi_game_logic.gamestage import GameStage
from kyojintohebi_game_logic.gameplayer import GamePlayerList
from kyojintohebi_game_logic import gamemessage as game_msg
from kyojintohebi_game_logic import dice
import random
import sys
import os

class Game:
    def __init__(self):
        self.stage = GameStage(8, 8)
        self.player = GamePlayerList()

def main():
    game = Game()


if __name__ == "__main__":
    main()
"""
    game = Game()
    game.run()
"""
