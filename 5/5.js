const fs = require("fs");

const [crates, moveList] = fs.readFileSync("./5.txt", "utf8").split("\n\n");

const rows = crates.split("\n").slice(0, -1).reverse();

// 1: 3, 2: 7, 3: 11, 4: 15 ...
const numStacks = (rows[0].length - 3) / 4 + 1;

const stacks = {};
for (let i = 1; i < numStacks + 1; i += 1) {
  stacks[i] = [];
}

// 1: 2, 2: 6, 3: 10, 4: 14 ...
const getStackFromColumnNum = (columnNumber) => {
  return (columnNumber - 2) / 4 + 1;
};

rows.forEach((row) => {
  [...row].forEach((char, index) => {
    if (char.match(/[A-Z]/i)) {
      const col = index + 1;
      const stack = getStackFromColumnNum(col);
      stacks[stack].push(char);
    }
  });
});

const parseMove = (move) => {
  const split = move.split(" ");
  return [split[1], split[3], split[5]].map((el) => Number(el));
};

const moves = moveList.split("\n").filter((line) => line.trim() !== "");
// pt1
// moves.forEach((move) => {
//   const [numCrates, from, to] = parseMove(move);
//   for (let i = 0; i < numCrates; i += 1) {
//     stacks[to].push(stacks[from].pop());
//   }
// });

// pt2
moves.forEach((move) => {
  const [numCrates, from, to] = parseMove(move);
  const spliced = stacks[from].splice(stacks[from].length - numCrates);
  stacks[to] = stacks[to].concat(spliced);
});

const res = Object.values(stacks).reduce(
  (acc, stack) => acc + stack[stack.length - 1],
  ""
);
console.log({ res });
