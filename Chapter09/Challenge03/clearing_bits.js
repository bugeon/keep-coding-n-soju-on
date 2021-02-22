const number = 423;
const k = 7;

const clearBitsFromMSB = (n, k) => {
	return n & ((1 << k) - 1);
};

const clearBitsFromPosition = (n, k) => {
	return n & ~((1 << k) - 1);
};

console.log(number.toString(2), number);
console.log(clearBitsFromMSB(number, k).toString(2), clearBitsFromMSB(number, k));
console.log(clearBitsFromPosition(number, k).toString(2), clearBitsFromPosition(number, k));