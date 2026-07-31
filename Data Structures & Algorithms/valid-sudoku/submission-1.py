class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value=board[i][j]
                if value!=".":
                    if  value in rows[i]:
                        return False
                    else:
                        rows[i].add(value)
                    if value in cols[j]:
                        return False
                    else:
                        cols[j].add(value)
                    box_in=(i // 3) * 3 + (j // 3)
                    if value in box[box_in]:
                        return False
                    else:
                        box[box_in].add(value)

        return True


