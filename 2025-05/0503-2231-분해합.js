const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());

let result = 0;

for (let i = 1; i < N; i++) {
  const sum =
    i +
    i
      .toString()
      .split('')
      .map(Number)
      .reduce((a, b) => a + b, 0);

  if (sum === N) {
    result = i;
    break;
  }
}

console.log(result);
