from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
	if not 'user' in request.session:
		return redirect(reverse('loginapp-index'))
	else:
		return render(request, 'bookreviews/index.html')