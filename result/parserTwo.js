const fs = require("fs");

let accumulator = 'firstName;lastName;middleName;from;to;date;time\n\n'

let fileData = fs.readFileSync("second_part.txt", "utf8");

let arrayOfStrings = fileData.split('\n');
arrayOfStrings.forEach((element, index) => {
    if (index !== 0) {
        let arrOfElements = element.split(',');
        if (arrOfElements[1] !== undefined) {
            let arrayOfNames = arrOfElements[2].split(' ');
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
            accumulator += arrOfElements[6] + ';';
            accumulator += arrOfElements[7] + ';';
            accumulator += arrOfElements[11] + ';';
            accumulator += arrOfElements[12] + '\n';
        }
    }
});

fs.writeFileSync('parsedTwo.txt', accumulator, "UTF-8");
