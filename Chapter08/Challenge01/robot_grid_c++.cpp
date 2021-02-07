#include <iostream>
using namespace std;

#define MAX_PATH 36

struct Point {
	int m;
	int n;
};

Point path[MAX_PATH];
bool visit_failed[6][6];
bool maze[6][6];
int current_path, recursion_call;

bool compute_path(int m, int n) {
	recursion_call++;

	if (m > 5 || n > 5) return false;
	if (maze[m][n]) return false;
	if (((m == 5) && (n == 5)) || compute_path(m + 1, n) || compute_path(m, n + 1)) {
		Point *new_p = &path[current_path++];
		new_p->m = m;
		new_p->n = n;

		return true;
	}

	return false;
}

bool compute_path_memoization(int m, int n) {
	recursion_call++;

	if (m > 5 || n > 5) return false;
	if (maze[m][n]) return false;
	if (visit_failed[m][n]) return false;

	if ((m == 5 && n == 5)
		|| compute_path_memoization(m + 1, n)
		|| compute_path_memoization(m, n + 1))
	{
		Point *new_p = &path[current_path++];
		new_p->m = m;
		new_p->n = n;

		return true;
	}

	visit_failed[m][n] = true;
	return false;
}

int main() {

	/*
	0 - robot, # - maze, X - target
	(0, 0) +           +
			|0| | | | | |
			| |#| | | | |
			|#| | | |#| |
			|#|#|#|#| | |
			| | | | | | |
			| | | | | |X|
			+           + (m, n)

	-> exchange start point to end point
	*/

	maze[1][1] = true;
	maze[2][0] = true;
	maze[2][4] = true;
	maze[3][0] = true;
	maze[3][1] = true;
	maze[3][2] = true;
	maze[3][3] = true;

	current_path = recursion_call = 0;
	compute_path(0, 0);

	for (int i = current_path - 1; i >= 0; i--) {
		cout << "#" << 10 - i << ", m :" << path[i].m << ", n: " << path[i].n << endl;
	}
	cout << "total recursion function call: " << recursion_call << endl;
	/*
	#0, m :0, n: 0
	#1, m :0, n: 1
	#2, m :0, n: 2
	#3, m :1, n: 2
	#4, m :1, n: 3
	#5, m :1, n: 4
	#6, m :1, n: 5
	#7, m :2, n: 5
	#8, m :3, n: 5
	#9, m :4, n: 5
	#10, m :5, n: 5
	total recursion function call: 24
	*/

	current_path = recursion_call = 0;
	compute_path_memoization(0, 0);

	for (int i = current_path - 1; i >= 0; i--) {
		cout << "#" << 10 - i << ", m :" << path[i].m << ", n: " << path[i].n << endl;
	}
	cout << "total recursion function call: " << recursion_call << endl;
	/*
	#0, m :0, n: 0
	#1, m :0, n: 1
	#2, m :0, n: 2
	#3, m :1, n: 2
	#4, m :1, n: 3
	#5, m :1, n: 4
	#6, m :1, n: 5
	#7, m :2, n: 5
	#8, m :3, n: 5
	#9, m :4, n: 5
	#10, m :5, n: 5
	total recursion function call: 22
	*/

	return 0;
}
