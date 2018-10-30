USE timetable;
Create table sub_details(sname varchar(8),hours int);
insert into sub_details VALUES("TOC",4);
insert into sub_details VALUES("MM",3);
insert into sub_details VALUES("GTC",4);
insert into sub_details VALUES("SS",3);
insert into sub_details VALUES("SC",3);
insert into sub_details VALUES("DC",3);
insert into sub_details VALUES("DP",3);
select * from sub_details;

Select sname from sub_details where hours=4;
Create table lab_details(lname varchar(8),lhours int,ldays int,ltime INT);
insert into lab_details values("Lab1",3,4,1);
insert into lab_details values("Lab2",3,1,2);
select * from lab_details;
drop table lab_details;