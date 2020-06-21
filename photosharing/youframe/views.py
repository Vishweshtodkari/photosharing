from django.shortcuts import render, redirect 
from django.http import HttpResponse 
from .models import Destination


# Create your views here. 
def index(request):
	load = Destination.objects.all()
	return render(request, 'index.html',{'load':load}) 


def uploadImage(request): 
	p =request.FILES['image']
	user = Destination(img =p)
	user.save()

	return redirect('/')
