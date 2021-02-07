#include <iostream>
using namespace std;

#define MAP_SIZE 8

/*
	There are 8 possible position based on {n, m}
	{n-1, m-2}, {n+1. m-2}, {n+2, m-1}, {n+2, m+1}, {n+1, m+2}, {n-1, m+2}, {n-2, m+1}, {n-2, m-1}
*/

int possible_row[8] = { 1,2,2,1,-1,-2,-2,-1 };
int possible_col[8] = { 2,1,-1,-2,-2,-1,1,2 };

int visited[MAP_SIZE][MAP_SIZE];

bool find_solution = false;

void knight_tour(int row, int col, int cell) {
	visited[row][col] = cell;
	if (find_solution) return;
	if (cell >= MAP_SIZE * MAP_SIZE) {
		// final position -> solve problem
		for (int i = 0; i < MAP_SIZE; i++) {
			for (int j = 0; j < MAP_SIZE; j++) {
				cout << visited[i][j] << " ";
			}
			cout << endl;
		}

		// after print solution, initialize visited to 0
		visited[row][col] = 0;
		find_solution = true;
		return;
	}

	// 8개의 가능한 좌표 모두 탐색
	for (int i = 0; i < 8; i++) {
		int new_r = row + possible_row[i];
		int new_c = col + possible_col[i];

		if ((new_r >= 0 && new_r < MAP_SIZE && new_c >= 0 && new_c < MAP_SIZE)
			&& visited[new_r][new_c] == 0) {
			knight_tour(new_r, new_c, cell + 1);
		}
	}

	visited[row][col] = 0;
}


int main() {
	for (int i = 0; i < MAP_SIZE; i++) {
		for (int j = 0; j < MAP_SIZE; j++) {
			visited[i][j] = 0;
		}
	}

	// (0, 0)부터 시작해 (MAP_SIZE, MAP_SIZE)까지 돌며 check
	// 하나의 답 말고 전체 답을 찾아야 하는 경우 col을 1~MAP_SIZE까지 반복하며 해답을 찾도록 변경
	knight_tour(0, 0, 1);

	/*

	*/
	return 0;
}
