let jsonStr = require('C:\\Users\\mmrfo\\Desktop\\FrequentFlyerForum-Profiles.json');
fs=require("fs")

let accumulator = 'NickName;Sex;FirstName;LastName;TravelDocuments;DateOfFlight;Departure;Arrival\n\n';

jsonStr['Forum Profiles'].forEach((elOfProfile) => {
    elOfProfile['Registered Flights'].forEach(elOfFlight => {
        accumulator += elOfProfile['NickName'] + ';';
        accumulator += elOfProfile['Sex'] + ';';
        accumulator += elOfProfile['Real Name']['First Name'] + ';';
        accumulator += elOfProfile['Real Name']['Last Name'] + ';';
        accumulator += elOfProfile['Travel Documents'][0]['Passports'] + ';';
        accumulator += elOfFlight['Date'] + ';';
        accumulator += elOfFlight['Departure']['City'] + ' ' + elOfFlight['Departure']['Country'] + ' ' + elOfFlight['Departure']['Airport'] + ';';
        accumulator += elOfFlight['Arrival']['City'] + ' ' + elOfFlight['Arrival']['Country'] + ' ' + elOfFlight['Arrival']['Airport'] + '\n';
    });
});

fs.writeFileSync('jsonToCsv.txt', accumulator, "UTF-8");
