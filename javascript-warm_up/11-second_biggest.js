#!/usr/bin/node

const arg1 = process.argv.slice(2).map(Number);

// function getSecondLargest that takes an array a.
function getSecondLargest (a) {
  const n = a.length;

  // Sort the array in non-decreasing order
  a.sort((a, b) => a - b);
  // Start from second last element as last is the largest
  for (let i = n - 2; i >= 0; i--) {
    // return the first element which is not equal to the
    // largest element
    if (a[i] !== a[n - 1]) {
      return a[i];
    }
  }
  return 0;
}
console.log(getSecondLargest(arg1));
