from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views import generic

from .models import Author
from .models import Quote

import redis
import json

class IndexView(generic.ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'author_list'

    def get_queryset(self):
        return Author.objects.order_by('author_name')
        
    def json_update(request):
     j = urllib2.urlopen('http://www.omdbapi.com/?t=bond&y=&plot=short&r=json')
     j_obj = json.load(j)
     for jo in j_obj: 
          print jo['Title']
     return HttpResponse(jo['title'])

class DetailView(generic.DetailView):
	model = Quote
	template_name = 'quotes/detail.html'


def index(request):
	author_list = Author.objects.order_by('author_name')
	#output = '<ul>'
	#a_href = '<li><a href="/quotes/'
	#for a in author_list:
	#	output += a_href + str(a.id) + '">' + a.author_name + '</a>'

	#return HttpResponse(output)
	return render(request, 'quotes/index.html', {'author_list': author_list})

def detail(request, quote_id):
	try:
		
		quote = Quote.objects.get(pk=quote_id)
	except Quote.DoesNotExist:
		raise Http404('Quote does not exist')

	return render(request, 'quotes/detail.html', {'quote': quote})
	
	
