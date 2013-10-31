import urllib2, json


def get_data(url):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	feed = response.read()
	data = json.loads(feed)
	return data