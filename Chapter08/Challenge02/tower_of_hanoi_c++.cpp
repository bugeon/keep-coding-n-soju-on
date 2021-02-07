#include <iostream>
using namespace std;

void move_disk(int n, int orig, int target, int inter) {
	if (n < 0) return;
	if (n == 1) {
		cout << "move disk 1 from " << orig << " to " << target << endl;
		return;
	}
	
	move_disk(n - 1, orig, inter, target);
	cout << "move disk " << n << " from " << orig << " to " << target << endl;
	move_disk(n - 1, inter, target, orig);
}

int main() {

	int n = 5;
	move_disk(n, 1, 3, 2);

	return 0;
}
