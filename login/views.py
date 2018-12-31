from django.shortcuts import render, HttpResponse, redirect

from .models import Profiles
# Create your views here.

from .forms import (

    ProfilesForm,
    searchForm
)

from django import views

def demoProfileList(request,  para = None):
    return render(request,'viewprofile.html',
        {
            'profiles' : Profiles.objects.all() if para == None else Profiles.objects.filter(
                name__icontains = para
            )
        }
    )

def raj(request,para):
    return HttpResponse(
        """<html><body>%s</body></html>"""%(para)
    )

def demologinIndex(request, custid):
    profile = Profiles.objects.get( id = custid)
    if request.POST:
        print (request.FILES)
        form = ProfilesForm(instance = profile, data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                'profile:profilelist'
            )
        else:
            return render(
                request,
                'details.html',
                {
                    'profile' : profile,
                    'form' : form,
                }
            )
    else:
        form = ProfilesForm(instance = profile)
        return render(
            request,
            'details.html',
            {
                'profile' : profile,
                'form' : form,
            }
        )

def demoProfileCreate(request, name, address, age):


    custid = Profiles.objects.create(
            name = name,
            address = address,
            age = age,    
        )
    return redirect(
         'profile:profilelist'
    )

class CreateProfileView(views.View):

    def get(self, request, *args, **kwargs):
        form = ProfilesForm()
        return render(
            request,
            'form.html',
            {
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = ProfilesForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(
                request,
                'form.html',
                {
                    'form': form
                }
            )

        return redirect(
         'profile:profilelist'
        )

    
class SearchProfileView(views.View):

    def get(self, request, *args, **kwargs):
        form = searchForm(initial={'search' : 'name'})
        return render(
            request,
            'form.html',
            {
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = searchForm(data = request.POST)
        if form.is_valid():
            return redirect(
               'profile:profilesearch',
               para = form.cleaned_data['search']
            )   

        else:
           
            return render(
                request,
                'form.html',
                {
                    'form': form
                }
            )

