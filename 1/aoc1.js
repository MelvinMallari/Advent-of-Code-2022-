const fs = require("fs");

const input = fs.readFileSync("./aoc1.txt", "utf8");

const elfBaggies = input.split(`\n\n`);

// smallest to largest
const largest = [-Infinity, -Infinity, -Infinity];
elfBaggies.forEach((baggie) => {
  const baggieCalories = baggie.split(`\n`).map((group) => Number(group));
  const totalCalories = baggieCalories.reduce((prev, curr) => prev + curr, 0);

  if (totalCalories > largest[2]) {
    largest[0] = largest[1];
    largest[1] = largest[2];
    largest[2] = totalCalories;
  } else if (totalCalories > largest[1]) {
    largest[0] = largest[1];
    largest[1] = totalCalories;
  } else if (totalCalories > largest[0]) {
    largest[0] = totalCalories;
  }
});

console.log(largest[0] + largest[1] + largest[2]);
