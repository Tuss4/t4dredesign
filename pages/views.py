from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import urllib2, json


def about(request):
	pass


def contact(request):
	pass


def portfolio(request):
	pass


def videos(request):
	url = 'https://gdata.youtube.com/feeds/api/users/tuss4dzigns/uploads?alt=json&orderby=published'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	feed = response.read()
	data = json.loads(feed)
	vids = []
	for i in data['feed']['entry']:
		vids.append("<img src='"+i['media$group']['media$thumbnail'][0]['url']+"' alt='"+i['title']['$t']+"' title='"+i['title']['$t']+"' /><br />")
	return HttpResponse(vids)


def repos(request):
	url = 'https://api.github.com/users/Tuss4/repos?sort=updated'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	feed = response.read()
	data = json.loads(feed)
	vids = ["<ul>"]
	for i in data:
		vids.append("<li><a href='"+i['html_url']+"'>"+i['name']+"</a></li>")
	vids.append("</ul>")
	return HttpResponse(vids)	
