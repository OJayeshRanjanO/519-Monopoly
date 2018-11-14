var canvas = document.querySelector("canvas")
canvas.width = window.innerWidth/2;
canvas.height = window.innerHeight;

var c = canvas.getContext('2d');
boardX = (canvas.width - canvas.width*0.9)/2;//550;
boardY = (canvas.height - canvas.height*0.9)/2;
boardWidth = canvas.width*0.9;
boardHeight = canvas.height*0.9;
var cornerTileDim = 110;
c.rect(boardX,boardY,boardWidth,boardHeight)
c.stroke()

GroupColorDim = cornerTileDim *0.2
var tile_list = []

function CornerTiles(){
		//Top left
	c.rect(boardX,boardY,cornerTileDim,cornerTileDim)
	c.stroke()
	c.font = "20px Arial";
	text="FREE"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2-10);
	text="PARKING"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2+10);
	tile_list.push( new boardObjects("Top Left",boardX,boardY,cornerTileDim,cornerTileDim,"#ffffff",20,"FREE PARKING") )


	//Bottom left
	BottomYCood = boardY+boardHeight-cornerTileDim
	c.rect(boardX,BottomYCood,cornerTileDim,cornerTileDim)
	c.stroke()
	c.font = "20px Arial";
	text="JAIL / JUST"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2-10);
	text="VISITING"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2+10);
	tile_list.push( new boardObjects("Bottom Left",boardX,BottomYCood,cornerTileDim,cornerTileDim,"#ffffff",10,"JAIL / JUST VISITING") )



	//Bottom right
	BottomXCood = boardX+boardWidth-cornerTileDim
	c.rect(BottomXCood,BottomYCood,cornerTileDim,cornerTileDim)
	c.stroke()
	c.font = "30px Arial";
	text="GO"
	c.fillText(text,BottomXCood+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2);
	tile_list.push( new boardObjects("Bottom Right",BottomXCood,BottomYCood,cornerTileDim,cornerTileDim,"#ffffff",0,"GO") )

	//Top right
	TopXCood = boardX+boardWidth-cornerTileDim
	c.rect(TopXCood,boardY,cornerTileDim,cornerTileDim)
	c.stroke()
	c.font = "20px Arial";
	text="GO TO"
	c.fillText(text,TopXCood+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2-10);
	text="JAIL"
	c.fillText(text,TopXCood+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2+10);
	tile_list.push( new boardObjects("Top Right",TopXCood,boardY,cornerTileDim,cornerTileDim,"#ffffff",30,"GO TO JAIL") )
}

function RightTiles(){
	c.font = "10px Arial";
	var fontSize = 10;

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
		var rightObject = new boardObjects("Right",rightTileStartX,rightTileStartY,rightTileWidth,rightTileHeight,c.fillStyle,(i+30),"");

		c.fillStyle="#000000";
		var tileName = "";
		var currName = leftArrayNames[i]
		for (var j = 0; j < currName.length; j++){
			var textLeftSpacing = (rightTileWidth - GroupColorDim - c.measureText(currName[j]).width)/2
			// console.log(rightTileWidth + " " + c.measureText(currName[j]).width + " " + textLeftSpacing)
			tileName += currName[j] + " ";
			c.fillText(currName[j], rightTileStartX+GroupColorDim+textLeftSpacing, rightTileStartY+fontSize+(j*fontSize));
		}
		rightObject.name = tileName;
		tile_list.push(rightObject);

		rightTileStartY+=rightTileHeight
	}
}

function TopTiles(){
	c.font = "10px Arial";
	var fontSize = 10;

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
		else if (i == 5 || i == 6 || i == 8){
			c.fillStyle="#ffee00";
			c.fillRect(topTileStartX,topTileGroupColorYCood,topTileWidth,GroupColorDim)
		}else{
			c.fillStyle = "#ffffff";
		}
		var topObject = new boardObjects("Top",topTileStartX,boardY,topTileWidth,topTileHeight,c.fillStyle,(i+20),"");

		c.fillStyle="#000000";
		var currName = leftArrayNames[i];
		var tileName = "";
		for (var j = 0; j < currName.length; j++){
			var textLeftSpacing = (topTileWidth-c.measureText(currName[j]).width)/2;
			tileName+=currName[j] + " ";
			c.fillText(currName[j], topTileStartX+textLeftSpacing, boardY+fontSize+(j*fontSize));
		}
		topObject.name = tileName;
		tile_list.push(topObject);
		topTileStartX+=topTileWidth
	}

}

function LeftTiles(){
	c.font = "10px Arial";
	var fontSize = 10;

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
		else if (i == 5 || i == 6 || i == 8){
			c.fillStyle="#ff00d8";
			c.fillRect(leftTileGroupColorXCood,leftTileStartY,GroupColorDim,leftTileHeight)
		}else {
			c.fillStyle="#ffffff"
		}
		var leftObject = new boardObjects("Left",boardX,leftTileStartY,leftTileWidth,leftTileHeight,c.fillStyle,(19-i),"");
		c.fillStyle="#000000";
		var currName = leftArrayNames[i];
		var tileName = "";
		for (var j = 0; j < currName.length; j++){
			var textLeftSpacing = (leftTileWidth - GroupColorDim - c.measureText(currName[j]).width)/2
			tileName += currName[j] + " ";
			c.fillText(currName[j], boardX+textLeftSpacing, leftTileStartY+fontSize+(j*fontSize));
		}
		leftObject.name = tileName;
		tile_list.push(leftObject)
		leftTileStartY+=leftTileHeight

	}

}

function BottomTiles(){
	c.font = "10px Arial";
	var fontSize = 10;

	//Bottom Tiles
	var botTileWidth=(boardWidth-(cornerTileDim+cornerTileDim)) / 9
	var botTileHeight=cornerTileDim
	var botTileStartX = boardX + cornerTileDim
	var botTileStartY = BottomYCood
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
		else if (i == 0 || i == 1 || i == 3){
			c.fillStyle="#00d8ff";
			c.fillRect(botTileStartX,botTileStartY,botTileWidth,GroupColorDim)
		}else {
			c.fillStyle="#ffffff"
		}
		var bottomObject = new boardObjects("Bottom",botTileStartX,botTileStartY,botTileWidth,botTileHeight,c.fillStyle,(9-i),"");
		c.fillStyle="#000000";
		var currName = bottomArrayNames[i]
		var tileName = ""
		for (var j = 0; j < currName.length; j++){
			var textLeftSpacing = (botTileWidth-c.measureText(currName[j]).width)/2
			tileName += currName[j] + " "
			c.fillText(currName[j], botTileStartX+textLeftSpacing, botTileStartY+GroupColorDim+fontSize+(j*fontSize) );
		}
		bottomObject.name = tileName;
		tile_list.push(bottomObject)

		botTileStartX+=botTileWidth
	}
}

function boardObjects(direction,x,y,width,height,color,index,name) {
	this.direction = direction;
	this.x = x;
	this.y = y;
	this.width = width;
	this.height = height;
	this.color = color;
	this.index = index;
	this.name = name;
}

var testState = {
	"turn":5,
	"current_player":1,
	"jailed":[false,false],
	"status":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	"position":[10,39],
	"liquid_cash":[1500,1500],
	"total_wealth":[1500,1500],
	"liquid_assets":[1500,1500],
	"phase":3,
	"phase_info":null,
	"debt":0,
	"previous_states":[],	
	"card_history":[],		
	"percent_own_buildings":[0.0,0.0],
	"percent_own_money":[0, 0],
	"total_transacted_wealth":[0.0, 0.0],
	"trades_p1":[],
	"trades_p2":[],
	"trades_attempmted":[0, 0], 
	"hotels_left":12,
	"houses_left":32,
	"monopolies_held":[0,0,0,0,0,0,0,0,0,0],
	"wait_count":[0, 0]	
}


function drawPlayer(state){
	for (var i = 0; i < 2; i++){
		var player_loc = state.position;
		var obj = tile_list[player_loc[i]];

		c.beginPath();
		var radius = 10;
	    c.fillStyle = i == 0 ? "red" : "blue";
	    if (state.jailed[i]){
	    	c.fillStyle = "grey";
	    }
	    var playerLocX = 0;
	    var playerLocY = 0;
	    if (obj.direction == "Bottom" || obj.direction == "Bottom Left" || obj.direction == "Bottom Right" || obj.direction == "Top Left" || obj.direction == "Top Right"){
	    	playerLocX = i == 0 ? obj.x + obj.width - (radius*2) : obj.x + (radius*2)
	    	playerLocY = obj.y + obj.height-(radius*2);
	    }else if (obj.direction == "Left"){
	    	playerLocX = i == 0 ? obj.x + obj.width - GroupColorDim - (radius*2) : obj.x + (radius*2)
	    	playerLocY = obj.y + obj.height-(radius*2);
	    }else if (obj.direction == "Top"){
	    	playerLocX = i == 0 ? obj.x + obj.width - (radius*2) : obj.x + (radius*2)
	    	playerLocY = obj.y + obj.height - GroupColorDim - (radius*2);
	    }else if (obj.direction == "Right"){
	    	playerLocX = i == 0 ? obj.x + obj.width - (radius*2) : obj.x + (radius*2) + GroupColorDim
	    	playerLocY = obj.y + obj.height-(radius*2);
	    }

	    c.arc(playerLocX, playerLocY, radius, 0, 2 * Math.PI, false);
	    c.fill();
	    c.fillStyle = "white";
	    c.fillText(i+1,playerLocX-(c.measureText(i+1).width/2),playerLocY+(c.measureText(i+1).width/2)  );
	    c.closePath();
	}
}
var obj = tile_list[1]
function loadPlayerProperties(state){
	var properties = state.
	if ()
}


function loadBoard(state){

	CornerTiles()

	BottomTiles()

	LeftTiles()

	TopTiles()

	RightTiles(state)

	tile_list.sort((a,b) => (a.index > b.index) ? 1 : ((b.index > a.index) ? -1 : 0)); 

	drawPlayer(state)


}

loadBoard(testState)

console.log(tile_list)