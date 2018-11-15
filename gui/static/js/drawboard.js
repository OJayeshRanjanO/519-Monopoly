var canvas = document.querySelector("canvas")
var c = canvas.getContext('2d');

if (screen.height <= 810){//James's screen
	if (screen.width <= 1024){
		canvas.width = window.innerWidth;
	}else{
		canvas.width = window.innerWidth*0.65;
	}
	canvas.height = window.innerHeight;

	var cornerTileDim = 80;

	var cornerTileFontSize = 12;
	var fontSize = 8;
	var radius = 8;
	var playerInfoFontSize = 12;
	var playerDotSize = 12;

}
else if (screen.height<=960){//Other People's screen
	if (screen.width <= 1200){
		canvas.width = window.innerWidth;
	}else if (screen.width <= 1440){
		canvas.width = window.innerWidth * 0.75;
	}else{
		canvas.width = window.innerWidth * 0.65;
	}
	canvas.height = window.innerHeight;

	var cornerTileDim = 90;

	var cornerTileFontSize = 15;
	var fontSize = 9;
	var radius = 9;
	var playerInfoFontSize = 15;
	var playerDotSize = 11;

}
else if (screen.height<=1080){//My Screen
	if (screen.width <= 1280){
		canvas.width = window.innerWidth;
	}else if (screen.width <= 1400){
		canvas.width = window.innerWidth * 0.75;
	}else if (screen.width <= 1920){
		canvas.width = window.innerWidth * 0.65;
	}else{
		canvas.width = window.innerWidth * 0.5;
	}
	canvas.height = window.innerHeight;

	var cornerTileDim = 110;

	var cornerTileFontSize = 20;
	var fontSize = 10;
	var radius = 10;
	var playerInfoFontSize = 20;
	var playerDotSize = 12;

}

canvas.style.left = (window.innerWidth - canvas.width)/2 + "px";

var boardX = (canvas.width - canvas.width*0.9)/2;//550;
var boardY = (canvas.height - canvas.height*0.9)/2;
var boardWidth = canvas.width*0.9;
var boardHeight = canvas.height*0.9;
c.rect(boardX,boardY,boardWidth,boardHeight)
c.stroke()

console.log(screen.width+ " " +screen.height)
GroupColorDim = cornerTileDim *0.2

var tile_list = []

var boardStates = []

var currentIndex = 0;

function CornerTiles(){
		//Top left
	c.beginPath()
	c.rect(boardX,boardY,cornerTileDim,cornerTileDim)
	c.stroke()
	c.font = cornerTileFontSize+"px Arial";
	c.fillStyle = "black";
	text="FREE"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2-(cornerTileFontSize/2));
	text="PARKING"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2+(cornerTileFontSize/2));
	tile_list.push( new boardObjects("Top Left",boardX,boardY,cornerTileDim,cornerTileDim,"#ffffff",20,"FREE PARKING") )
	c.closePath()

	//Bottom left
	c.beginPath()
	BottomYCood = boardY+boardHeight-cornerTileDim
	c.rect(boardX,BottomYCood,cornerTileDim,cornerTileDim)
	c.stroke()
	c.fillStyle = "black";
	c.font = cornerTileFontSize+"px Arial";
	text="JAIL / JUST"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2-(cornerTileFontSize/2));
	text="VISITING"
	c.fillText(text,boardX+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2+(cornerTileFontSize/2));
	tile_list.push( new boardObjects("Bottom Left",boardX,BottomYCood,cornerTileDim,cornerTileDim,"#ffffff",10,"JAIL / JUST VISITING") )
	c.closePath()

	//Bottom right
	c.beginPath()
	BottomXCood = boardX+boardWidth-cornerTileDim
	c.rect(BottomXCood,BottomYCood,cornerTileDim,cornerTileDim)
	c.stroke()
	c.fillStyle = "black";
	c.font = cornerTileFontSize*1.3+"px Arial";
	text="GO"
	c.fillText(text,BottomXCood+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2-(cornerTileFontSize/2));
	text="\u{1F844}"
	c.fillText(text,BottomXCood+cornerTileDim/2-c.measureText(text).width/2,BottomYCood+cornerTileDim/2+(cornerTileFontSize/2));
	tile_list.push( new boardObjects("Bottom Right",BottomXCood,BottomYCood,cornerTileDim,cornerTileDim,"#ffffff",0,"GO") )
	c.closePath()

	//Top right
	c.beginPath()
	TopXCood = boardX+boardWidth-cornerTileDim
	c.rect(TopXCood,boardY,cornerTileDim,cornerTileDim)
	c.stroke()
	c.fillStyle = "black";
	c.font = cornerTileFontSize+"px Arial";
	text="GO TO"
	c.fillText(text,TopXCood+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2-(cornerTileFontSize/2));
	text="JAIL"
	c.fillText(text,TopXCood+cornerTileDim/2-c.measureText(text).width/2,boardY+cornerTileDim/2+(cornerTileFontSize/2));
	tile_list.push( new boardObjects("Top Right",TopXCood,boardY,cornerTileDim,cornerTileDim,"#ffffff",30,"GO TO JAIL") )
	c.closePath()
}

function RightTiles(){
	c.font = fontSize+"px Arial";

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
		c.beginPath()
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
		c.beginPath()

	}
}

function TopTiles(){
	c.font = fontSize + "px Arial";

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
	c.font = fontSize+"px Arial";

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
	c.font = fontSize+"px Arial";

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

function drawPlayer(state){
	for (var i = 0; i < 2; i++){
		var player_loc = state.position;
		var obj = tile_list[player_loc[i]];

		c.beginPath();
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
	    	playerLocY = obj.y + obj.height-(radius*2.5);
	    }else if (obj.direction == "Top"){
	    	playerLocX = i == 0 ? obj.x + obj.width - (radius*2) : obj.x + (radius*2)
	    	playerLocY = obj.y + obj.height - GroupColorDim - (radius*2);
	    }else if (obj.direction == "Right"){
	    	playerLocX = i == 0 ? obj.x + obj.width - (radius*2) : obj.x + (radius*2) + GroupColorDim
	    	playerLocY = obj.y + obj.height-(radius*2.5);
	    }
	    c.arc(playerLocX, playerLocY, radius, 0, 2 * Math.PI, false);
	    c.fill();
	    c.fillStyle = "white";
	    c.font = playerDotSize + "px Arial"
	    c.fillText(i+1,playerLocX-(c.measureText(i+1).width/2),playerLocY+(c.measureText(i+1).width/2)  );
	    c.closePath();
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

function loadPlayerProperties(state){
		// console.log(tile_list)
		// console.log(obj)
	var hotel = "\u{1F3E2}"
	var house = "\u{1F3E0}"
	var owned = "OWNED"
	var mortgaged = "MORTGAGED"
	var unowned = "UNOWNED"

	var status = state.status;
	// var properties = tile_list;
	for (var i = 0; i < tile_list.length;i++){
		var obj = tile_list[i]
		status_value = status[i];
		var text = "";
		if (status_value == 0){
			c.font = fontSize+"px Arial";
			text = unowned;
		}
		else if(status_value == 1 || status_value == -1){
			c.font = fontSize+"px Arial";
			text = owned
		}
		else if ( (status_value > -6 && status_value < -1) || (status_value > 1 && status_value < 6)){//HOUSE
			c.font = fontSize*1.5 + "px Arial";
			text = ""
			var num_houses = Math.abs(status_value) - 1;
			for (var j = 0; j < num_houses; j++){
				text+=house
			}
		}else if (status_value == 6 || status_value == -6){
			c.font = fontSize * 2 + "px Arial";
			text = hotel
		}else if (status_value == 7 || status_value == -7){
			c.font = fontSize + "px Arial";
			text = mortgaged
		}
		var tileLocX=0;
		var tileLocY=0;
		if (i != 2 && i!= 4 && i!= 7 && i!=17 && i!= 22 && i!=33 && i!= 36 && i!=38){
			if (obj.direction == "Bottom"){
				tileLocX = obj.x + (obj.width/2) - (c.measureText(text).width/2);
				tileLocY = obj.y + obj.height - c.measureText("B").width/2;
			}else if (obj.direction == "Left"){
				tileLocX = obj.x + ((obj.width-GroupColorDim)/2) - (c.measureText(text).width/2);
				tileLocY = obj.y + obj.height - c.measureText("B").width/2;
			}else if (obj.direction == "Top"){
				tileLocX = obj.x + (obj.width/2) - (c.measureText(text).width/2);
				tileLocY = obj.y + (obj.height - GroupColorDim) - c.measureText("B").width/2;
			}else if (obj.direction == "Right"){
				tileLocX = obj.x + ((obj.width+GroupColorDim)/2) - (c.measureText(text).width/2);
				tileLocY = obj.y + obj.height - c.measureText("B").width/2;
			}
		}


		if (status_value < 0){c.fillStyle = "blue";}
		else if (status_value > 0){c.fillStyle = "red";}
		else {c.fillStyle = "grey";}


		c.fillText(text,tileLocX,tileLocY );

	}
}

function showStats(state){
	var player1 = document.getElementById("player1");
	// (window.innerWidth - canvas.width)/2
	canvasEdge = (window.innerWidth - canvas.width)/2
	tileWidth = tile_list[22].width
	player1.style.left = canvasEdge + boardX + cornerTileDim + tileWidth + "px"//(window.innerWidth - canvas.width)/2 + "px";
	// console.log(player1.style.left + " " +tile_list[22].x)
	player1.style.top = boardY+cornerTileDim+c.measureText("M").width + "px";
	player1.style.fontSize = playerInfoFontSize+"px";
	
	player1.innerHTML = state.current_player == 0 ? "&#9654;" + "<b>PLAYER 1</b>" : "<b>PLAYER 1</b>";
	player1.innerHTML += state.jailed[0] ?  " (JAIL: " + state.wait_count[0]+")" : ""
	player1.innerHTML += "<br>Liquid Cash: $" + state.liquid_cash[0]
	player1.innerHTML += "<br>Total Wealth: $" + state.total_wealth[0]
	player1.innerHTML += "<br>Liquid Assets: $" + state.liquid_assets[0]
	player1.innerHTML += "<br>Debt:" + state.debt
	player1.innerHTML += "<br>Buildings Owned:" + state.percent_own_buildings[0] + "%"
	player1.innerHTML += "<br>Money Owned:" + state.percent_own_buildings[0] + "%"
	player1.innerHTML += "<br>Transacted Wealth:" + state.total_transacted_wealth[0]
	// player1.innerHTML += "<br><br>TRADES:";

	var turn = document.getElementById("turn");
	turn.innerText = "Turn " + state.turn;
	turn.style.left = canvasEdge + boardX + cornerTileDim + tileWidth*4 + "px";
	turn.style.top = boardY+cornerTileDim+c.measureText("M").width + "px";
	turn.style.fontSize = playerInfoFontSize+"px";


	var player2 = document.getElementById("player2");
	player2.style.fontSize = playerInfoFontSize+"px";

	player2.style.left = canvasEdge + boardX + cornerTileDim + tileWidth*6 + "px";
	player2.style.top = boardY+cornerTileDim +c.measureText("M").width+ "px";
	player2.innerHTML = state.current_player == 1 ?  "&#9654;" + "<b>PLAYER 2</b>" : "<b>PLAYER 2</b>";
	player2.innerHTML += state.jailed[1] ?  " (JAIL: " + state.wait_count[1]+")" : ""

	player2.innerHTML += "<br>Liquid Cash: $" + state.liquid_cash[1]
	player2.innerHTML += "<br>Total Wealth: $" + state.total_wealth[1]
	player2.innerHTML += "<br>Liquid Assets: $" + state.liquid_assets[1]
	player2.innerHTML += "<br>Debt:" + state.debt
	player2.innerHTML += "<br>Buildings Owned:" + state.percent_own_buildings[1] + "%"
	player2.innerHTML += "<br>Money Owned:" + state.percent_own_buildings[1] + "%"
	player2.innerHTML += "<br>Transacted Wealth:" + state.total_transacted_wealth[1]
	// player2.innerHTML += "<br><br>TRADES:";

}
function goChangeState(direction){
	if (direction == "prev"){
		if (currentIndex > 0){
			currentIndex-=1;
		}
	}else if (direction == "next"){
		if (currentIndex < boardStates.length-1){
			currentIndex+=1;
		}
	}
	loadBoard(boardStates[currentIndex])
	console.log(currentIndex)
}

function drawButtons(){
	var prev = document.getElementById("prev");
	var next = document.getElementById("next");
	next.style.width = cornerTileDim + "px";
	prev.style.width = cornerTileDim+ "px";

	next.style.height = boardY /2+ "px";
	prev.style.height = boardY/2+ "px";
	// console.log(next.style.height + " TEST ")

	prev.style.left = canvasEdge + boardX + "px";
	next.style.left = canvasEdge + boardX + boardWidth - cornerTileDim + "px";

	prev.style.top = (boardY - boardY/2)/2 + "px"
	next.style.top = (boardY - boardY/2)/2 + "px"


}
function loadBoard(state){
	c.clearRect(0, 0, canvas.width, canvas.height);
	tile_list = []

	CornerTiles()

	BottomTiles()

	LeftTiles()

	TopTiles()

	RightTiles()

	tile_list.sort((a,b) => (a.index > b.index) ? 1 : ((b.index > a.index) ? -1 : 0)); 

	drawPlayer(state);

	loadPlayerProperties(state);

	showStats(state);

	drawButtons();

}

$( document ).ready(function() {

	 $.ajax({
      type: "POST",
      url: "/fetch_gamestate",
      dataType: "json",
      contentType : "application/json"
    }).done(function (data, textStatus, jqXHR) {
        // var data = data.cruiseList;
        // console.log(data.game_state_array);
        boardStates = data.game_state_array;
        // console.log(boardStates);
        loadBoard(boardStates[currentIndex]);

    }).fail(function(jqXHR, textStatus, errorThrown) { 
    	alert(textStatus + " " + jqXHR); 
    });

});