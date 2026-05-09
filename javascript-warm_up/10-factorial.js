#!/usr/bin/node

const arg1 = process.argv[2];
const a = parseInt(arg1);

function fact (n) {
  if (isNaN(n)) {
    return 1;
  }
  let res = 1;
  for (let i = 1; i <= n; i++) {
    res *= i;
  }
  return res;
}
console.log(fact(a));
