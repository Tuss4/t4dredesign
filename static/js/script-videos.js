var durl = 'http://youtube.com/embed/';
function getThisId(datum) {
	var newUrl = 'http://youtube.com/embed/'+datum+'?autoplay=1&allowFullScreen=true';
	return newUrl;
};
function changeThisId(datum) {
	$('#ytplayer').attr('src', getThisId(datum));
};
$(document).ready(function() {
	$('.ovid').click(function() {
		$('#vid_overlay').show();
	});
	$('#vidclose').click(function() {
		$('#vid_overlay').hide();
		$('#ytplayer').attr('src', durl);
	});
	$(document).keyup(function(e){
		if (e.keyCode === 27){
			$("#vid_overlay").hide();
			$("#ytplayer").attr("src",durl);
		};
	});
});