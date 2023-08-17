class Solution {
    static isValidSudoku(board) {
        const cols = new Map();
        const rows = new Map();
        const squares = new Map(); // key is `${r//3},${c//3}`

        for (let r = 0; r < 9; r++) {
            for (let c = 0; c < 9; c++) {
                const cell = board[r][c];
                if (cell === '.') {
                    continue;
                }
                const rowKey = `r${r}`;
                const colKey = `c${c}`;
                const squareKey = `${Math.floor(r / 3)},${Math.floor(c / 3)}`;
                
                if (rows.has(rowKey) && rows.get(rowKey).has(cell) ||
                    cols.has(colKey) && cols.get(colKey).has(cell) ||
                    squares.has(squareKey) && squares.get(squareKey).has(cell)) {
                    return false;
                }
                
                if (!rows.has(rowKey)) rows.set(rowKey, new Set());
                if (!cols.has(colKey)) cols.set(colKey, new Set());
                if (!squares.has(squareKey)) squares.set(squareKey, new Set());
                
                rows.get(rowKey).add(cell);
                cols.get(colKey).add(cell);
                squares.get(squareKey).add(cell);
            }
        }
        
        return true;
    }
}

const board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
];

console.log(Solution.isValidSudoku(board));
