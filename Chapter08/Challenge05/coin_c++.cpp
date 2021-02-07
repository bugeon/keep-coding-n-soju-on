#include <iostream>
using namespace std;

#define N 10000
#define MAX_POSITION 4

int coins[MAX_POSITION] = { 25, 10, 5, 1 };
int calculate_change_call = 0;
int calculate_change_visited_call = 0;

int cached[N + 1][MAX_POSITION];

int calculate_change(int amount, int position) {
	calculate_change_call++;
	if (position >= MAX_POSITION - 1) {
		return 1;
	}

	int coin = coins[position];
	int count = 0;
	for (int i = 0; i * coin <= amount; i++) {
		int remaining = amount - i * coin;
		count += calculate_change(remaining, position + 1);
	}

	return count;
}

int calculate_visited_change(int amount, int position) {
	calculate_change_visited_call++;

	if (cached[amount][position] > 0) return cached[amount][position];

	if (position >= MAX_POSITION - 1) {
		return 1;
	}

	int coin = coins[position];
	int count = 0;
	for (int i = 0; i * coin <= amount; i++) {
		int remaining = amount - i * coin;
		count += calculate_visited_change(remaining, position + 1);
	}

	cached[amount][position] = count;
	return count;
}

int main() {
	cout << "change count: " << calculate_change(N, 0) << endl;
	cout << "recursion call: " << calculate_change_call << endl;
	/*
	change count: 134235101
	recursion call: 134436304
	*/
	for (int i = 0; i < N + 1; i++) {
		for (int j = 0; j < MAX_POSITION; j++) {
			cached[i][j] = -1;
		}
	}

	cout << "change count: " << calculate_visited_change(N, 0) << endl;
	cout << "recursion call: " << calculate_change_visited_call << endl;
	/*
	change count: 134235101
	recursion call: 2200206
	*/
	return 0;
}
