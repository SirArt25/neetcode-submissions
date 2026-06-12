class Solution:
    def checkRow(self, number, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(0, 9):
            val = board[number][i]
            if val != ".":
                if val in seen: return False
                seen.add(val)
        return True

    def checkCollumn(self, number, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(0, 9):
            val = board[i][number]
            if val != ".":
                if val in seen: return False
                seen.add(val)
        return True

    def checkGrid(self, number, board: List[List[str]]) -> bool:
        seen = set()
        starting_i = (number // 3) * 3
        starting_j = (number % 3) * 3

        for i in range(starting_i, starting_i + 3):
            for j in range(starting_j, starting_j + 3):
                val = board[i][j]
                if val != ".":
                    if val in seen: return False
                    seen.add(val)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            if self.checkRow(i, board) == False:
                return False
            if self.checkCollumn(i, board) == False:
                return False
            if self.checkGrid(i, board) == False:
                return False
        return True