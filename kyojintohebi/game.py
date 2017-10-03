# -*- coding: utf-8 -*-
"""
Created on Thu 08/31/2017

@Author Junichi Suetsugu (末次 淳一)
"""

from kyojintohebi_game_logic.gamestage import GameStage
from kyojintohebi_game_logic.gameplayer import GamePlayerList
from kyojintohebi_game_logic import gamemessage as game_msg
from kyojintohebi_game_logic import dice
import sys
import os
import random

class Game:
    def __init__(self):
        self.name = ""
        self.stage = GameStage(8, 8)
        self.player = GamePlayerList()
        self.turn = 1
        self.piece_move_limit_num = 0

    def select_player_turn_num(self, player_id):
        turn_select_message = {"入力": "ランダム"}

        for turn_num in self.player.get_turn_num_list():
            turn_select_message[str(turn_num)] = "{0}バン".format(turn_num)
        get_input = game_msg.selection_request(turn_select_message)
        for turn_num in self.player.get_turn_num_list():
            if get_input == str(turn_num):
                self.player.set_turn_num(player_id,turn_num)
            elif not get_input:
                self.player.set_turn_num(player_id,random.randint(1,len(self.player.get_turn_num_list())))

    def show_game_status(self, player_id):
        self.stage.show_stage()
        print("{0}バン目".format(self.turn))
        print("---{0}のバン---".format(self.player.player_data["id"][player_id]["name"]))

    def roll_the_dice(self):
        if self.turn == 1:
            self.piece_move_limit_num = dice.dice(2)
        else:
            self.piece_move_limit_num = dice.dice(2)

"""
class Scene:
    def __init__(self):
        self.__scenes = []

    def get_scenes(self):
        return self.__scenes

    scenes = property(fget = get_scenes)

    def add_scene(self, function):
        self.scenes.append(function)

    def __callback(self, function, *args):
        return function(*args)

    def run(self):
        while True:
            for function in self.scenes:
                self.__callback(function)"""

def main():
    game = Game()
    game.player.add_player(1)
    game.player.set_name(1, "player1")
    game.player.set_piece(1, "king", "1@")
    game.player.set_piece(1, "foot_print", "1#")
    game.player.set_spawn_point(1, 1, 2, 2)
    game.player.set_spawn_point(1, 2, 5, 5)
    game.player.add_player(2)
    game.player.set_name(2, "player2")
    game.player.set_piece(2, "king", "2@")
    game.player.set_piece(2, "foot_print", "2#")
    game.player.set_spawn_point(2, 1, 2, 5)
    game.player.set_spawn_point(2, 2, 5, 2)
    for p_id in game.player.get_id_list():
        for point_num in game.player.get_spawn_point_num_list(p_id):
            game.stage.put_piece(
                     game.player.player_data["id"][p_id]["piece"]["spawn_point"][point_num]["x"],
                     game.player.player_data["id"][p_id]["piece"]["spawn_point"][point_num]["y"],
                     game.player.player_data["id"][p_id]["piece"]["king"],
                     game.player.player_data["id"][p_id]["name"])
    print("---{0}が操作してください---".format(game.player.player_data["id"][1]["name"]))
    print("ゲームを進める順番を決めてください")
    game.select_player_turn_num(1)
    scene = "roll the dice"
    while True:
        for c_turn_num in sorted(game.player.get_turn_num_list()):
            if scene == "roll the dice":
                c_turn_num_in_player = game.player.get_turn_num_in_player()
                c_player_id = c_turn_num_in_player[c_turn_num]
                os.system("cls")
                game.show_game_status(c_player_id)
                get_input = game_msg.selection_request({"入力": "続行", "c": "終了"})
                if get_input == "c":
                    sys.exit(0)
                print("---コマを動かせる回数を決めます---")
                get_input = game_msg.selection_request({"入力": "続行"})
                print("数字が1~6のサイコロを振って出た数になります")
                if game.turn == 1:
                    print("最初のバンなので2回振って出た数の合計になります")
                game.roll_the_dice()
                print("-結果:\n-残り移動数:{0}".format(game.piece_move_limit_num))
                input()
                scene = "select command"
            while scene == "select command":
                os.system("cls")
                game.show_game_status(c_player_id)
                print("---選択してください---")
                get_input = game_msg.selection_request({"1": "コマを選択する", "2": "パス", "c": "降伏"})
                if get_input == "1":
                    scene = "select piece"
                elif get_input == "2":
                    scene = "roll the dice"
                    break
                elif get_input == "c":
                    print("降伏して負けを認めます。本当に良いですか?")
                    get_input = game_msg.selection_request({"1": "降伏する", "c": "やめる"})
                    if get_input == "1":
                        scene = surrender
                    elif get_input == "c":
                        continue
            while scene == "select piece":
                os.system("cls")
                game.show_game_status(c_player_id)
                print("---コマの場所を指定してください---")
                try:
                    get_input_x = int(input("ヨコ >>> "))
                    if not -1 < get_input_x < game.stage.get_stage_length()["x"]:
                        raise ValueError
                    get_input_y = int(input("タテ >>> "))
                    if not -1 < get_input_y < game.stage.get_stage_length()["y"]:
                        raise ValueError
                except ValueError:
                    print("ヨコ0~{0},タテ0~{1} の数字を入力してください".format(game.stage.get_stage_length()["x"]-1,game.stage.get_stage_length()["y"]-1))
                    input()
                else:
                    get_piece = game.stage.what_is_piece(get_input_x, get_input_y)
                    if get_piece:
                        print("コマ:{0} プレイヤー:{1}".format(get_piece["piece"], get_piece["player"]))
                        input()
                        if get_piece["player"] == game.player.player_data["id"][c_player_id]["name"]:
                            if get_piece["piece"] == game.player.player_data["id"][c_player_id]["piece"]["king"]:
                                piece_x = get_input_x
                                piece_y = get_input_y
                                scene = "select piece command"
                        else:
                            print("コマがありません")
                            scene = "select command"
                        break
            while scene == "select piece command":
                piece_x_move_num = 1
                piece_y_move_num = 1
                os.system("cls")
                game.show_game_status(c_player_id)
                print("残り移動数:{0}".format(game.piece_move_limit_num))
                print("---選択してください---")
                get_input = game_msg.selection_request({"w": "↑", "a": "←", "s": "↓", "d": "→", "c": "やめる"})
                if get_input == "w" and piece_y > 0:
                    game.stage.move_piece(piece_x, piece_y, 0, -piece_y_move_num, game.player.player_data["id"][c_player_id]["piece"]["foot_print"])
                    piece_y -= piece_y_move_num
                elif get_input == "a" and piece_x > 0:
                    game.stage.move_piece(piece_x, piece_y, -piece_x_move_num, 0, game.player.player_data["id"][c_player_id]["piece"]["foot_print"])
                    piece_x -= piece_x_move_num
                elif get_input == "s" and piece_y < game.stage.get_stage_length()["y"]-1:
                    game.stage.move_piece(piece_x, piece_y, 0, piece_y_move_num, game.player.player_data["id"][c_player_id]["piece"]["foot_print"])
                    piece_y += piece_y_move_num
                elif get_input == "d" and piece_x < game.stage.get_stage_length()["x"]-1:
                    game.stage.move_piece(piece_x, piece_y, piece_x_move_num, 0, game.player.player_data["id"][c_player_id]["piece"]["foot_print"])
                    piece_x += piece_x_move_num
                elif get_input == "c":
                    scene = "select command"
            while scene == "surrender":
                game_msg.selection_request({"入力": "終了"})
                sys.exit(0)
        game.turn += 1


if __name__ == "__main__":
    main()
