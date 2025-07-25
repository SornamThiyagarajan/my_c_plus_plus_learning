class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Row 0
        for _ in range(1, rowIndex + 1):
            # Generate next row using previous row
            # Append 1 at the end and create new row by summing adjacent pairs
            row = [1] + [row[i] + row[i+1] for i in range(len(row) - 1)] + [1]
        return row