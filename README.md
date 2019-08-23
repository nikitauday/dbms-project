TABLES
  1.User Table
    Attributes: -Name
                -Email
                -Username
                -Password
                -Type
    create_user(request)
      When user enters details into html file, and insert into query runs in the backend which collects the required information for the tabel USER
    login_response(request)
      Connection is established with the database. email and password is entered by the user. An SQL Query is run at the backend which validates the credetials and retrieves the type of user and redirects accordingly.
   
   2.sub_details
      Attributes: -sname
                  -hours
      
   3.lab_details
      Attributes: -ldays
                  -ltime
    create_func()
  4.freeperiod
  
      Attributes: -subject
                  -status
  
  
  
