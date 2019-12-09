
window.onload = function()
{
	var module = new DrawingModule();
	var drawing = false;

	function draw(env)
	{
		if(drawing == true)
		{

			var curr_point = new Point(env.clientX, env.clientY);
			curr_point.x -= module.rect.left;
			curr_point.y -= module.rect.top;
			module.place_pixel(curr_point);

		}
		
	}

	module.canvas.onmousemove = draw;
	module.canvas.onmouseup = function() {drawing = false;};
	module.canvas.onmouseleave = function() {drawing = false;};
	module.canvas.onmousedown = function() {drawing = true;};

}


