
window.onload = function()
{
	var module = new DrawingModule();

	function draw(env)
	{
		var curr_point = new Point(env.ClientX, env.ClientY);
		curr_point.x -= module.rect.left;
		curr_point.y -= module.rect.top;
		module.place_pixel(curr_point);
	}

	module.canvas.onmousemove = draw;
}


