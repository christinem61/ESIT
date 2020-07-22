const resemble = require('resemblejs/resemble');
const fs = require('fs');

var avg = 0.0;
var occupancy = 0;
var origin = resemble(fs.readFileSync('/home/pi/Desktop/pictures/origin.jpg'));
var pic0 = fs.readFileSync('/home/pi/Desktop/pictures/0.jpg');
var pic1 = fs.readFileSync('/home/pi/Desktop/pictures/1.jpg');
var pic2 = fs.readFileSync('/home/pi/Desktop/pictures/2.jpg');
var pictures = [pic0, pic1, pic2];
var bounds = [{left: 60, top: 250, right: 500, bottom: 720}, {left: 650, top: 250, right: 1030, bottom: 720}, {left: 350, top: 0, right: 560, bottom: 250}, {left: 630, top: 0, right: 830, bottom: 250}];
var areas = [5.03, 4.95, 17.55, 18.43]; // to convert percentages to comparable numbers

for (var i = 0; i < 4; i++){
	
	// changing settings for each bounding box
	resemble.outputSettings({
	  boundingBox: bounds[i],
	  useCrossOrigin: false,
	  outputDiff: true
	});
	
	
	for (var j = 0; j < 3; j++) {
		var mismatch = 0;
		
		// can't use data within this for whatever reason so defined as mismatch
		var diff = origin.compareTo(pictures[j]).onComplete(function(data){
			mismatch = data.misMatchPercentage;
		});
		
		//console.log(mismatch); //testing purposes
		avg += parseFloat(mismatch);
	}
		
	// converting average of 3 pictures' percentages to comparable percentages	
	avg = avg/3 * areas[i]; 
	
	//idk if they actually need different percentages but separate for now
	
	if (avg - 8 > 0){
		avg -= 3;
		if (areas[i] > 10){
			occupancy += avg/22;
		} else {
			occupancy += avg/40;
		}
	}
	avg = 0;
}

// if it's over 100 
if (occupancy > 10) {
	occupancy = 10;
}
console.log(occupancy*10);

/* var image = data.getImageDataUrl.toString();
    image = image.replace("image/png", "image/octet-stream");
    fs.writeFileSync('./mismatch.png', image);
    
    {
      misMatchPercentage : 100, // %
      isSameDimensions: true, // or false
      dimensionDifference: { width: 0, height: -1 }, // defined if dimensions are not the same
      getImageDataUrl: function(){}
    }
    */
    //fs.writeFileSync('./data.json', JSON.stringify(data, null, 4) , 'utf-8');

