const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const shirt = input[1].split(' ').map(Number);
const arr = input[2].split(' ').map(Number);

const T = arr[0];
const P = arr[1];

let sum = 0;

for (let i = 0; i < shirt.length; i++) {
  sum += Math.ceil(shirt[i] / T);
}

console.log(sum);

const answer = Math.floor(N / P);
console.log(answer + ' ' + (N - answer * P));
