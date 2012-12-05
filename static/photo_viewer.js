function Button(id) {
	this.id = id;
	this.action = function(){};
	this.enabled = true;
	//$(this.id).hide();
}

Button.prototype.enable = function() {
	if(!this.enabled) {
		this.enabled = true;
		$(this.id).show();
	}
}

Button.prototype.disable = function() {
	if(this.enabled) {
		this.enabled = false;
		$(this.id).hide();
	}
}

function PhotoController(listOfPhotos, selected, leftButton, rightButton) {
	this.listOfPhotos = listOfPhotos;
	this.selected = selected;
	this.leftButton = leftButton;
	this.rightButton = rightButton;
	$(this.selected).show();
	if(this.listOfPhotos.indexOf(this.selected) == 0) {
		this.leftButton.disable();
	}
	if(this.listOfPhotos.indexOf(this.selected) == this.listOfPhotos.length - 1) {
		this.rightButton.disable();
	}
	var instance = this;
	this.leftButton.action = function() {
		instance.previous();
	};
	this.rightButton.action = function() {
		instance.next();
	};
}

PhotoController.prototype.next = function() {
	$(this.selected).hide();
	this.selected = this.listOfPhotos[this.listOfPhotos.indexOf(this.selected) + 1];
	$(this.selected).show();
	if(this.listOfPhotos.indexOf(this.selected) == this.listOfPhotos.length - 1) {
		this.rightButton.disable();
	}
	this.leftButton.enable();
}

PhotoController.prototype.previous = function() {
	$(this.selected).hide();
	this.selected = this.listOfPhotos[this.listOfPhotos.indexOf(this.selected) - 1];
	$(this.selected).show();
	if(this.listOfPhotos.indexOf(this.selected) == 0) {
		this.leftButton.disable();
	}
	this.rightButton.enable();
}

