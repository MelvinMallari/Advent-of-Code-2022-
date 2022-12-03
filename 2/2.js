const fs = require("fs");

const input = fs.readFileSync("./2.txt", "utf8");

const matches = input.split("\n");

const TRANSLATE = {
  X: "LOSE",
  Y: "DRAW",
  Z: "WIN",
};

const SCORES = {
  ROCK: 1,
  PAPER: 2,
  SCISSOR: 3,
  LOSE: 0,
  DRAW: 3,
  WIN: 6,
};

const CORRESPONDING_MOVE_SCORE = {
  A: { LOSE: SCORES.SCISSOR, DRAW: SCORES.ROCK, WIN: SCORES.PAPER },
  B: { LOSE: SCORES.ROCK, DRAW: SCORES.PAPER, WIN: SCORES.SCISSOR },
  C: { LOSE: SCORES.PAPER, DRAW: SCORES.SCISSOR, WIN: SCORES.ROCK },
};

const total = matches.reduce((acc, match) => {
  if (match.trim() === "") return acc;
  const [otherMove, rawOutcome] = match.split(" ");
  const outcome = TRANSLATE[rawOutcome];
  return acc + SCORES[outcome] + CORRESPONDING_MOVE_SCORE[otherMove][outcome];
}, 0);

console.log(total);
