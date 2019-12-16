class DrawingModule
{
	constructor()
	{
		this.canvas = document.getElementById("drawing_area");
		this.context = this.canvas.getContext("2d");
		this.rect = this.canvas.getBoundingClientRect();
		this.scale = new Point(this.canvas.width/this.rect.width, this.canvas.height / this.rect.height);	
		this.last_point = new Point();
	}

	
	draw(point)
	{
		this.context.beginPath();
  		this.context.strokeStyle = 'black';
  		this.context.lineWidth = 15;
  		this.context.moveTo(this.last_point.x, this.last_point.y);
  		this.context.lineTo(point.x, point.y);
  		this.context.stroke();
  		this.context.closePath();
		this.last_point = point;
	}


	clear()
	{
		this.context.clearRect(0,0, this.canvas.width, this.canvas.height);	
	}
}




