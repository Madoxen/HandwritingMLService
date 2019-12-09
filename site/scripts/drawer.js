class DrawingModule
{
	constructor()
	{
		this.canvas = document.getElementById("drawing_area");
		this.context = this.canvas.getContext("2d");
		this.rect = this.canvas.getBoundingClientRect();
		this.scale = new Point(this.canvas.width/this.rect.width, this.canvas.height / this.rect.height);	
	}

	
	place_pixel(point)
	{
		this.context.fillStyle = "#000000";
    		this.context.fillRect (point.x, point.y, 1, 1);	
	}
}




