class Box {
	constructor(width, height, colour) {
		this.width = width;
		this.height = height;
		this.colour = colour;
	}

	can_be_next(Box) {
		return (Box.width > this.width) && (Box.height > this.height) && (Box.colour !== this.colour);
	}
}

const get_highest_tower = (index) => {
	let highest = 0;
	const current = boxes[index];

	if (index < boxes.length && cache[index])
		return cache[index];

	for (let i = index + 1; i < boxes.length; i++) {
		if (boxes[i].can_be_next(current)) {
			const height = get_highest_tower(i, cache);
			highest = Math.max(height, highest);
		}
	}

	highest += current.height;
	cache[index] = highest;

	return highest;
}

const boxes = [];
boxes.push(new Box(10, 5, 2));
boxes.push(new Box(10, 7, 1));
boxes.push(new Box(10, 3, 1));
boxes.push(new Box(14, 10, 3));
boxes.push(new Box(5, 7, 1));
boxes.push(new Box(7, 5, 1));
boxes.push(new Box(2, 8, 1));

boxes.sort((a, b) => {
	return b.width - a.width || b.height - a.height;
});

const cache = new Array(boxes.length);
const result = get_highest_tower(0);

console.log(boxes);
console.log(result);
console.log(cache);
