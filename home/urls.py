from django.urls import path
from . import views

app_name = 'home'

urlpatterns =  [
	path('',views.index,name='index'),
	path('about/',views.about,name='about'),
	path('impress/',views.impress,name='impress'),
	path('insertSlide/',views.insertSlide,name='insertSlide'),

]