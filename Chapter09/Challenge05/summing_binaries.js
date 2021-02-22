const p = 17;
const q = 20;

const bitsSum = (p, q) => {
	let and = p & q;
	let xor = p ^ q;

	while (and) {
		and = and << 1;
		
		const tmp = xor ^ and;
		and = xor & and;
		xor = tmp;
	}

	return `${xor.toString(2)}(${xor})`;
};

console.log(`\t${p.toString(2)}(${p})
+\t${q.toString(2)}(${q})
------------------
\t${bitsSum(p, q)}`);