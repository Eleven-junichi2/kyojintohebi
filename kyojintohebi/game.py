# -*- coding: utf-8 -*-
"""
Created on Thu 08/31/2017

@Author Junichi Suetsugu (末次 淳一)
"""

from kyojintohebi_game_logic.gamestage import GameStage
from kyojintohebi_game_logic.gameplayer import GamePlayerList
from kyojintohebi_game_logic import gamemessage as game_msg
#from kyojintohebi_game_logic import dice
import random
import sys
import os

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

    def select_player_turn(self, selecter_p_id, p_2_id):
        print("進める順番を決めてください")
        get_input = game_msg.selection_request({"入力": "ランダム", "1": " 1バン", "2": " 2バン"})
        if get_input == "1":
            self.game_player.set_turn_num(selecter_p_id, 1)
        elif get_input == "2":
            self.game_player.set_turn_num(selecter_p_id, 2)
        else:
            self.game_player.set_turn_num(random.randint(selecter_p_id, p_2_id), random.randint(1, 2))

    def show_player_turn_num(self, p_id):
        print("{0}: {1}バン".format(self.game_player.game_player_list["id"][p_id]["name"],
                                  self.game_player.game_player_list["id"][p_id]["turn_num"]
                                 )
             )

    def show_game_status(self):
        self.game_stage.show_stage()
        for p_id in self.game_player.get_id_list():
            self.show_player_turn_num(p_id)

    def run(self):
        print("---{0}が操作しています---".format(self.game_player.game_player_list["id"][1]["name"]))
        self.select_player_turn(1, 2)
        for p_id in self.game_player.get_id_list():
            self.show_player_turn_num(p_id)
        game_msg.selection_request({"入力": "始める"})
        turn_num_in_p = self.game_player.get_turn_num_in_player()

        while 1:
            for p_turn_num in sorted(self.game_player.get_turn_num_list()):
                c_turn_p_id = turn_num_in_p[p_turn_num]
                while 1:
                    os.system("cls")
                    self.show_game_status()
                    print("---{0}のバンです---".format(self.game_player.game_player_list["id"][c_turn_p_id]["name"]))
                    get_input = game_msg.selection_request({"入力": "続ける"})
                    if get_input == "c":
                        sys.exit(0)
                    print("---選んでください---")
                    get_input = game_msg.selection_request({"1": "コマを選択する", "2": "パス", "c": "終了"})
                    if get_input == "1":
                        try:
                            print("ヨコ")
                            get_x = int(input(">>> "))
                            if get_x < 0:
                                raise IndexError
                            print("タテ")
                            get_y = int(input(">>> "))
                            if get_y < 0:
                                raise IndexError
                            print(self.game_stage.what_is_piece(get_x, get_y))
                            get_input = game_msg.selection_request({"入力": "続ける"})
                        except ValueError:
                            print("数字を入力してください")
                            get_input = game_msg.selection_request({"入力": "続ける"})
                        except IndexError:
                            print("0~7までの数字を入力してください")
                            get_input = game_msg.selection_request({"入力": "続ける"})
                    elif get_input == "2":
                        break
                    elif get_input == "c":
                        sys.exit(0)

def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
"""
    game = Game()
    game.run()
"""
