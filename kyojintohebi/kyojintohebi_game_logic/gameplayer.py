# -*- coding: utf-8 -*-
"""
Created on Fri 09/01/2017 JTS

@Author: Junichi Suetsugu (末次 淳一)
"""
class GamePlayerList:
    """description of class"""
    def __init__(self):
        self.__game_player_list = {"id": {}}

    def get_game_player_list(self):
        return self.__game_player_list

    game_player_list = property(fget=get_game_player_list)


    def add_player(self, player_id):
        self.game_player_list["id"].update({player_id: {
            "name": "",
            "turn_num": player_id,
            "piece": {
                "king": "",
                "foot_print": "",
                "spawn_point": {1: {"x": 0, "y": 0},2: {"x": 0, "y": 0}}
                }
            }
                                           })

    def exchange_turn_num(self, p1_id, p2_id):
        p1_turn_num = self.game_player_list["id"][p1_id]["turn_num"]
        p2_turn_num = self.game_player_list["id"][p2_id]["turn_num"]
        self.game_player_list["id"][p1_id]["turn_num"] = p2_turn_num
        self.game_player_list["id"][p2_id]["turn_num"] = p1_turn_num


    def set_turn_num(self, player_id, turn_num):
        for p_id in self.get_id_list():
            if self.game_player_list["id"][p_id]["turn_num"] == turn_num:
                self.game_player_list["id"][p_id]["turn_num"] = self.game_player_list["id"][player_id]["turn_num"]
                break
        self.game_player_list["id"][player_id]["turn_num"] = turn_num

    def get_turn_num_in_player(self):
        """

        Returns:
            turn_num_in_player: {turn_num: player_id, …}
        """
        turn_num_in_player = {}
        for p_id in self.get_id_list():
            turn_num_in_player[self.game_player_list["id"][p_id]["turn_num"]] = p_id
        return turn_num_in_player

    def get_turn_num_list(self):
        return list(self.get_turn_num_in_player().keys())

    def sort_turn_num(self):
        turn_num_list = self.get_turn_num_list()
        turn_num_list.sort()
        for p_id, turn_num in zip(self.get_id_list(), turn_num_list):
            self.game_player_list["id"][p_id]["turn_num"] = turn_num

    def set_name(self, player_id, name):
        self.game_player_list["id"][player_id]["name"] = name

    def set_piece(self, id, piece_type, piece):
        if not piece_type == "spawn_point":
            self.game_player_list["id"][id]["piece"][piece_type] = piece
        else:
            raise ValueError("Can't set spawn_point.")

    def set_spawn_point(self, id, point_num, x, y):
        self.game_player_list["id"][id]["piece"]["spawn_point"][point_num]["x"] = x
        self.game_player_list["id"][id]["piece"]["spawn_point"][point_num]["y"] = y

    def get_data_type_list(self, id):
        return list(self.game_player_list["id"][id].keys())

    def get_id_list(self):
        return list(self.game_player_list["id"].keys())

    def get_spawn_point_num_list(self, id):
        return list(self.game_player_list["id"][id]["piece"]["spawn_point"].keys())

    def get_name_player_id(self, name):
        for player_id in self.get_id_list():
            if self.game_player_list["id"][player_id]["name"] == name:
                return player_id

if __name__ == "__main__":
    game_player = GamePlayerList()
    game_player.add_player(1)
    game_player.set_name(1, "junichi")
    game_player.add_player(2)
    game_player.set_name(2, "yuma")
    game_player.add_player(3)
    game_player.set_name(3, "python")
    game_player.exchange_turn_num(1, 3)
    print(game_player.get_turn_num_in_player())
    game_player.sort_turn_num()
    print(game_player.get_turn_num_in_player())
