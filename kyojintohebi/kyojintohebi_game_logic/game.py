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

        for p_id in self.game_player.get_id_list():
            for spawn_p_num in self.game_player.get_spawn_point_num_list(p_id):
                self.game_stage.put_piece(self.game_player.game_player_list["id"][p_id]["piece"]["spawn_point"][spawn_p_num]["x"],
                                          self.game_player.game_player_list["id"][p_id]["piece"]["spawn_point"][spawn_p_num]["y"],
                                          self.game_player.game_player_list["id"][p_id]["piece"]["king"],
                                          self.game_player.game_player_list["id"][p_id]["name"]
                                          )

    def select_player_turn(self, p_1_id, p_2_id):
        print("進める順番を決めてください")
        get_input = game_msg.selection_request({"入力": "ランダム", "1": " 1バン", "2": " 2バン"})
        if get_input == "1":
            self.game_player.set_turn_num(p_1_id, 1)
        elif get_input == "2":
            self.game_player.set_turn_num(p_2_id, 2)
        else:
            self.game_player.set_turn_num(random.randint(p_1_id, p_2_id), random.randint(1, 2))

    def run(self):
        self.select_player_turn(1, 2)

if __name__ == "__main__":
    game = Game()
    game.run()
