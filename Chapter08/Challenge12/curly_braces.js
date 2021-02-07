const N = 4;
const ANSWER = new Array(N + 1);

for (let i = 0; i <= N; i++) {
	ANSWER[i] = [];
}

const curlyBraces = (n) => {
	if (n <= 1)
		return;
	
	const braces = [...ANSWER[n - 1]];
	for (const brace of braces) {
		for (let i = 0; i < brace.length; i++) {
			new_brace = `${brace.slice(0, i)}{}${brace.slice(i)}`;
			
			if (ANSWER[n].indexOf(new_brace) === -1) {
				ANSWER[n].push(new_brace);
			}
		}
	}
}

ANSWER[0].push('');
ANSWER[1].push('{}');
for (let i = 2; i <= N; i++) {
	curlyBraces(i);
}

console.log(ANSWER[N]);