from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
import random

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
	q_str = "INSERT INTO user(name, email, username, password, type) VALUES('{}', '{}', '{}', '{}','{}')".format(request.POST.get('name'), request.POST.get('email'), request.POST.get('username'), request.POST.get('password'),request.POST.get('usertype'))
	print(q_str)
	cursor.execute(q_str)
	return index(request)

@csrf_exempt
def login_response(request):
	cursor=connection.cursor()
	email=request.POST.get('email')
	password=request.POST.get('password')
	a = "SELECT type FROM user WHERE email='{}' and password='{}'".format(request.POST.get('email'),request.POST.get('password'))
	cursor.execute(a)
	result = cursor.fetchall()
	for r in result:
		print(r)
	if(len(result)>1):
		return render(request, 'timetable/index.html')				#when number of records found in DB is more than 1-->
	elif(len(result)==0):											#when password or username  is wrong
		return render(request, 'timetable/index.html')	
	else:
		if(result[0][0]=='Student'):
			return render(request, 'timetable/welcomestudent.html')
		elif(result[0][0]=="HOD"):
			return render(request, 'timetable/welcomeadmin.html')
		else:
			return render(request, 'timetable/welcometeach.html')		

	type = result[0][0]
	name = result[0][1]
	print(result)
	#for res in cursor.fetchall():
		#result = res
	#if len(cursor.fetchall()) == 1:
	#else:
	#	print("Incorrect")
	return HttpResponse("hi you are ")			#removed +name
	


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

	
def view(request):
	return render(request,'timetable/view.html')

def interests(request):
	return HttpResponse("Nikita's interests")
def welcomeadmin(request):
	return render(request, 'timetable/welcomeadmin.html')
def welcometeach(request):
	return render(request, 'timetable/welcometeach.html')
def welcomestudent(request):
	return render(request, 'timetable/welcomestudent.html')




def freehoursee(request):
	return render(request, 'timetable/index.html')				#Replace index.html with the page to see free hours

def createtable(request):
	return render(request, 'timetable/createtable.html')				


def create_func(request):
	cursor=connection.cursor()
	a="Select sname from sub_details where hours=4"
	d="Select sname from sub_details where hours=3"
	b="select ldays from lab_details"
	c="select ltime from lab_details"
	fourhr=[]
	threehr=[]
	labday=[]
	labtime=[]
	
	cursor.execute(a)
	result=cursor.fetchall()
	for i in range(len(result)):
		fourhr.append(result[i][0])
	print(fourhr)


	cursor.execute(d)
	result=cursor.fetchall()
	for i in range(len(result)):
		threehr.append(result[i][0])
	print(threehr)

	cursor.execute(b)
	result=cursor.fetchall()
	for i in range(len(result)):
		labday.append(result[i][0])
	print(labday)

	cursor.execute(c)
	result=cursor.fetchall()
	for i in range(len(result)):
		labtime.append(result[i][0])
	print(labtime)

	
	a=[["free " for j in range(6)] for i in range(5)]
	b=[[0 for j in range(6)] for i in range(5)]
	count=0
    #allocating lab hours


	for k in range(len(labday)):
		for i in range(3):
			if(labtime[k]==1):
				a[labday[k]][i]=" lab "
				b[labday[k]][i]=1
			
			else:
				a[labday[k]][i+3]=" lab "
				b[labday[k]][i+3]=1

	#allocating three hour periods
	for l in range(len(threehr)):
		while count<3:
			i=random.randrange(5)
			j=random.randrange(6)
			if(b[i][j]!=1):
				a[i][j]=threehr[l]
				b[i][j]=1
				count+=1
		count=0     


	#allocating fouhour periods
		
	for l in range(len(fourhr)):
		while count<4:
			i=random.randrange(5)
			j=random.randrange(6)
			if(b[i][j]!=1):
				a[i][j]=fourhr[l]
				b[i][j]=1
				count+=1
		count=0     
			
	for i in range(5):
		for j in range(6):
			print(a[i][j] ,end=" ")
		print('\n')
	query="INSERT INTO finaltable(period1,period2,period3,period4,period5,period6) values(%s,%s,%s,%s,%s,%s)"
	cursor.executemany(query,a)
	connection.commit()
	query="INSERT INTO temptable(period1,period2,period3,period4,period5,period6) values(%s,%s,%s,%s,%s,%s)"
	cursor.executemany(query,a)
	connection.commit()
	return HttpResponse("Nikita's interests")	






def your_func(p):						#random function
	random_value = p*100
	return random_value
