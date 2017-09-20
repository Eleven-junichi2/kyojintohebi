# -*- coding:utf-8 -*-

"""
Created on 07/25/2017 JTS

@Author Junichi Suetsugu (末次 淳一)z
"""
class GameStage(object):
    """ボードゲームの盤(stage)のオブジェクトです。
    """
    def __init__(self, x=2, y=2, empty_square="__"):
        """初期化メソッドです。

        Args:
            x(int):
            y(int):
            empty_square(str):
        """
        self.__stage_squares = []
        self.__empty_square = empty_square
        for i in range(y):
            self.__stage_squares.append([{"piece": self.empty_square, "player": "0"} for j in range(x)])
        self.__stage_length = {"x": len(self.__stage_squares), "y": len(self.__stage_squares[0])}

    def get_stage_squares(self):
        return self.__stage_squares

    stage_squares = property(fget=get_stage_squares)

    def get_empty_square(self):
        return self.__empty_square

    def set_empty_square(self, empty_square):
        if isinstance(empty_square, str):
            self.__empty_square = empty_square
        else:
            raise TypeError

    empty_square = property(get_empty_square, set_empty_square)

    def get_stage_length(self):
        return self.__stage_length

    stage_length = property(fget=get_stage_length)

    def put_piece(self, x, y, piece, player):
        """この関数は stage_squaresアトリビュート の指定された要素に piece と player を代入します。

        Args:
            x(int):
            y(int):
            piece(string):
            player(string):
        """
        piece = "_"*(len(self.empty_square) - len(piece)) + piece
        self.stage_squares[y][x]["piece"] = piece
        self.stage_squares[y][x]["player"] = player

    def del_piece(self, x, y):
        """stage_squaresアトリビュート の指定された要素に empty_squareアトリビュートに代入します。

        Args:
            x(int):
            y(int):
        """
        self.stage_squares[y][x] = {"piece": self.empty_square, "player": "0"}

    def move_piece(self, x, y, moving_num_x = 0, moving_num_y = 0, foot_print = ""):
        """ステージの指定された駒を移動します

        Args:
            x(int):
            y(int):
            moving_num_x(int):
            moving_num_y(int):
            foot_print(str): 移動の跡ができます。空の場合は移動の跡はできません。
        """
        self.put_piece(x + moving_num_x, y + moving_num_y, self.stage_squares[y][x]["piece"], self.stage_squares[y][x]["player"])
        if not foot_print:
            self.del_piece(x, y)
        elif foot_print:
            self.put_piece(x, y, foot_print, self.stage_squares[y + moving_num_y][x + moving_num_x]["player"])
    def what_is_piece(self, x, y):
        """この関数は stage_squaresアトリビュート の指定された要素を返します。

        Returns:
            dictionary:

        """
        if self.stage_squares[y][x]["piece"] == self.empty_square:
            piece = None
        else:
            piece = self.stage_squares[y][x]
        return piece

    def show_stage(self, delimiter = "|"):
        """stage_squaresアトリビュート を整形して表示します
        """
        j = []
        for i in range(len(self.stage_squares[0])):
            j.append(self.empty_square+str(i))
        print("+"+"".join(j)+"_")
        for i, square in enumerate(self.stage_squares):
            print(str(i)+delimiter+delimiter.join([j["piece"] for j in square])+"|")

def main():
    """
    モジュールを直接実行した際のエントリポイントです。
    """
    game_stage = GameStage(8, 8, empty_square='__')
    game_stage.put_piece(2, 2, "1p", "1")
    game_stage.show_stage()
    game_stage.move_piece(2, 2, 1)
    game_stage.show_stage()

if __name__ == "__main__":
    main()
