#include <iostream>
using namespace std;

int longest_sequence(int n) {
	int result = -1;
	int c = 0;
	int before_num = -1;

	while (n) {
		if (n & 1) {
			c++;
			if (c > result) result = c;
		}
		else {
			if (n & 2 && before_num) {
				c++;
				if (c > result) result = c;
			}
			else {
				c = 0;
			}
		}

		before_num = n & 1;
		n = n >> 1;
	}

	return result;

}

void main() {
	int n;
	cin >> n;
	cout << longest_sequence(n) <<endl;
}
