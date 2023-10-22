
from django.urls import path,include
from . import views
urlpatterns = [
    
	path('', views.main,name="main"),
	path('create/',views.create,name='create'),
	path('search/',views.search,name='search')
]
