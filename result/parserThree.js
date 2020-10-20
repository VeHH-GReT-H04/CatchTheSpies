const fs = require("fs");

let accumulator = 'firstName;lastName;middleName;from;to;date;time\n\n'

let fileData = fs.readFileSync("jsonToCsv.txt", "utf8");

let arrayOfStrings = fileData.split('\n');
arrayOfStrings.forEach((element, index) => {
    if (index !== 0 && index !== 1) {
        let arrayOfElements = element.split(';');
        if (arrayOfElements[2] !== 'null') {
            accumulator += arrayOfElements[2] + ';';
            accumulator += arrayOfElements[3] + ';';
            accumulator += '' + ';';
            accumulator += arrayOfElements[6] + ';';
            accumulator += arrayOfElements[9] + ';';
            accumulator += arrayOfElements[5] + ';';
            accumulator += '' + '\n';
        }
    }
});

fs.writeFileSync('parsedThree.txt', accumulator, "UTF-8");