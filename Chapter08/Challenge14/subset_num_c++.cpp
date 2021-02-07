#include <iostream>
using namespace std;

#define ARRAY_SIZE 7

int subset_answer[ARRAY_SIZE];
int arr_subset[ARRAY_SIZE] = { 5, 1, 6, 10, 7, 11, 2 };

void find_subset_sum_recursive(int i, int current_sum, int given_sum) {
	if (current_sum == given_sum) {
		for (int i = 0; i < ARRAY_SIZE; i++) {
			if (subset_answer[i] == 1) {
				cout << arr_subset[i] << " ";
			}
		}
		cout << endl;
	}
	else if (i != ARRAY_SIZE) {
		subset_answer[i] = 1;
		current_sum += arr_subset[i];

		find_subset_sum_recursive(i + 1, current_sum, given_sum);

		current_sum -= arr_subset[i];
		subset_answer[i] = 0;

		find_subset_sum_recursive(i + 1, current_sum, given_sum);
	}
}

// TO DD: 
void find_subset_sum_DP(int given_sum) {
}

int main() {
	cout << "find sum using recursive: " << endl;
	find_subset_sum_recursive(0, 0, 9);

	cout << "find sum using DP: " << endl;
	find_subset_sum_DP(9);

	/*

	*/
	return 0;
}
