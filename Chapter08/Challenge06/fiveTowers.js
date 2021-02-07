const GRID_SIZE = 5;
const PRE_ROWS = new Array(GRID_SIZE);
const PRE_COLS = new Array(GRID_SIZE);

const fiveTowers = (row, col) => {
	for (let i = 0; i < row; i++)
	{
		if (col == PRE_COLS[i])
			return;
		if (Math.abs(col - PRE_COLS[i]) == Math.abs(row - PRE_ROWS[i]))
			return;
	}

	PRE_ROWS[row] = row, PRE_COLS[row] = col;

	if (row == GRID_SIZE - 1)
	{
		console.log(PRE_COLS);
		return;
	}

	for (let i = 0; i < GRID_SIZE; i++) {
		fiveTowers(row + 1, i);
	}
}
	
for (let i = 0; i < GRID_SIZE; i++)
	fiveTowers(0, i);