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

        self.game_turn = 1
        self.piece_move_num_limit = 0

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

    def show_game_status(self, current_turn_p_id):
        self.game_stage.show_stage()
        for p_id in self.game_player.get_id_list():
            self.show_player_turn_num(p_id)
        print("{0}ターン目".format(self.game_turn))
        print("---{0}のバンです---".format(self.game_player.game_player_list["id"][current_turn_p_id]["name"]))

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
                os.system("cls")
                self.show_game_status(c_turn_p_id)
                get_input = game_msg.selection_request({"入力": "続ける"})
                print("---コマを移動できる数を決めます---")
                if self.game_turn == 1:
                    print("最初のターンなので、サイコロを2回ふって出た数の合計になります")
                    game_msg.selection_request({"入力": "続ける"})
                    piece_move_num_limit = dice.dice(2)
                else:
                    print("サイコロをふって決めます")
                    game_msg.selection_request({"入力": "続ける"})
                    piece_move_num_limit = dice.dice(1)
                print("合計:{}".format(piece_move_num_limit))
                game_msg.selection_request({"入力": "続ける"})
                while 1:
                    os.system("cls")
                    self.show_game_status(c_turn_p_id)
                    print("---選んでください---")
                    get_input = game_msg.selection_request({"1": "コマを選択する", "p": "パス", "c": "終了"})
                    if get_input == "1":
                        try:
                            print("ヨコ")
                            get_x = int(input(">>> "))
                            if get_x < 0 or get_x > self.game_stage.get_stage_length()["x"]-1:
                                raise IndexError
                            print("タテ")
                            get_y = int(input(">>> "))
                            if get_y < 0 or get_y > self.game_stage.get_stage_length()["y"]-1:
                                raise IndexError
                            get_piece_data = self.game_stage.what_is_piece(get_x, get_y)
                        except ValueError:
                            print("---数字を入力してください---")
                            game_msg.selection_request({"入力": "続ける"})
                        except IndexError:
                            print("---0~7までの数字を入力してください---")
                            game_msg.selection_request({"入力": "続ける"})
                        else:
                            if get_piece_data:
                                print("コマ: {0} プレイヤー: {1}".format(get_piece_data["piece"], get_piece_data["player"]))
                                game_msg.selection_request({"入力": "続ける"})
                                if get_piece_data["player"] == self.game_player.game_player_list["id"][c_turn_p_id]["name"]:
                                    piece_x = get_x
                                    piece_y = get_y
                                    while 1:
                                        os.system("cls")
                                        self.show_game_status(c_turn_p_id)
                                        flag_move = False
                                        print("残りの移動できる数:{0}".format(piece_move_num_limit))
                                        get_input = game_msg.selection_request({"w": "↑", "a": "←", "s": "↓", "d": "→", "c": "やめる"})
                                        if get_input == "c":
                                            break
                                        elif get_input == "w" and piece_y > 0:
                                            get_piece_data = self.game_stage.what_is_piece(piece_x, piece_y-1)
                                            self.game_stage.move_piece(piece_x, piece_y,
                                                                       0, -1,
                                                                       self.game_player.game_player_list["id"][c_turn_p_id]["piece"]["foot_print"])
                                            piece_y = piece_y - 1
                                            flag_move = True
                                        elif get_input == "a" and piece_x > 0:
                                            get_piece_data = self.game_stage.what_is_piece(piece_x-1, piece_y)
                                            self.game_stage.move_piece(piece_x, piece_y,
                                                                       -1, 0,
                                                                       self.game_player.game_player_list["id"][c_turn_p_id]["piece"]["foot_print"])
                                            piece_x = piece_x - 1
                                            flag_move = True
                                        elif get_input == "s" and piece_y < self.game_stage.get_stage_length()["y"]-1:
                                            get_piece_data = self.game_stage.what_is_piece(piece_x, piece_y+1)
                                            self.game_stage.move_piece(piece_x, piece_y,
                                                                       0, 1,
                                                                       self.game_player.game_player_list["id"][c_turn_p_id]["piece"]["foot_print"])
                                            piece_y = piece_y + 1
                                            flag_move = True
                                        elif get_input == "d" and piece_x < self.game_stage.get_stage_length()["x"]-1:
                                            get_piece_data = self.game_stage.what_is_piece(piece_x+1, piece_y)
                                            self.game_stage.move_piece(piece_x, piece_y,
                                                                       1, 0,
                                                                       self.game_player.game_player_list["id"][c_turn_p_id]["piece"]["foot_print"])
                                            piece_x = piece_x + 1
                                            flag_move = True
                                        if flag_move:
                                            piece_move_num_limit = piece_move_num_limit - 1
                                            if get_piece_data:
                                                if not get_piece_data["player"] == self.game_player.game_player_list["id"][c_turn_p_id]["name"]:
                                                    enemy_piece_p_id = self.game_player.get_name_player_id(get_piece_data["player"])
                                                    if get_piece_data["king"] == self.game_player.game_player_list["id"][enemy_piece_p_id]["piece"]["king"]:
                                                        print("---{0}が操作しています---".format(get_piece_data["name"]))
                                                        print("---復活させる場所を選んでください---")
                                                        game_msg.selection_request({"1": "ヨコ:{0} タテ:{1}".format(self.game_player.game_player_list["id"][enemy_piece_p_id]["piece"]["spawn_point"][1],
                                                                                                                    self.game_player.game_player_list["id"][enemy_piece_p_id]["piece"]["spawn_point"][2])})
                            else:
                                print("コマがありません")
                                game_msg.selection_request({"入力": "続ける"})
                    elif get_input == "p":
                        break
                    elif get_input == "c":
                        sys.exit(0)
                self.game_turn = self.game_turn + 1

def main():
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
"""
    game = Game()
    game.run()
"""
