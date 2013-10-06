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
});