function queue_josephus(n, k) {
	const circle = [];

	for (let i = 1; i <= n; i++) {
		circle.push(i);
	}
	
	let nth = 0;
	while (circle.length !== 1) {
		const eliminated = circle.shift()
		++nth;

		if (nth == k) {
			nth = 0;
			continue;
		}
		
		circle.push(eliminated);

		// for (let i = 1; i <= k; i++) {
		// 	const eliminated = circle.shift()
			

		// 	if (i === k) {
		// 		// console.log(`${eliminated}`);
		// 		break;
		// 	}

		// 	circle.push(eliminated);
		// }
	}

	console.log(`최종 생존자: ${circle.pop()}번`);
}

const n = 15;
const k = 3; 

queue_josephus(n, k);