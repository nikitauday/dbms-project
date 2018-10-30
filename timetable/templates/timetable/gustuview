def login_response(request):
	cursor=connection.cursor()
	email=request.POST.get('email')
	password=request.POST.get('password')
	try:
		a = "SELECT type FROM user WHERE email='{}' and password='{}'".format(request.POST.get('email'),request.POST.get('password'))
	except:
		pass
	a = "SELECT * FROM user WHERE email='{}'".format(request.POST.get('email'))
	cursor.execute(a)
	result = cursor.fetchall()
	print(result)
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
	return HttpResponse("hi you are "+name)