from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
import re
# Create your views here.
def index_view(request, *args, **kwargs):
	form = ProductForm()
	context={
		'form':form,
		'is_index':True
	}
	return render(request, 'products/index.html',context)


def product_create_view(request):
	 
	flg=0
	requested_long = request.POST.get('long_text')
	requested_short = request.POST.get('short_text')
	if requested_short==None:
		return render(request, 'products/index.html',{'form':ProductForm})
	else:
		objs = Product.objects.filter(short_text = requested_short)
		if len(objs) !=0:
			flg=1

	if flg == 1:
		nform=ProductForm(initial={'long_text':requested_long})
		return render(request, 'products/already_exist.html',{'form':nform})
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		#print()
		form = ProductForm()
		
	if "http" not in requested_long[:4]:
		requested_long = "https://" + requested_long
	context = {
		'form': form ,
		'shorted_url':requested_short,
		'long_url':requested_long
	}
	return render(request, 'products/shorted.html',context)

def product_fetch(request,fetch_it):
	try:
		obj = Product.objects.get(short_text=fetch_it)
	except Product.DoesNotExist:
		return render(request,'products/error.html')
	redirected_url = obj.long_text
	if "http" not in redirected_url[:4]:
		redirected_url = "https://" + redirected_url
	return redirect(redirected_url)

def handle_error(request):
	return render(request,'products/error.html')