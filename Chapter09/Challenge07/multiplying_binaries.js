const p = 124;
const q = 29;

const is_zero = (n) => {
	return n === 0;
}

const bitsMultiply = (p, q) => {
	let result = 0;

	while (!is_zero(q)) {
		if (q & 1 !== 0)
			result += p;
		
		p = p << 1;
		q = q >> 1;
	}

	return result;
};

console.log(bitsMultiply(p, q));