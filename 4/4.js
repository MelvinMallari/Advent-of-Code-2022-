const fs = require("fs");

const input = fs.readFileSync("./4.txt", "utf8");
const ranges = input.split("\n").filter((line) => line.trim() !== "");

const hasFullContainment = (range1, range2) => {
  const [l1, u1] = range1.split("-").map((item) => Number(item));
  const [l2, u2] = range2.split("-").map((item) => Number(item));
  return (l1 <= l2 && u1 >= u2) || (l2 <= l1 && u2 >= u1);
};

// pt1;
const total = ranges.reduce((acc, range) => {
  const [range1, range2] = range.split(",");
  return hasFullContainment(range1, range2) ? acc + 1 : acc;
}, 0);
console.log({ total });

// pt2
const overlaps = (range1, range2) => {
  const [l1, u1] = range1.split("-").map((item) => Number(item));
  const [l2, u2] = range2.split("-").map((item) => Number(item));
  return (
    (l2 <= l1 && l1 <= u2) ||
    (l2 <= u1 && u1 <= u2) ||
    hasFullContainment(range1, range2)
  );
};
const res = ranges.reduce((acc, range) => {
  const [range1, range2] = range.split(",");
  return overlaps(range1, range2) ? acc + 1 : acc;
}, 0);
console.log({ res });
