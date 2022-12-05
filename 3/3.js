const fs = require("fs");

const input = fs.readFileSync("./3.txt", "utf8");
const rucksack = input.split("\n").filter((line) => line.trim() !== "");

const LOWER_CASE_REF = "a";
const UPPER_CASE_REF = "A";
const calculatePriority = (ch) => {
  if (ch === ch.toUpperCase()) {
    return ch.charCodeAt(0) - UPPER_CASE_REF.charCodeAt(0) + 27;
  }
  return ch.charCodeAt(0) - LOWER_CASE_REF.charCodeAt(0) + 1;
};

const findCommon = (group) => {
  const sets = group.slice(1).map((ruck) => new Set(ruck));
  for (let ch of group[0]) {
    if (sets.every((set) => set.has(ch))) {
      return ch;
    }
  }
};

// pt1
const total = rucksack.reduce((acc, ruck) => {
  const half = ruck.length / 2;
  const compartments = [ruck.slice(0, half), ruck.slice(half)];
  const common = findCommon(compartments);
  return acc + calculatePriority(common);
}, 0);
console.log({ total });

// pt2
let res = 0;
const groupSize = 3;
for (let i = 0; i < rucksack.length; i += groupSize) {
  const group = rucksack.slice(i, i + groupSize);
  const common = findCommon(group);
  res += calculatePriority(common);
}
console.log({ res });
