const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);
const output = [];

for (let i = 1; i <= T; i++) {
  const [A, B] = input[i].split(' ').map(Number);
  output.push(A + B);
}

console.log(output.join('\n'));
