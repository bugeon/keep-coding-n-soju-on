function queue_josephus(n, k) {
	const circle = [];

	for (let i = 1; i <= n; i++) {
		circle.push(i);
	}
	
	while (circle.length !== 1) {
		for (let i = 1; i <= k; i++) {
			const eliminated = circle.shift()

			if (i === k) {
				// console.log(`${eliminated}`);
				break;
			}

			circle.push(eliminated);
		}
	}

	console.log(`최종 생존자: ${circle.pop()}`);
}

const n = 15;
const k = 3; 

queue_josephus(n, k);