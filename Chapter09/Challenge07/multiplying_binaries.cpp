#include <iostream>
using namespace std;

int multiplying_binaries(int p, int q) {
	int result = 0;

	while(q) {
		if (q & 1) {
			result += p;
		}
		p = p << 1;
		q = q >> 1;
	}
	
	return result;
}

void main() {
	int p, q;
	cin >> p >> q;
	cout << multiplying_binaries(p, q) <<endl;
}
