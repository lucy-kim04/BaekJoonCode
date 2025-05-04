const fs = require('fs');
const [m, n] = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split(' ')
  .map(Number);

const isPrime = new Array(n + 1).fill(true);
isPrime[0] = isPrime[1] = false;

for (let i = 2; i <= Math.sqrt(n); i++) {
  if (isPrime[i]) {
    for (let j = i * i; j <= n; j += i) {
      isPrime[j] = false;
    }
  }
}

let result = '';
for (let i = m; i <= n; i++) {
  if (isPrime[i]) result += i + '\n';
}
console.log(result);
