const find_magic_i = (start, end) => {
	const mid = parseInt((start + end) / 2);
	console.log(start, mid, end);
	if (start > end)
		return -1;

	const	result = find_magic_i(0, Math.min(mid - 1, arr[mid]));

	if (result !== -1)
		return result;

	if (arr[mid] === mid)
		return mid;

	return find_magic_i(Math.max(mid + 1, arr[mid]), end);
}


// const arr = [1, 4, 4, 4, 5, 5, 6, 6, 6, 11, 12, 12, 12, 15, 17, 20, 21, 21];
// const arr = [0, 1, 2, 3, 4, 5, 6];
const arr = [1, 4, 4, 4, 4, 5, 6, 6, 6, 11, 12, 12, 12];

const answer = find_magic_i(0, arr.length - 1);
if (answer === -1)
	console.log(`Thers isn't any magic index!`);
else
	console.log(`첫 magic index는 arr[${answer}] : ${answer}`);
