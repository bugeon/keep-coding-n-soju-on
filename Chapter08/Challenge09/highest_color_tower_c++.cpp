#include <iostream>
using namespace std;

struct Box {
	int width;
	int height;
	int color;
};

Box boxes[7];

int visited_boxes[7];
int build_call = 0;

int build(int base) {
	build_call++;

	int height = 0;
	int highest = 0;
	for (int i = base + 1; i < 7; i++) {
		if (boxes[base].color != boxes[i].color && boxes[base].width > boxes[i].width && boxes[base].height > boxes[i].height) {
			height = build(i);
		}
		if (highest < height) highest = height;
	}
	highest += boxes[base].height;

	return highest;
}

int build_memoization(int base) {
	build_call++;

	if (visited_boxes[base] > 0) return visited_boxes[base];

	int height = 0;
	int highest = 0;
	for (int i = base + 1; i < 7; i++) {
		if (boxes[base].color != boxes[i].color && boxes[base].width > boxes[i].width && boxes[base].height > boxes[i].height) {
			height = build_memoization(i);
		}
		if (highest < height) highest = height;
	}
	highest += boxes[base].height;
	visited_boxes[base] = highest;

	return highest;
}

int main() {
	// boxes들이 sort되어 있다고 가정(width 기준)
	boxes[0] = { 14, 10, 3 };
	boxes[1] = { 10, 5, 2 };
	boxes[2] = { 10, 7, 1 };
	boxes[3] = { 10, 3, 1 };
	boxes[4] = { 7, 5, 1 };
	boxes[5] = { 5, 7, 1 };
	boxes[6] = { 2, 8, 1 };

	int highest = 0;
	int max_highest = 0;
	for (int i = 0; i < 7; i++) {
		highest = build(i);
		if (highest > max_highest) max_highest = highest;
	}
	cout << "The highest tower of colored boxes has a high of (plain recursion): " << max_highest << endl;
	cout << "build call: " << build_call << endl;

	build_call = 0;
	for (int i = 0; i < 7; i++) visited_boxes[i] = -1;
	highest = 0;
	max_highest = 0;
	for (int i = 0; i < 7; i++) {
		highest = build_memoization(i);
		if (highest > max_highest) max_highest = highest;
	}
	cout << "The highest tower of colored boxes has a high of (Memoization): " << max_highest << endl;
	cout << "build call: " << build_call << endl;

	/*

	*/
	return 0;
}
