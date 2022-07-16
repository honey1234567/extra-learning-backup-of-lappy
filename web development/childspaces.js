let cp = require("child_process");
console.log("trying to open calculator");
cp.execSync("calc");
cp.execSync("start chrome https:\\www.pepcoding.com");
console.log("opened calculator");
//cp.execSync("calc"); open vscode
//cp.execSync("start chrome https:\\www.pepcoding.com");
//similarly you can open all these in cmd line by wriytting these like calc etc
//open other file output from this file
let output = cp.execSync("node abc.js");
console.log("abc fired" + output);

