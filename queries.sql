CREATE DATABASE timetable;
USE timetable;

CREATE TABLE user(id INT PRIMARY KEY auto_increment DEFAULT 0, name varchar(16), email varchar(20), username varchar(16), password varchar(16));

SELECT * from user;
