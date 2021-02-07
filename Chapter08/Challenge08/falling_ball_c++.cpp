#include <iostream>
#include <random>
using namespace std;

#define COLS 5
#define ROWS 5

int elevations[ROWS][COLS];
int falling_ball_call = 0;

void compute_path(int rows, int cols) {
	falling_ball_call++;

	int c_value = elevations[rows][cols];
	elevations[rows][cols] = 0;

	if (rows >= 0 && rows < ROWS &&  cols > 0 && cols < COLS) {
		if (rows - 1 >= 0 && elevations[rows - 1][cols] > 0 && elevations[rows - 1][cols] < c_value) compute_path(rows - 1, cols);
		if (rows + 1 >= 0 && elevations[rows + 1][cols] > 0 && elevations[rows + 1][cols] < c_value) compute_path(rows + 1, cols);
		if (cols - 1 >= 0 && elevations[rows][cols - 1] > 0 && elevations[rows][cols - 1] < c_value) compute_path(rows, cols - 1);
		if (cols + 1 >= 0 && elevations[rows][cols + 1] > 0 && elevations[rows][cols + 1] < c_value) compute_path(rows, cols + 1);
	}
}

int main() {

	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<int> dis(1, 5); // a spot can have the colors 1, 2 or 3

	// add random elevations
	for (int i = 0; i < ROWS; i++) {
		for (int j = 0; j < COLS; j++) {
			elevations[i][j] = dis(gen);
			cout << elevations[i][j] << " ";
		}
		cout << endl;
	}

	

	cout << "Middle cell has elevation: " << elevations[ROWS / 2][COLS / 2] << endl;
	compute_path(ROWS / 2, COLS / 2);

	cout << "Result grid:" << endl;
	for (int i = 0; i < ROWS; i++) {
		for (int j = 0; j < COLS; j++) {
			cout << elevations[i][j] << " ";
		}
		cout << endl;
	}

	cout << "recursion call: " << falling_ball_call << endl;
	/*
	2 1 2 1 3
	5 2 2 1 1
	1 1 4 1 5
	2 4 2 3 5
	3 5 4 5 1
	Middle cell has elevation: 4

	Result grid:
	2 1 2 1 3
	5 2 0 0 1
	1 0 0 0 5
	2 4 0 3 5
	3 5 4 5 1

	recursion call: 6
	*/
	return 0;
}
