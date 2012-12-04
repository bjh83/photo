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
	for(photo in this.listOfPhotos) {
		$(photo).hide();
	}
	$(this.selected).show();
	if(this.listOfPhotos.indexOf(this.selected) == 0) {
		this.leftButton.disable();
	}
	if(this.listOfPhotos.indexOf(this.selected) == this.listOfPhotos.length - 1) {
		this.rightButton.disable();
	}
	this.leftButton.action = this.next;
	this.rightButton.action = this.previous;
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

