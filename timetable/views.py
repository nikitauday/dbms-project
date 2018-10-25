from django.shortcuts import render, HttpResponse

"""
Syntax of view function: 

def function_name(request):
	return render(request, 'timetable/html_page_name.html', context_dict)
"""

# Create your views here.
def index(request):
	return render(request, 'timetable/index.html')

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