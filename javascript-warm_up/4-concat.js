#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (arg1 === undefined || arg2 === undefined) {
    
  const failed = String(arg1).concat(' is ', String(arg2));
  console.log(failed);
} else {
  const result = arg1.concat(' is ', arg2);
  console.log(result);
}
