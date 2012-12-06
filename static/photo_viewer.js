function ElementList() {
	this.list = new Array();
}

ElementList.prototype.addId = function(element) {
	this.list.push("#" + element);
}

ElementList.prototype.getList = function() {
	return this.list;
}

function Button(element) {
	this.id = "#" + element;
	this.enabled = true;
	this.action = function() {};
}

Button.prototype.enable = function() {
	if(!this.enabled) {
		this.enabled = true;
		$(this.id).show();
	}
}

Button.prototype.disable = function() {
	if(this.enable) {
		this.enable = false;
		$(this.id).hide();
	}
}

function PhotoController(listOfPhotos, previousButton, nextButton, splash) {
	this.selected = listOfPhotos[0];
	this.listOfPhotos = listOfPhotos;
	this.previousButton = previousButton;
	this.nextButton = nextButton;
	this.splash = splash;
	var instance = this;
	this.previousButton.action = function() {
		instance.previous();
	}
	this.nextButton.action = function() {
		instance.next();
	}
}

PhotoController.prototype.previous = function() {
	$(this.selected).hide();
	this.selected = this.listOfPhotos[this.listOfPhotos.indexOf(this.selected) - 1];
	$(this.selected).show();
	if(this.listOfPhotos.indexOf(this.selected) == 0) {
		this.previousButton.disable();
	}
	this.nextButton.enable();
}

PhotoController.prototype.next = function() {
	$(this.selected).hide();
	this.selected = this.listOfPhotos[this.listOfPhotos.indexOf(this.selected) + 1];
	$(this.selected).show();
	if(this.listOfPhotos.indexOf(this.selected) == this.listOfPhotos.length) {
		this.nextButton.disable();
	}
	this.previousButton.enable();
}

PhotoController.prototype.splashOn = function(selected) {
	this.selected = selected;
	$(this.splash).show();
	$(this.selected).show();
	this.previousButton.enable();
	this.nextButton.enable();
	if(this.listOfPhotos.indexOf(this.selected) == 0) {
		this.previousButton.disable();
	}
	if(this.listOfPhotos.indexOf(this.selected) == this.listOfPhotos.length) {
		this.nextButton.disable();
	}
}

PhotoContoller.prototype.splashOff = function() {
	$(this.selected).hide();
	$(this.splash).hide();
}

