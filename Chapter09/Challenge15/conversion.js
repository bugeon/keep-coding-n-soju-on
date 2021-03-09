const conversion = (p, q) => {
	let count = 0;

	const xor = p ^ q;

	for (bit of xor.toString(2)) {
		if (bit === '1')
			count++;
	}

	// console.log(p.toString(2));
	// console.log(q.toString(2));
	// console.log(`–––––––––––––––––––`)
	// console.log(xor.toString(2));

	return count;
};

const p = 290932;
const q = 352345;

console.log(conversion(p, q));