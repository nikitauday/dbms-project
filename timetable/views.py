from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

"""
Syntax of view function: 

def function_name(request):
	return render(request, 'timetable/html_page_name.html', context_dict)
"""

# Create your views here.
def index(request):
	return render(request, 'timetable/index.html')

def register(request):
	return render(request, 'timetable/register.html')

@csrf_exempt
def create_user(request):
	cursor = connection.cursor()
	print(request.POST)
	q_str = "INSERT INTO user(name, email, username, password) VALUES('{}', '{}', '{}', '{}')".format(request.POST['name'], request.POST['email'], request.POST['username'], request.POST['password'])
	print(q_str)
	cursor.execute(q_str)
	return index(request)

def dashboard(request):
	# sql statement  - get details where email  = kittiya email
	# these are the results of the sql  query
	user = 'Adarsh'
	friends = your_func(12)

	context_dict = {} 
	context_dict['name'] = user
	context_dict['message'] = 'hello there my dear ' + user
	context_dict['friends'] = friends
	return render(request, 'timetable/dashboard.html', context_dict)

def interests(request):
	return HttpResponse("Nikita's interests")

def your_func(p):
	random_value = p*100
	return random_value