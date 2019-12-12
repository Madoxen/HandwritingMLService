
window.onload = function()
{
	var module = new DrawingModule();
	var clear_button = document.getElementById("clear_button");
	var drawing = false;
	var result_text = document.getElementById("results_text");

	function draw(env)
	{
		if(drawing === true)
		{

			var curr_point = new Point(env.clientX, env.clientY);
			curr_point.x -= module.rect.left;
			curr_point.y -= module.rect.top;
			module.draw(curr_point);

		}
		
	}

	function stopDrawing()
	{
		drawing = false;
		module.last_point = new Point();
	}

	function startDrawing()
	{
		drawing = true;
	}


	//sends image to a server
	function sendDrawing()
	{
		var img_data = module.context.getImageData(0,0, module.canvas.width, module.canvas.height)
		var grayscale_data = prepareDrawing(img_data)
		var xhr = new XMLHttpRequest();
		xhr.open("POST", "/");
		xhr.onreadystatechange = function() { // Call a function when the state changes.
    			if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
        		// Request finished.
			console.log("POST finished");
			result_text.innerHTML = xhr.response
		    }
		}

		xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
		xhr.send(JSON.stringify({"width" : module.canvas.width, "height" : module.canvas.height , "array" : grayscale_data}));
	}


	//Converts image to grayscale, reducing amount of necessary data
	function prepareDrawing(img_data)
	{
		var result = new Array();
		for(i = 3; i < img_data.data.length; i+=4)
		{
			//Convert to greyscale (only alpha counts)	
			result.push(img_data.data[i]);
		}
		return result; 
	}


	//Add canvas event handlers
	module.canvas.onmousemove = draw;
	module.canvas.onmouseup = stopDrawing;
	module.canvas.onmouseleave = stopDrawing;
	module.canvas.onmousedown = startDrawing;
	clear_button.onclick = function() {module.clear()};
	send_button.onclick = sendDrawing;
}


