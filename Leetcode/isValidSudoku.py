'''
Straight forward Solution going through all the possible cases that would make
a board not valid
https://oj.leetcode.com/problems/valid-sudoku/
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        
        # check every lines, every columns, every square for redundant numbers

        # check line by line
        for i in range(0,9):
            check = set()           
            for j in range(0,9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] not in check:
                    check.add(board[i][j])
                else:
                    return False
        
        # check column by column
        for i in range(0,9):
            check = set()           
            for j in range(0,9):
                if board[j][i] == '.':
                    pass
                elif board[j][i] not in check:
                    check.add(board[j][i])
                else:
                    return False

        # check square by square
        for k in [0,3,6]:
            for l in [0,3,6]:
            	check = set()
                for i in range(0+k,3+k):
                    for j in range(0+l,3+l):
                        if board[i][j] == '.':
                            pass
                        elif board[i][j] not in check:
                            check.add(board[i][j])
                        else:
                            return False

        return True

s = Solution()

test =  ["..4...63.",".........","5......9.","....6....","4.3.....1","...7.....","...5.....",".........","........."]
test_line = ["..55....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
test_col = ["..5.....6","..5.14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]


print s.isValidSudoku(test) == True
print s.isValidSudoku(test_line) == False
print s.isValidSudoku(test_col) == False

test2 = ["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"]

