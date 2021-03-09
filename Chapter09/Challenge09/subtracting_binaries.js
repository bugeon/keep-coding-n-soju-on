const p = 124;
const q = 29;

const bitsSum = (p, q) => {
	let and = p & q;
	let xor = p ^ q;

	while (and) {
		and = and << 1;
		
		const tmp = xor ^ and;
		and = xor & and;
		xor = tmp;
	}

	return xor;
};

const bitsSub = (p, q) => {
	// const result = p + ~q + 1;
	// return result;
	
	p = bitsSum(p, ~q);
	p = bitsSum(p, 1);
	return p;
};

console.log(bitsSub(p, q));