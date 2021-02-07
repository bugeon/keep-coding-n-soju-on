#include <iostream>
using namespace std;

#define ARRAY_LENGTH 18
int arr[ARRAY_LENGTH] = {1, 4, 4, 4, 5, 5, 6, 6, 6, 11, 12, 12, 12, 15, 17, 20, 21, 21};
int magic_index_call = 0;

int find(int start, int end) {
	magic_index_call++;
	if (start > end) return -1;

	int middle = (start + end) / 2;
	int c_value = arr[middle];

	if (middle == c_value) return middle;

	int left_index;
	if (middle < c_value)
		left_index = find(0, middle - 1);
	else
		left_index = find(0, c_value);
	if (left_index > 0) return left_index;

	int right_index;
	if (middle < c_value)
		right_index = find(c_value, end);
	else
		right_index = find(middle + 1, end);

	//return -1;
}

int main() {
	
	int result_index = find(0, ARRAY_LENGTH - 1);
	cout << "index " << result_index << " has value " << arr[result_index] << endl;
	cout << "recursion call: " << magic_index_call << endl;

	/*
	
	*/
	return 0;
}
