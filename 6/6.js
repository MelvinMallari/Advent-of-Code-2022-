const fs = require("fs");
const input = fs.readFileSync("./6.txt", "utf8").trim();

const chars = [...input];
const PACKET_LENGTH = 4;
const MESSAGE_LENGTH = 14;
const findMarker = (windowLength) => {
  for (let i = 0; i < chars.length - windowLength; i += 1) {
    const window = chars.slice(i, i + windowLength);
    const set = new Set(window);
    if (set.size === windowLength) return i + windowLength;
  }
};

console.log("pt1", findMarker(PACKET_LENGTH));
console.log("pt2", findMarker(MESSAGE_LENGTH));
