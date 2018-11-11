var canvas = document.querySelector("canvas")
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var c = canvas.getContext('2d');
boardX = 550;
boardY = 40;
boardWidth = 900;
boardHeight = 900;
c.rect(boardX,boardY,boardWidth,boardHeight)
c.stroke()

//Top left
cornerTileDim = 110;
c.rect(boardX,boardY,cornerTileDim,cornerTileDim)
c.stroke()
c.font = "20px Arial";
text="FREE"
c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2-10);
text="PARKING"
c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2+10);


//Bottom left
BottomYCood = boardY+boardHeight-cornerTileDim
c.rect(boardX,BottomYCood,cornerTileDim,cornerTileDim)
c.stroke()
c.font = "20px Arial";
text="JAIL / JUST"
c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2-10);
text="VISITING"
c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2+10);


//Bottom right
BottomXCood = boardX+boardWidth-cornerTileDim
c.rect(BottomXCood,BottomYCood,cornerTileDim,cornerTileDim)
c.stroke()
c.font = "30px Arial";
text="GO"
c.fillText(text,BottomXCood+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2);

//Top right
TopXCood = boardX+boardWidth-cornerTileDim
c.rect(TopXCood,boardY,cornerTileDim,cornerTileDim)
c.stroke()
c.font = "20px Arial";
text="GO TO"
c.fillText(text,TopXCood+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2-10);
text="JAIL"
c.fillText(text,TopXCood+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2+10);




GroupColorDim = cornerTileDim *0.2
c.font = "10px Arial";
var fontSize = 10;

//Bottom Tiles
botTileWidth=(boardWidth-(cornerTileDim+cornerTileDim)) / 9
botTileHeight=cornerTileDim
botTileStartX = boardX + cornerTileDim
botTileStartY = BottomYCood
var bottomArrayNames = [
["CONNECTICUT","AVENUE"],
["VERMONT","AVENUE"],
["CHANCE"],
["ORIENTAL","AVENUE"],
["READING","RAILROAD"],
["INCOME","TAX"],
["BALTIC","AVENUE"],
["COMMUNITY","CHEST"],
["MEDITER-","RANEAN","AVENUE"]
]
for( var i = 0; i < 9; i++){
	c.rect(botTileStartX,botTileStartY,botTileWidth,botTileHeight)
	c.stroke()	
	if (i == 6 || i == 8){
		c.fillStyle="#38004f";
		c.fillRect(botTileStartX,botTileStartY,botTileWidth,GroupColorDim)
	}
	if (i == 0 || i == 1 || i == 3){
		c.fillStyle="#00d8ff";
		c.fillRect(botTileStartX,botTileStartY,botTileWidth,GroupColorDim)
	}
	c.fillStyle="#000000";
	var currName = bottomArrayNames[i]
	for (var j = 0; j < currName.length; j++){
		var textLeftSpacing = (botTileWidth-c.measureText(currName[j]).width)/2
		c.fillText(currName[j], botTileStartX+textLeftSpacing, botTileStartY+GroupColorDim+fontSize+(j*fontSize) );
	}


	botTileStartX+=botTileWidth
}

//Left Tiles
leftTileWidth=cornerTileDim
leftTileHeight=(boardHeight-(cornerTileDim+cornerTileDim)) / 9
leftTileStartY = boardY + cornerTileDim
leftTileGroupColorXCood = boardX+leftTileWidth-GroupColorDim
var leftArrayNames = [
["NEW YORK","AVENUE"],
["TENNESSEE","AVENUE"],
["COMMUNITY","CHEST"],
["ST. JAMES","PLACE"],
["PENNSYLVANIA","RAILROAD"],
["VIRGINIA","AVENUE"],
["STATES","AVENUE"],
["ELECTRIC","COMPANY"],
["ST. CHARLES","PLACE"]
]
for( var i = 0; i < 9; i++){
	c.rect(boardX,leftTileStartY,leftTileWidth,leftTileHeight)
	c.stroke()

	if (i == 0 || i == 1 || i == 3){
		c.fillStyle="#ffa500";
		c.fillRect(leftTileGroupColorXCood,leftTileStartY,GroupColorDim,leftTileHeight)
	}
	if (i == 5 || i == 6 || i == 8){
		c.fillStyle="#ff00d8";
		c.fillRect(leftTileGroupColorXCood,leftTileStartY,GroupColorDim,leftTileHeight)
	}
	c.fillStyle="#000000";
	var currName = leftArrayNames[i]
	for (var j = 0; j < currName.length; j++){
		var textLeftSpacing = (leftTileWidth - GroupColorDim - c.measureText(currName[j]).width)/2
		c.fillText(currName[j], boardX+textLeftSpacing, leftTileStartY+fontSize+(j*fontSize));
	}
	leftTileStartY+=leftTileHeight

}

//Top Tiles
topTileWidth=(boardWidth-(cornerTileDim+cornerTileDim)) / 9
topTileHeight=cornerTileDim
topTileStartX = boardX + cornerTileDim
topTileGroupColorYCood = boardY + topTileHeight - GroupColorDim
var leftArrayNames = [
["KENTUCKY","AVENUE"],
["CHANCE"],
["INDIANA","AVENUE"],
["ILLINOIS","AVENUE"],
["B. & O.","RAILROAD"],
["ATLANTIC","AVENUE"],
["VENTNOR","AVENUE"],
["WATER","WORKS"],
["MARVIN","AVENUE"]
]
for( var i = 0; i < 9; i++){
	c.rect(topTileStartX,boardY,topTileWidth,topTileHeight)
	c.stroke()
	if (i == 0 || i == 2 || i == 3){
		c.fillStyle="#FF0000";
		c.fillRect(topTileStartX,topTileGroupColorYCood,topTileWidth,GroupColorDim)
	}
	if (i == 5 || i == 6 || i == 8){
		c.fillStyle="#ffee00";
		c.fillRect(topTileStartX,topTileGroupColorYCood,topTileWidth,GroupColorDim)
	}
	c.fillStyle="#000000";
	var currName = leftArrayNames[i]
	for (var j = 0; j < currName.length; j++){
		var textLeftSpacing = (topTileWidth-c.measureText(currName[j]).width)/2
		c.fillText(currName[j], topTileStartX+textLeftSpacing, boardY+fontSize+(j*fontSize));
	}
	topTileStartX+=topTileWidth

}



//Right Tiles
rightTileWidth=cornerTileDim
rightTileHeight=(boardHeight-(cornerTileDim+cornerTileDim)) / 9
rightTileStartY = boardY + cornerTileDim
rightTileStartX = TopXCood
var leftArrayNames = [
["PACIFIC","AVENUE"],
["NORTH","CAROLINA","AVENUE"],
["COMMUNITY","CHEST"],
["PENNSYLVANIA","AVENUE"],
["SHORT","LINE"],
["CHANCE"],
["PARK","PLACE"],
["LUXURY","TAX"],
["BROADWALK"]
]
for( var i = 0; i < 9; i++){
	c.rect(rightTileStartX,rightTileStartY,rightTileWidth,rightTileHeight)
	c.stroke()	
	if (i== 0 || i == 1 || i == 3){
		c.fillStyle="#009650";
		c.fillRect(rightTileStartX,rightTileStartY,GroupColorDim,leftTileHeight)
	}
	if (i== 6 || i == 8){
		c.fillStyle="#00639e";
		c.fillRect(rightTileStartX,rightTileStartY,GroupColorDim,leftTileHeight)
	}
	c.fillStyle="#000000";
	var currName = leftArrayNames[i]
	for (var j = 0; j < currName.length; j++){
		var textLeftSpacing = (rightTileWidth - GroupColorDim - c.measureText(currName[j]).width)/2
		console.log(rightTileWidth + " " + c.measureText(currName[j]).width + " " + textLeftSpacing)
		c.fillText(currName[j], rightTileStartX+GroupColorDim+textLeftSpacing, rightTileStartY+fontSize+(j*fontSize));
	}

	rightTileStartY+=rightTileHeight
}