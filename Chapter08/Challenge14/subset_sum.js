const arr = [3, 2, 7, 4, 5, 1, 6, 7, 9];
const s = 7;
// const arr = [5, 1, 6, 10, 7, 11, 2];
// const s = 9;

const dp = new Array(arr.length).fill(0);

for (let i = 0; i < dp.length; i++) {
	dp[i] = new Array(s + 1).fill(0);
}

for (let i = 0; i < arr.length; i++) {
	for (let j = 0; j < s + 1; j++) {
		if (arr[i] === j ) {
			dp[i][j] = arr[i];
			continue;
		}
		else if (i === 0) continue;

		if(arr[i] > j) dp[i][j] = dp[i - 1][j];
		else if(dp[i - 1][j]) dp[i][j] = dp[i - 1][j];
		else {
			const temp = dp[i - 1][j - arr[i]] > 0 ? arr[i] : 0;
			dp[i][j] = dp[i - 1][j - arr[i]] + temp;
		}
	}
}

for (let i = 0; i < dp.length; i++) {
	for (let j = 0; j < dp[i].length; j++) {
		process.stdout.write(`${dp[i][j]} `);
	}
	console.log();
}

console.log();

const print_subset_sum = (s) => {
	for (let i = 0; i < arr.length; i++) {
		if (dp[i][s] === s && arr[i] <= s) {
			let target = s;
			process.stdout.write(`subset : ${arr[i]}`);
			target -= arr[i];

			let idx = i;
			while (target > 0) {
				let subset_num = target;

				for (let j = idx; j >= 0 ; j--) {
					if (j === 0 && dp[j][target])
						break;
					else if (dp[j][target] === 0) {
						subset_num = arr[j + 1];
						break;
					}
				}

				process.stdout.write(`, ${subset_num}`);
				target -= subset_num;
			}

			console.log();
		}
	}
};

print_subset_sum(s);