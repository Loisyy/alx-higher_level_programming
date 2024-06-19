#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).map(Number).filter(n => !isNaN(n));

  if (arr.length < 2) {
    console.log('0');
  } else {
    const second = arr.sort((a, b) => b - a)[1];
    console.log(second);
  }
}

