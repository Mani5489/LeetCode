class Solution:
    def checkValues(self, player, maps) -> bool:
        if maps.get((0, 0)) == maps.get((0, 1)) == maps.get((0, 2)) == player:
            return True
        if maps.get((1, 0)) == maps.get((1, 1)) == maps.get((1, 2)) == player:
            return True
        if maps.get((2, 0)) == maps.get((2, 1)) == maps.get((2, 2)) == player:
            return True
        if maps.get((0, 0)) == maps.get((1, 0)) == maps.get((2, 0)) == player:
            return True
        if maps.get((0, 1)) == maps.get((1, 1)) == maps.get((2, 1)) == player:
            return True
        if maps.get((0, 2)) == maps.get((1, 2)) == maps.get((2, 2)) == player:
            return True
        if maps.get((0, 0)) == maps.get((1, 1)) == maps.get((2, 2)) == player:
            return True
        if maps.get((0, 2)) == maps.get((1, 1)) == maps.get((2, 0)) == player:
            return True
        return False

    def tictactoe(self, moves: list[list[int]]) -> str:
        maps = {}
        for i in range(len(moves)):
            r, c = moves[i][0], moves[i][1]
            if i % 2 == 0:
                maps[(r, c)] = 'X'
            else:
                maps[(r, c)] = 'O'
        if self.checkValues('X', maps):
            return "A"
        elif self.checkValues('O', maps):
            return "B"
        elif len(moves) == 9:
            return 'Draw'
        else:
            return 'Pending'