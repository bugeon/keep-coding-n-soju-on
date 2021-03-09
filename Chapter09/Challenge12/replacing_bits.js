const bitsReplace = (p, q, i, j) => {

	const leftSidefromJ = (~0) << (j + 1);
	const rightSidefromI = (1 << i) - 1;

	const sides_of_p = (leftSidefromJ | rightSidefromI) & p;
	const q_from_j_to_i = ((1 << j) - 1) & (q << i)
	
	return sides_of_p | q_from_j_to_i;
};

// 책과 다르게 p의 부분을 q로 바꿈
const p = 4914;
const q = 63;
const i = 4;
const j = 9;

console.log(bitsReplace(p, q, i, j).toString(2));