class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        seen_cols = []
        seen_boxes = []

        for i in range(9):
            seen_cols.append(defaultdict(int))
            seen_boxes.append(defaultdict(int))
        
        for i, r in enumerate(board):

            seen = defaultdict(int)
            box = i // 3 * 3

            for j, n in enumerate(r):

                if n == '.':
                    continue
                
                seen_cols[j][n] += 1
                seen_boxes[box + j // 3][n] += 1
                seen[n] += 1

            if sum(seen.values()) != len(seen.values()):
                return False

        for seen_col in seen_cols:
            if sum(seen_col.values()) != len(seen_col.values()):
                return False

        for seen_box in seen_boxes:
            if sum(seen_box.values()) != len(seen_box.values()):
                return False

        return True

        

        
            





        