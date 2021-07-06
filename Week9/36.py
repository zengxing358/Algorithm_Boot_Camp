class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dicn={i:[] for i in range(9)}
        dicm={i:[] for i in range(9)}
        dici={i:[] for i in range(9)}
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] not in dicn[i]:
                        dicn[i].append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in dicm[j]:
                        dicm[j].append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in dici[i//3*3+j//3]:
                        dici[i//3*3+j//3].append(board[i][j])
                    else:
                        return False
        return True