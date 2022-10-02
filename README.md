"Cafe-Management-System"
The main objective of this project is to provide fast and easy service to the customers, admin, and employees of the cafe. This management system will reduce the manual work for managing the café. I have applied all the knowledge I gained about database system so far along with my knowledge about python and Kivy for the execution of this Café Management system.


"Libraries"
Following libraries have been used to:
-	import kivy
-	import pyodbc
-	from kivy.app import App
-	from kivy.uix.button import Button
-	from kivy.uix.label import Label
-	from kivy.uix.gridlayout import GridLayout
-	from kivy.uix.textinput import TextInput
-	from kivy.uix.image import Image
-	from kivy.core.window import Window
-	import pyodbc as odbccon


"Brief Description of the Libraries used"
Kivy:
Kivy is a free and open-source Python framework for developing mobile apps and other multitouch application software with a natural user interface. Its further extensions are mentioned above and they are used to import app, buttons, label, grid layout (for the outlook of our application), text input (used for insering, deleting, updating, placing an order queries to enter data), image (to display images on our screen), and window (to manage the size, colour, spacing of our application). 

Pyodbc:
The pyodbc library provides Python developers with easy access to ODBC (Open Database Connectivity) databases. Therefore, you can implement the method given in this section to set up Python ODBC integrations with any platforms such as MS Access, MySQL, IBM Db2, etc.


"Main Functions"
Start_tab: 
It displays a button of Café Manager and on pressing that button it takes us to the function cust_admin_emp.
Cust_admin_emp: It displays 3 buttons of Customer, Admin, Employee. On pressing Customer button, we go to the customer1 function. On pressing the Admin Button, we go to the admin function and on pressing the employee function it takes us to employee1 function.

Customer1: 
It displays 4 buttons that are, Eatables, Drinks, Back, and Exit. On pressing the Eatables button, it displays the table of eatables present in the database. Similarly, on pressing the Drinks button, it displays the table of refreshments present in the database. The menu of eatables and drinks further have a button of place an order from where we can place an order and buy more. The back button takes us back to the cust_admin_emp function and exit button allows us to exit the programme.

Admin: 
It takes us to a login page for the admin and after logging in we go to a new function admin1. Admin1 has 4 buttons on Edit Eatables, Edit Drinks, Edit Employee, and Exit. On pressing Edit Eatables, we go to another function where the admin can display the menu of the Eatables, insert new eatables, delete, update, and search of eatables too. Similar case is for the Edit Drinks and Edit Employee button. 

Employee: 
It takes us to the login page for the employee and after logging in we go to another function employee1. Employee1 further has a form for the employee to fill which includes inserting Id, Name, Cellphone, Email, and Job. After submitting this, the information is inserted into the Employee table in the database and the admin can view this change in its module. 
