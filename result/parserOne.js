const fs = require("fs");

let accumulator = 'firstName;lastName;middleName;from;to;date;time\n\n'

let fileData = fs.readFileSync("first_part.txt", "utf8");

let arrayOfStrings = fileData.split('\n');
arrayOfStrings.forEach((element, index) => {
    if (index !== 0) {
        let arrOfElements = element.split(',');
        if (arrOfElements[1] !== undefined) {
            let arrayOfNames = arrOfElements[1].split(' ');

            if (arrayOfNames.length === 2) {
                accumulator += arrayOfNames[0] + ';';
                accumulator += arrayOfNames[1] + ';';
                accumulator += '' + ';';
            } else if (arrayOfNames.length === 3) {
                if (arrayOfNames[1].length !== 1) {
                    accumulator += arrayOfNames[0] + ';';
                    accumulator += arrayOfNames[1] + ';';
                    accumulator += arrayOfNames[2] + ';';
                }
                else if (arrayOfNames[1].length === 1) {
                    accumulator += arrayOfNames[0] + ';';
                    accumulator += arrayOfNames[2] + ';';
                    accumulator += arrayOfNames[1] + ';';
                }
            }
            accumulator += arrOfElements[9] + ';';
            accumulator += arrOfElements[10] + ';';
            accumulator += arrOfElements[13] + ';';
            accumulator += arrOfElements[14] + '\n';
        }
    }
});

fs.writeFileSync('parsedOne.txt', accumulator, "UTF-8");
