from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from pages.forms import Contact
from videos.models import Video
import urllib2, json, os
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


def about(request):
	a = True
	context = {
		"a": a
	}
	return render(request, 'pages/about.html', context)

def contact(request):
	form = Contact()
	if request.method == 'POST':
		form = Contact(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			send_mail(
				data['subject']
				, data['message']+'\n'+data['email']
				, 'tjs@tuss4.webfactional.com'
				, ['tuss4dbfn@gmail.com']
				, fail_silently=False
				)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse("Yeah that stuff wasn't valid, dude.")
	c = True
	context = {
		"form": form,
		"c": c
	}
	return render(request, 'pages/contact.html', context)


def portfolio(request):
	path = r'g:/t4dredesign/static/cgi/'
	gallery = os.listdir(path)
	p = True
	context = {
		"p": p,
		"gallery": gallery
	}
	return render(request, 'pages/portfolio.html', context)


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
		vid.date = i['published']['$t']
		if not Video.objects.filter(video_id=vid.video_id).exists():
			vid.save()
	v = True
	v_list = Video.objects.all()
	paginator = Paginator(v_list, 5)

	page = request.GET.get('page')
	try:
		vs = paginator.page(page)
	except PageNotAnInteger:
		vs = paginator.page(1)
	except EmptyPage:
		vs = paginator.page(paginator.num_pages)
	context = {
		"vids": vs,
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


def blog(request):
	url = 'https://public-api.wordpress.com/rest/v1/sites/tricking.tuss4dzigns.com/posts'
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	feed = response.read()
	data = json.loads(feed)
	vids = []
	b = True
	for i in data['posts']:
		vids.append(
			"<h2><a href='"+i['short_URL']+"' target='_blank'>"+i['title']+"</a></h2>\n"+i['date']+"\n"+i['content']
			)
	context = {
		"b": b,
		"posts": vids
	}
	return render(request, "pages/blog.html", context)
