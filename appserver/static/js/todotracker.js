window.TTWT = {
		apps:{},
		widgets:{}
}

TTWT.widgets.NavClick=function(selector) {
	this.navbar=selector;
	this.navbar.find('.nav_click').each(function() {
		console.log(this);
	});
};

TTWT.apps.Frontend=function(selector) {
	this.frontend=selector;
	var nav=this.frontend.find('#navigation');
	this.navigation=new TTWT.widgets.NavClick(nav);
}
TTWT.apps.Tasks=function() {
	console.log('hello');
};


$(document).ready(function() {
	frontend=new TTWT.apps.Frontend($('body'));
});
