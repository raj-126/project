from django.shortcuts import render, HttpResponse, redirect

from django.views import View

# Create your views here.

def demo(request, *args, **kwargs):
    return HttpResponse(
        """<html><body>Na Malyu Bhai</body></html>""", # Not necessary
        status = 200
    )

def redirectdemo(request, *args, **kwargs):
   return redirect('profiles:profilelanding')

def demorender(request, *args, **kwargs):
    pass# pending till we get to know how django template works

class MyDemoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse(
        """<html><body>IN GET ::</body></html>""", # Not necessary
        status = 200
    )

    def post(self, request, *args, **kwargs):
        return HttpResponse(
        """<html><body>IN POST ::</body></html>""", # Not necessary
        status = 200
    )

    def put(self, request, *args, **kwargs):
        return HttpResponse(
        """<html><body>IN PUT ::</body></html>""", # Not necessary
        status = 200
    )
