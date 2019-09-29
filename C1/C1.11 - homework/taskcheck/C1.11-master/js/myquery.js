function myQuery (selector, context = document){
	if(selector != document){
		this.elements = Array.from(context.querySelectorAll(selector));	
	}
	return this
}

myQuery.prototype.ready = function(fn){
	document.addEventListener("DOMContentLoaded", fn);
}

myQuery.prototype.each = function (fn){
	this.elements.forEach((element, index) => fn.call(element, element, index));
	return this;
}

myQuery.prototype.click = function(fn){
	this.each(element => element.addEventListener('click', fn))
	return this
}

myQuery.prototype.change = function(fn){
	this.each(element => element.addEventListener('change', fn))
}

myQuery.prototype.hide = function(){
	this.each(element => element.style.display = 'none')
  return this;
}

myQuery.prototype.show = function(){
	this.each(element => element.style.display = '')
  return this;
}

myQuery.prototype.remove = function(){
	this.each(element => element.remove())
  return this;
}

myQuery.prototype.class = function(name){
	this.each(element => element.className = name)
  return this;
}

myQuery.prototype.value = function(value){
	element = this.elements[0];
	if (typeof(value) == 'string'){
		element.value = value;
	} 
	else if (typeof(value) == 'function'){
		element.value = value();
	}
	return element.value;
}

myQuery.prototype.html = function(html){
	element = this.elements[0];
	if (typeof(html) == 'string'){
		element.innerHTML = html;
	} 
	else if (typeof(html) == 'function'){
		element.innerHTML = html();
	}
	return element.innerHTML;
}

myQuery.prototype.text = function(text){
	element = this.elements[0];
	if (typeof(text) == 'string'){
		element.textContent = text;
	}
	else if (typeof(text) == 'function'){
		element.textContent = text();
	}
	return element.textContent;
}

const $ = (e) => new myQuery(e);