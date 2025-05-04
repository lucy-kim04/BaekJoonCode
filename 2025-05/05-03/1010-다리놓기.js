const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = parseInt(input[0]);

function factorial(n) {
  let res = 1;
  for (let i = 2; i <= n; i++) res *= i;
  return res;
}

function comb(n, r) {
  return factorial(n) / (factorial(r) * factorial(n - r));
}

for (let i = 1; i <= T; i++) {
  const [N, M] = input[i].split(' ').map(Number);
  console.log(Math.round(comb(M, N)));
}
