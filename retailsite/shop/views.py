from django.shortcuts import render

def index(request):
	return render(request, 'shop/index.html')
	
def products(request):
	return render(request, 'shop/products.html')
	
def contact(request):
	return render(request, 'shop/Contact.html')
	
def signin(request):
	return render(request, 'shop/Signin.html')

