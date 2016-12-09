from django.shortcuts import render
from django.http import HttpResponse
#from collections import namedtuple

from .models import category


# Create your views here.

  #  def get_body():
  #    return 'hello categories'
  #  Response = namedtuple('Response',['get','status_code'])
  #  return Response{
  #   get=get_body, 
  #     'status_code':200
  # }
def get_categories(request):
   html="<html><head></head><body><ul>"
   items = category.objects.all()
   for items in items:
      html += '<li>' + items.name +'</li>'
   html += "</ul></body></html>"
   return HttpResponse(html)

   items =category.objects.all()
   return render(
       request,
       'get_categories.html',
       ('items',items)
            )       
    