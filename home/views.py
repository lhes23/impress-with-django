from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Slide
from .forms import slideForm


def index(request):
	return render(request,'home/index.html')

def about(request):
	return render(request,'home/about.html')

def impress(request):
	slide = Slide.objects.all()
	data = {'slide':slide}
	return render(request,'home/impress.html',data)

def insertSlide(request):
	form = slideForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('home:insertSlide')
	data = {'form':form}
	return render(request,'home/insertSlide.html',data)