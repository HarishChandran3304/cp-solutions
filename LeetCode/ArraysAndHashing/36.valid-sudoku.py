from typing import List


# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            hashset = {str(i): set() for i in range(10)}

            for i in range(9):
                for j in range(9):
                    if board[i][j].isdigit():
                        if board[i].count(board[i][j]) > 1:
                            return False
                        
                        if [board[x][j] for x in range(9)].count(board[i][j]) > 1:
                            return False

                        if (i//3,j//3) in hashset[board[i][j]]:
                            return False
                        
                        hashset[board[i][j]].add((i//3,j//3))
            
            return True