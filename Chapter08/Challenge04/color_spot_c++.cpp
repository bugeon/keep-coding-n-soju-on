#include <iostream>
#include <random>
using namespace std;

#define COLS 5
#define ROWS 5

int a[ROWS][COLS];

int biggest_color_spot, biggest_color;
int current_color_spot, current_color;
int visited_func_call = 0;

void compute_biggest_color_visited(int rows, int cols) {
	visited_func_call++;
	a[rows][cols] = -a[rows][cols];
	current_color_spot++;

	if (rows - 1 > 0 && a[rows - 1][cols] == current_color) compute_biggest_color_visited(rows - 1, cols);
	if (rows + 1 < ROWS && a[rows + 1][cols] == current_color) compute_biggest_color_visited(rows + 1, cols);
	if (cols - 1 > 0 && a[rows][cols - 1] == current_color) compute_biggest_color_visited(rows, cols - 1);
	if (cols + 1 < COLS && a[rows][cols + 1] == current_color) compute_biggest_color_visited(rows, cols + 1);
}

int main_color() {
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<int> dis(1, 3); // a spot can have the colors 1, 2 or 3

	
	biggest_color = -1;
	biggest_color_spot = -1;

	// add random colors
	for (int i = 0; i < ROWS; i++) {
		for (int j = 0; j < COLS; j++) {
			a[i][j] = dis(gen);
		}
	}

	// show the surface on screen
	for (int i = 0; i < ROWS; i++) {
		for (int j = 0; j < COLS; j++) {
			cout << a[i][j] << "  ";
		}
		cout << endl;
	}

	for (int i = 0; i < ROWS; i++) {
		for (int j = 0; j < COLS; j++) {
			current_color_spot = 0;
			current_color = a[i][j];
			if (a[i][j] > 0)
				compute_biggest_color_visited(i, j);
			if (current_color_spot > biggest_color_spot) {
				biggest_color_spot = current_color_spot;
				biggest_color = -1 * a[i][j];
			}

		}
	}
	cout << "biggest spot color: " << biggest_color << ", biggest spot: " << biggest_color_spot << endl;
	cout << "recursion with visited function call: " << visited_func_call << endl;

	/*
	1  3  2  1  2
	1  1  3  1  3
	1  2  2  2  1
	1  3  3  2  3
	1  2  1  1  3
	biggest spot color: 1, biggest spot: 6
	recursion with visited function call: 25
	*/

	return 0;
}
