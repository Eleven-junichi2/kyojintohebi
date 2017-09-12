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
    
class Game:
    def __init__(self):
        self.game_stage = GameStage(8, 8)
        self.game_player = GamePlayerList()

        self.game_player.add_player(1)
        self.game_player.set_name(1, "player1")
        self.game_player.set_piece(1, "king", "1@")
        self.game_player.set_piece(1, "foot_print", "1#")
        self.game_player.set_spawn_point(1, 1, 2, 2)
        self.game_player.set_spawn_point(1, 2, 5, 5)

        self.game_player.add_player(2)
        self.game_player.set_name(2, "player2")
        self.game_player.set_piece(2, "king", "2@")
        self.game_player.set_piece(2, "foot_print", "2#")
        self.game_player.set_spawn_point(2, 1, 2, 5)
        self.game_player.set_spawn_point(2, 2, 5, 2)

if __name__ == "__main__":
    game = Game()
