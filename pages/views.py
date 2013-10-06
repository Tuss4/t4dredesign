from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from videos.models import Video
import urllib2, json


def about(request):
	a = True
	context = {
		"a": a
	}
	return render(request, 'pages/about.html', context)

def contact(request):
	pass


def portfolio(request):
	pass


def videos(request):
	url = 'https://gdata.youtube.com/feeds/api/users/tuss4dzigns/uploads?alt=json&orderby=published&max-results=50'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	feed = response.read()
	data = json.loads(feed)
	for i in data['feed']['entry']:
		vid = Video()
		vid.video_id = i['id']['$t'][42:]
		vid.thumbnail = i['media$group']['media$thumbnail'][0]['url']
		vid.url = 'http://youtube.com/watch?v='+i['id']['$t'][42:]
		vid.title =i['title']['$t']
		vid.description = i['content']['$t']
		if not Video.objects.filter(video_id=vid.video_id).exists():
			vid.save()
	v = True
	context = {
		"vids": Video.objects.all(),
		"v": v
	}
	return render(request, 'pages/videos.html', context)


def repos(request):
	url = 'https://api.github.com/users/Tuss4/repos?sort=updated'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	feed = response.read()
	data = json.loads(feed)
	vids = []
	g = True
	for i in data:
		vids.append("<li><a href='"+i['html_url']+"' target='_blank'>"+i['name']+"</a></li>")
	context = {
		"repos": vids,
		"g": g
	}
	return render(request, "pages/repos.html", context)	
