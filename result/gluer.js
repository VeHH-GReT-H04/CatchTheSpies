const fs = require("fs");

let accumulator = 'firstName;lastName;middleName;from;to;date;time\n'

let templateData = fs.readFileSync("template.txt", "utf8");
let parsedOneData = fs.readFileSync("parsedOne.txt", "utf8");
let parsedTwoData = fs.readFileSync("parsedTwo.txt", "utf8");
let parsedThreeData = fs.readFileSync("parsedThree.txt", "utf8");

accumulator += templateData + parsedOneData + parsedTwoData + parsedThreeData;



fs.writeFileSync('result.txt', accumulator, "UTF-8");