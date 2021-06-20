from django.urls import path
from .views import HttpResponse

urlpatterns= [
		path('',homePageView, name='home')

]