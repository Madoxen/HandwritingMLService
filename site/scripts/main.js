
window.onload = function()
{
	var module = new DrawingModule();
	var clear_button = document.getElementById("clear_button")
	var drawing = false;

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



	//Add canvas event handlers
	module.canvas.onmousemove = draw;
	module.canvas.onmouseup = stopDrawing;
	module.canvas.onmouseleave = stopDrawing;
	module.canvas.onmousedown = startDrawing;
	clear_button.onclick = function() {module.clear()};

}


