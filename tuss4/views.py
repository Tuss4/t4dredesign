from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def main(request):
	h = True
	context = {
		"h": h
	}
	return render(request, 'main.html', context)
