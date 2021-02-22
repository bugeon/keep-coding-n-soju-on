const number = 423;
const position = 7;

const setValue = (n, p, bit) => {
	return bit === 1 ? n | (1 << (p - 1)) : n & ~(1 << (p - 1));
};

console.log(`${number.toString(2)} - ${number}의 2진수 표기`);
console.log(`${setValue(number, position, 1).toString(2)}(${setValue(number, position, 1)}) - ${position}번째 위치를 1로 변경`);
console.log(`${setValue(number, position + 1, 0).toString(2)}(${setValue(number, position + 1, 0)}) - ${position + 1}번째 위치를 0으로 변경`);