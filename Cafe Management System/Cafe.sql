create database Cafe_Menu
use Cafe
create table Eatables(Food varchar(100),Prices float )
sp_help Eatables
create table Refreshments(Drinks varchar(100),Prices float)
sp_help Refreshments
create table Employee (Employee_ID int, Employee_Name varchar(100),Cell_phone int,Email varchar(100), Job varchar (100))

select * from Eatables