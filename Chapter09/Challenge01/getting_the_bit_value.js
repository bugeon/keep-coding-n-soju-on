const number = 423;
const position = 7;

// p번째의 수를 확인할 경우 p - 1 만큼 이동해야하는거 아닌가? 책은 p만큼 이동
const getValue = (n, p) => {
	const value = n & (1 << (p - 1));

	return value > 0 ? 1 : 0;
};

console.log(`${number}의 2진수 표기: ${number.toString(2)}`);
console.log(`${position}번째 수: ${getValue(number, position)}`);
