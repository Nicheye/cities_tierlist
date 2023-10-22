from django.shortcuts import render,redirect
from . models import City
# Create your views here.
from django.db.models import Q
from .forms import PostCity
from django.core.paginator import Paginator
def main(request):
	cities = City.objects.order_by('-date').all()
	pagin = Paginator(cities,5)
	page_number =request.GET.get("page")
	page_obj = pagin.get_page(page_number)
	return render(request,'main.html',{'page_obj':page_obj})

def create(request):
	if request.method == 'POST':
		form = PostCity(request.POST)
		if form.is_valid():
			citi = form.save()
			return redirect('main')
	else:
		form=PostCity()
		return render(request,'create.html',{'form':form})
	
def search(request):
	if request.method =='GET':
		query = request.GET.get('query')
		if query:
			cities = City.objects.filter(Q(name__icontains=query)).order_by('-date').all()
			pag=Paginator(cities,5)
			page_number =request.GET.get("page")
			page_obj = pag.get_page(page_number)
			return render(request,'search.html',{'cities':cities,'query':query,"page_obj":page_obj})
	else:
		return redirect('main')