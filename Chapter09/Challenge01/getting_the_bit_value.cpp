#include <iostream>
using namespace std;

char get_bit_value(int n, int k) {
	int result = n & (1 << k);

	if (result > 0) return '1';
	else return '0';
}

void main() {
	int input_number, position, result;
	cin >> input_number >> position;
	cout << get_bit_value(input_number, position) <<endl;
}
