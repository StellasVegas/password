from django.shortcuts import render
from django.http import HttpResponse
import random, time

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def description(request):
	a=time.strftime("%Y %b %d %X") 
	return render(request, 'generator/description.html', {"time":a })

def password(request):

	characters = list('asdfgwqertertkjl')
	
	if request.GET.get('uppercase'):
		characters.extend(list('ASDFGHJQWERTYU'))
	if request.GET.get('special'):
		characters.extend(list('!@#$%^&**('))

	length = int(request.GET.get('length',12))
	thepassword =''
	for x in range(length):
		thepassword+=random.choice(characters)

	return render(request, 'generator/password.html',{"password":thepassword})

	