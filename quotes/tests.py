from django.test import TestCase

import json

def json_update(str):
     j = urllib2.urlopen('http://www.omdbapi.com/?t=bond&y=&plot=short&r=json')
     j_obj = json.load(j)
     for jo in j_obj: 
          print jo['Title']
     return
     
     json_update()
# Create your tests here.
