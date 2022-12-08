const fs = require("fs");
const input = fs.readFileSync("./7.txt", "utf8").trim();
const lines = input.split("\n");

class TreeNode {
  constructor(path, size = 0) {
    this.path = path;
    this.size = size;
    this.directories = {};
    this.files = {};
  }
}

const buildTree = () => {
  let history = [];
  const root = new TreeNode("/");
  history = [root];

  lines.forEach((line) => {
    const arguments = line.split(" ");
    const currNode = history[history.length - 1];

    if (arguments[0] === "$") {
      if (arguments[1] === "cd") {
        const arg = arguments[2];
        if (arg === "/") {
          history = [root];
        } else if (arg === "..") {
          history.pop();
        } else {
          history.push(currNode.directories[arg]);
        }
      }
    } else if (arguments[0] === "dir") {
      const dir = arguments[1];
      currNode.directories[dir] = new TreeNode(dir);
    } else {
      const [fileSize, fileName] = [arguments[0], arguments[1]];
      currNode.files[fileName] = new TreeNode(fileName, Number(fileSize));
    }
  });

  // fill in directory sizes
  const dfs = (node) => {
    if (!node) return 0;
    node.size += Object.values(node.files).reduce(
      (acc, file) => acc + file.size,
      0
    );
    Object.values(node.directories).forEach((dir) => {
      node.size += dfs(dir);
    });
    return node.size;
  };
  dfs(root);

  return root;
};

const tree = buildTree();
const pt1 = () => {
  let total = 0;
  const sum = (node) => {
    if (!node) return;
    Object.values(node.directories).forEach((dir) => {
      if (dir.size <= 100000) total += dir.size;
      sum(dir);
    });
  };
  sum(tree);
  return total;
};
console.log("pt1", pt1());

const pt2 = () => {
  let min = Infinity;
  const SPACE_NEEDED = 8381165;
  const bfs = (node) => {
    if (!node) return;
    let level = Object.values(node.directories);
    while (level.length > 0) {
      let nextLevel = [];
      level.forEach((dir) => {
        if (dir.size < SPACE_NEEDED) return;
        min = dir.size < min ? dir.size : min;
        nextLevel = nextLevel.concat(Object.values(dir.directories));
      });
      level = nextLevel;
    }
  };
  bfs(tree);
  return min;
};
console.log("pt2", pt2());
