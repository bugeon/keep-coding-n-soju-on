#include <iostream>
using namespace std;

#define GRID_SIZE 5
#define MAX_SOLUTION 100

int solutions[MAX_SOLUTION][GRID_SIZE];
int solution_count = 0;
int five_tower_call = 0;

bool can_build(int columns[], int next_row, int next_col) {
	five_tower_call++;

	for (int current_row = 0; current_row < next_row; current_row++) {
		int current_col = columns[current_row];

		// cannot build on the same column
		if (current_col == next_col) {
			return false;
		}

		int columns_distance = current_col - next_col;
		if (columns_distance < 0) columns_distance =- columns_distance;
		int rows_distance = next_row - current_row;

		// cannot build on the same diagonal
		if (columns_distance == rows_distance) {
			return false;
		}
	}

	return true;
}

void build_towers(int row, int columns[]) {
	if (row == GRID_SIZE) {
		for (int i = 0; i < GRID_SIZE; i++) {
			solutions[solution_count][i] = columns[i];
		}
		solution_count++;
		return;
	}

	for (int col = 0; col < GRID_SIZE; col++) {
		if (can_build(columns, row, col)) {
			// build this tower
			columns[row] = col;

			// go to the next row
			build_towers(row + 1, columns);
		}
	}
}

int main() {
	int col[GRID_SIZE];
	for (int i = 0; i < GRID_SIZE; i++) col[i] = 0;

	build_towers(0, col);

	for (int i = 0; i < solution_count; i++) {
		cout << "solutions: ";
		for (int j = 0; j < GRID_SIZE; j++) {
			cout << solutions[i][j] <<" ";
		}
		cout << endl;
	}
	cout << "recursion call: " << five_tower_call << endl;

	/*
	solutions: 0 2 4 1 3
	solutions: 0 3 1 4 2
	solutions: 1 3 0 2 4
	solutions: 1 4 2 0 3
	solutions: 2 0 3 1 4
	solutions: 2 4 1 3 0
	solutions: 3 0 2 4 1
	solutions: 3 1 4 2 0
	solutions: 4 1 3 0 2
	solutions: 4 2 0 3 1
	recursion call: 220
	*/
	return 0;
}
