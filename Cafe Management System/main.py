import kivy
import pyodbc
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.core.window import Window
import pyodbc as odbccon

conn = odbccon.connect("Driver={SQL Server Native Client 11.0};"
                       "Server=AMNA;"
                       "Database=Cafe;"
                       "Trusted_Connection=yes;")

class grid_layout(GridLayout):

    def __init__(self, **kwargs):
        # base class constructor
        super().__init__(**kwargs)
        self.start_tab()
        return

    # Cafe Manager Page
    def start_tab(self):
        self.clear_widgets()
        self.cols = 1

        self.size_hint = (0.6, 0.7)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/cup.jpg")
        self.add_widget(self.img)
        self.menu = Button(text="Cafe Manager", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.menu.bind(on_press=self.cust_admin_emp)
        self.add_widget(self.menu)
        return self.menu

    # Customer Admin Employee Choice.
    def cust_admin_emp(self, instance):
        self.clear_widgets()
        self.cols = 1
        Window.clearcolor = (0, 0, 0, 0)
        self.size_hint = (0.9, 0.9)
        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/home1.jpg")
        self.add_widget(self.img)
        self.cust = Button(text="Customer", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.cust.bind(on_press=self.customer)
        self.add_widget(self.cust)
        self.ad = Button(text="Admin", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.ad.bind(on_press=self.admin)
        self.add_widget(self.ad)
        self.emp = Button(text="Employee", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.emp.bind(on_press=self.employee)
        self.add_widget(self.emp)
        return

    # Customer Event
    def customer(self, instance):
        return self.customer1(instance)

    # Admin Event.
    def admin(self, instance):
        self.clear_widgets()

        self.cols = 1
        self.size_hint=(0.6,0.7)
        self.pos_hint={"center_x":.5,"center_y":.5}
        self.img=Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/p2.png")
        self.add_widget(self.img)

        lab = Label(text="Password", color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(lab)

        self.password = TextInput(multiline=False, hint_text="Enter Password", password=True)
        self.add_widget(self.password)

        self.enter = Button(text="Enter", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.enter)
        self.enter.bind(on_press=self.pass1)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.cust_admin_emp)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

        return GridLayout()

    #Empoyee Event.
    def employee(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.6, 0.7)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/p2.png")
        self.add_widget(self.img)

        lab = Label(text="Password", color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(lab)

        self.password = TextInput(multiline=False, hint_text="Enter Password", password=True,)
        self.add_widget(self.password)

        self.enter = Button(text="Enter", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.enter)
        self.enter.bind(on_press=self.pass1)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.cust_admin_emp)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    #Password.
    def pass1(self, instance):
        admin = "admin123"
        employee = "employee123"
        if str(self.password.text) == admin:
            self.admin1(instance)

        elif str(self.password.text) == employee:
            self.employee2(instance)
        else:
            self.clear_widgets()
            self.cols = 1
            self.size_hint = (0.6, 0.7)
            self.pos_hint = {"center_x": .5, "center_y": .5}

            self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/p2.png")
            self.add_widget(self.img)

            lab = Label(text="Password", color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
            self.add_widget(lab)
            self.password = TextInput(multiline=False, hint_text="Wrong Password", password=True)
            self.add_widget(self.password)

            self.enter = Button(text="Enter", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
            self.add_widget(self.enter)

            self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
            self.back.bind(on_press=self.cust_admin_emp)
            self.add_widget(self.back)

            self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
            self.exit.bind(on_press=self.press4)
            self.add_widget(self.exit)

            self.enter.bind(on_press=self.pass1)
        return

    #Employee Details.
    def employee2(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)

        self.lab1 = Label(text="Employee ID ", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.lab2 = Label(text="Employee Name ", font_size=20,bold="True")
        self.name = TextInput(multiline=False)

        self.lab3 = Label(text="Employee Cell Phone ", font_size=20,bold="True")
        self.cp = TextInput(multiline=False)

        self.lab4 = Label(text="Employee Email ", font_size=20,bold="True")
        self.email= TextInput(multiline=False)

        self.lab5 = Label(text="Employee Job ", font_size=20,bold="True")
        self.job = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.add_widget(self.lab2)
        self.add_widget(self.name)

        self.add_widget(self.lab3)
        self.add_widget(self.cp)

        self.add_widget(self.lab4)
        self.add_widget(self.email)

        self.add_widget(self.lab5)
        self.add_widget(self.job)

        self.bottom_layout=GridLayout()
        self.bottom_layout.cols=3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.employee1)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.cust_admin_emp)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)

        self.add_widget(self.bottom_layout)


    # Admin.
    def admin1(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/edit.png")
        self.add_widget(self.img)

        self.eatables = Button(text="Edit Eatables", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.eatables.bind(on_press=self.p1)
        self.add_widget(self.eatables)

        self.drinks = Button(text="Edit Drinks", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.drinks.bind(on_press=self.p2)
        self.add_widget(self.drinks)

        self.employee = Button(text="Edit Employee", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.employee.bind(on_press=self.p3)
        self.add_widget(self.employee)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)


    #Employee Insert Query.
    def employee1(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)

        cursor = conn.cursor()

        query = ('''insert into Employee (Employee_ID, Employee_Name ,Cell_phone,Email, Job) values (?,?,?,?,?)''')
        val = (self.id.text, self.name.text, self.cp.text, self.email.text, self.job.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Entered Succesfully!", font_size=30,
                         font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1),
                           color=(1, 1, 1, 1), font_size=20,
                           font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.cust_admin_emp)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1),
                           color=(1, 1, 1, 1), font_size=20,
                           font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Edit Eatables.
    def p1(self,instance):
        self.clear_widgets()
        self.cols=1
        self.size_hint = (0.9, 0.9)
        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/pic5.jpg")
        self.add_widget(self.img)
        self.spacing=1
        self.eatable_menu= Button(text="Menu", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.eatable_menu.bind(on_press=self.p11)
        self.add_widget(self.eatable_menu)

        self.eatable_insert = Button(text="Insert", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.eatable_insert.bind(on_press=self.p12)
        self.add_widget(self.eatable_insert)

        self.eatable_delete = Button(text="Delete", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.eatable_delete.bind(on_press=self.p13)
        self.add_widget(self.eatable_delete)

        self.eatable_update = Button(text="Update", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.eatable_update.bind(on_press=self.p14)
        self.add_widget(self.eatable_update)

        self.eatable_search = Button(text="Search", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.eatable_search.bind(on_press=self.p15)
        self.add_widget(self.eatable_search)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.admin1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Edit Drinks.
    def p2(self,instance):
        self.clear_widgets()
        self.cols=1
        self.size_hint = (0.9, 0.9)
        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/pic2.jpg")
        self.add_widget(self.img)
        self.drinks_menu= Button(text="Menu", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.drinks_menu)
        self.drinks_menu.bind(on_press=self.p21)

        self.drinks_insert = Button(text="Insert", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.drinks_insert.bind(on_press=self.p22)
        self.add_widget(self.drinks_insert)

        self.drink_delete = Button(text="Delete", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.drink_delete.bind(on_press=self.p23)
        self.add_widget(self.drink_delete)

        self.drink_update = Button(text="Update", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.drink_update.bind(on_press=self.p24)
        self.add_widget(self.drink_update)

        self.drink_search = Button(text="Search", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.drink_search.bind(on_press=self.p25)
        self.add_widget(self.drink_search)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.admin1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Edit Employee.
    def p3(self,instance):
        self.clear_widgets()
        self.cols=1
        self.size_hint = (0.9, 0.9)
        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/pic6.png")
        self.add_widget(self.img)
        self.employee_list= Button(text="Employees", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.employee_list)
        self.employee_list.bind(on_press=self.p31)

        self.employee_insert = Button(text="Add a New Employee", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.employee_insert.bind(on_press=self.p32)
        self.add_widget(self.employee_insert)

        self.employee_delete = Button(text="Delete an Employee", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.employee_delete.bind(on_press=self.p33)
        self.add_widget(self.employee_delete)

        self.employee_update = Button(text="Update an Employee", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.employee_update.bind(on_press=self.p34)
        self.add_widget(self.employee_update)

        self.employee_search=Button(text="Search an Employee", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.employee_search.bind(on_press=self.p35)
        self.add_widget(self.employee_search)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.admin1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatable Menu Display.
    def p11(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.spacing = 1
        self.size_hint = (1, 1)
        cursor = conn.cursor()
        cursor.execute('Select * from Eatables')
        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)

        self.l1 = Label(text="FOOD", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2 = Label(text="PRICE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.l1)
        self.add_widget(self.l2)

        for i in range(0, n):
            # Window.clearcolor=(0, 0.5, 0.5, 1)
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.lab2 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab1)
            self.add_widget(self.lab2)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatables Admin Insert.
    def p12(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)

        self.lab1 = Label(text="Food", font_size=30,bold="True")
        self.food = TextInput(multiline=False)

        self.lab2 = Label(text="Price", font_size=30,bold="True")
        self.price = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.food)

        self.add_widget(self.lab2)
        self.add_widget(self.price)

        self.bottom_layout=GridLayout()
        self.bottom_layout.cols=3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p122)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    def p122(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        cursor = conn.cursor()

        query = ('''insert into Eatables (Food, Prices) values (?,?)''')
        val = (self.food.text, self.price.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Entered Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatable Delete Event.
    def p13(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/delete.png")
        self.add_widget(self.img)

        self.lab1 = Label(text="Eatable Name", font_size=20,bold="True")
        self.food = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.food)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p133)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def p133(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1

        self.size_hint = (0.9, 0.9)

        cursor = conn.cursor()

        query = ('''delete from Eatables where Food= (?)''')
        val = (self.food.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Deleted Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatable Update Event.
    def p14(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/update.jpg")
        self.add_widget(self.img)

        self.update_eatable = Button(text="Eatable", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_eatable.bind(on_press=self.p141)
        self.add_widget(self.update_eatable)

        self.update_price = Button(text="Price", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_price.bind(on_press=self.p142)
        self.add_widget(self.update_price)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatable Name Update Event.
    def p141(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)

        self.lab1 = Label(text="Updated Eatable Name", font_size=20,bold="True")
        self.eatable1 = TextInput(multiline=False)

        self.lab2 = Label(text="Name that needs to be Updated", font_size=20,bold="True")
        self.eatable2 = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.eatable1)

        self.add_widget(self.lab2)
        self.add_widget(self.eatable2)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p1411)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p14)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)

        self.add_widget(self.bottom_layout)

    # Eatable Price Update Event.
    def p142(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.lab1 = Label(text="Name of the Eatable", font_size=20,bold="True")
        self.eatable = TextInput(multiline=False)


        self.lab2 = Label(text="Updated Price", font_size=20,bold="True")
        self.price = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.eatable)

        self.add_widget(self.lab2)
        self.add_widget(self.price)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p1422)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p14)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)

        self.add_widget(self.bottom_layout)

    # Eatable Name Update Event.
    def p1411(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        cursor = conn.cursor()

        query = (''' update Eatables set Food = (?) where Food = (?) ''')
        val = (self.eatable1.text, self.eatable2.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatable Price Update Event.
    def p1422(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        cursor = conn.cursor()

        query = ('''update Eatables set Prices = (?) where Food = (?)''')
        val = (self.price.text, self.eatable.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatable Search Event.
    def p15(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/search.webp")
        self.add_widget(self.img)

        self.lab1 = Label(text="Eatable Name", font_size=20,bold="True")
        self.food = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.food)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p151)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def p151(self, instance):
        self.clear_widgets()
        self.cols = 2
        self.spacing = 1
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        cursor = conn.cursor()

        query = (''' select * from Eatables where Food = (?) ''')
        val = (self.food.text)
        cursor.execute(query, val)

        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)

        self.l1 = Label(text="FOOD", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2 = Label(text="PRICE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.l1)
        self.add_widget(self.l2)

        for i in range(0, n):
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab1)
            self.lab2 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab2)

        conn.commit()

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Drinks Menu Display.
    def p21(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.spacing = 1
        self.size_hint = (1, 1)
        cursor = conn.cursor()
        cursor.execute('Select * from Refreshments')
        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)

        self.l1 = Label(text="BEVERAGE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                        color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2 = Label(text="PRICE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                        color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.l1)
        self.add_widget(self.l2)

        for i in range(0, n):
            # Window.clearcolor=(0, 0.5, 0.5, 1)
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.lab2 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab1)
            self.add_widget(self.lab2)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def p22(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)

        self.lab1 = Label(text="Drink ", font_size=30,bold="True")
        self.drink = TextInput(multiline=False)

        self.lab2 = Label(text="Price", font_size=30,bold="True")
        self.price = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.drink)

        self.add_widget(self.lab2)
        self.add_widget(self.price)

        self.bottom_layout=GridLayout()
        self.bottom_layout.cols=3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p222)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    def p222(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        cursor = conn.cursor()

        query = ('''insert into Refreshments (Drinks, Prices) values (?,?)''')
        val = (self.drink.text, self.price.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Entered Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Drinks Delete Event.
    def p23(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/delete.png")
        self.add_widget(self.img)

        self.lab1 = Label(text="Drink Name", font_size=20,bold="True")
        self.drinks = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.drinks)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p233)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def p233(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = ('''delete from Refreshments where Drinks= (?)''')
        val = (self.drinks.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Deleted Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Drink Update Event.
    def p24(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/update.jpg")
        self.add_widget(self.img)

        self.update_drink = Button(text="Drink",  background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1),font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_drink.bind(on_press=self.p241)
        self.add_widget(self.update_drink)

        self.update_price = Button(text="Price", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_price.bind(on_press=self.p242)
        self.add_widget(self.update_price)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Drink Name Update Event.
    def p241(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)

        self.lab1 = Label(text="Updated Drink Name", font_size=20,bold="True")
        self.drink1 = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.drink1)

        self.lab2 = Label(text="Name that needs to be Updated", font_size=20,bold="True")
        self.drink2 = TextInput(multiline=False)

        self.add_widget(self.lab2)
        self.add_widget(self.drink2)

        self.bottom_layout=GridLayout()
        self.bottom_layout.cols=3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p2411)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p24)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    # Drink Price Update Event.
    def p242(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)

        self.lab1 = Label(text="Name of the Drink", font_size=20,bold="True")
        self.drink = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.drink)

        self.lab2 = Label(text="Updated Price", font_size=20,bold="True")
        self.price = TextInput(multiline=False)

        self.add_widget(self.lab2)
        self.add_widget(self.price)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p2422)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p24)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    # Drink Name Update Event.
    def p2411(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        cursor = conn.cursor()

        query=(''' update Refreshments set Drinks = (?) where Drinks = (?) ''')
        val=(self.drink1.text,self.drink2.text)
        cursor.execute(query,val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Drink Price Update Event.
    def p2422(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)

        cursor = conn.cursor()

        query = ('''update Refreshments set Prices = (?) where Drinks = (?)''')
        val = (self.price.text, self.drink.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Drink Search Event.
    def p25(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9,0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/search.webp")
        self.add_widget(self.img)

        self.lab1 = Label(text="Drink Name", font_size=20,bold="True")
        self.drink= TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.drink)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p251)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def p251(self, instance):
        self.clear_widgets()
        self.cols = 2
        self.spacing = 1
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = (''' select * from Refreshments where Drinks = (?) ''')
        val = (self.drink.text)
        cursor.execute(query, val)

        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)

        self.l1 = Label(text="BEVERAGE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2 = Label(text="PRICE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.l1)
        self.add_widget(self.l2)

        for i in range(0, n):
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab1)
            self.lab2 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab2)
        conn.commit()

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p2)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee List Display.
    def p31(self,instance):
        self.clear_widgets()
        self.cols = 5
        self.size_hint = (1, 1)
        cursor = conn.cursor()
        cursor.execute('Select * from Employee')
        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arr5 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
            arr3.append(row[2])
            arr4.append(row[3])
            arr5.append(row[4])

        n = len(arr1)

        self.l1=Label(text="ID",font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2=Label(text="NAME",font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l3=Label(text="CELL PHONE",font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l4=Label(text="EMAIL",font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l5=Label(text="JOB",font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))

        self.add_widget(self.l1)
        self.add_widget(self.l2)
        self.add_widget(self.l3)
        self.add_widget(self.l4)
        self.add_widget(self.l5)

        for i in range(0, n):
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20, pos=(0, 0), halign="left", valign="middle")
            self.lab2 = Label(text=f'{arr2[i]}', color=(1, 1, 1, 1), font_size=20, pos=(0, 0), halign="left", valign="middle")
            self.lab3 = Label(text=f'{arr3[i]}', color=(1, 1, 1, 1), font_size=20, pos=(0, 0), halign="left", valign="middle")
            self.lab4 = Label(text=f'{arr4[i]}', color=(1, 1, 1, 1), font_size=20, pos=(0, 0), halign="left", valign="middle")
            self.lab5 = Label(text=f'{arr5[i]}', color=(1, 1, 1, 1), font_size=20, pos=(0, 0), halign="left", valign="middle")

            self.add_widget(self.lab1)
            self.add_widget(self.lab2)
            self.add_widget(self.lab3)
            self.add_widget(self.lab4)
            self.add_widget(self.lab5)

        self.ex1 = Label(text=f'{""}', color=(1, 1, 1, 1), font_size=20)
        self.add_widget(self.ex1)


        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.ex2 = Label(text=f'{""}', color=(1, 1, 1, 1), font_size=20)
        self.add_widget(self.ex2)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

        self.ex3 = Label(text=f'{""}', color=(1, 1, 1, 1), font_size=20)
        self.add_widget(self.ex3)

    #Employee Insert.
    def p32(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)

        self.lab1 = Label(text="Employee ID", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.lab2 = Label(text="Employee Name", font_size=20,bold="True")
        self.name = TextInput(multiline=False)

        self.lab3 = Label(text="Employee Cell Phone", font_size=20,bold="True")
        self.cp = TextInput(multiline=False)

        self.lab4 = Label(text="Employee Email", font_size=20,bold="True")
        self.email= TextInput(multiline=False)

        self.lab5 = Label(text="Employee Job", font_size=20,bold="True")
        self.job = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.add_widget(self.lab2)
        self.add_widget(self.name)

        self.add_widget(self.lab3)
        self.add_widget(self.cp)

        self.add_widget(self.lab4)
        self.add_widget(self.email)

        self.add_widget(self.lab5)
        self.add_widget(self.job)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p322)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)

        self.add_widget(self.bottom_layout)

    def p322(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        cursor = conn.cursor()

        query = ('''insert into Employee (Employee_ID, Employee_Name ,Cell_phone,Email, Job) values (?,?,?,?,?)''')
        val = (self.id.text, self.name.text, self.cp.text, self.email.text, self.job.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Entered Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    #Employee Delete.
    def p33(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/delete.png")
        self.add_widget(self.img)

        self.lab1 = Label(text="Employee ID", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p333)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def p333(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = ('''delete from Employee where Employee_ID= (?)''')
        val = (self.id.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Deleted Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee Update Event.
    def p34(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/update.jpg")
        self.add_widget(self.img)

        self.update_ID = Button(text="Employee ID", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_ID.bind(on_press=self.p341)
        self.add_widget(self.update_ID)

        self.update_name = Button(text="Employee Name", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_name.bind(on_press=self.p342)
        self.add_widget(self.update_name)

        self.update_cell = Button(text="Employee Cellphone", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_cell.bind(on_press=self.p343)
        self.add_widget(self.update_cell)

        self.update_email = Button(text="Employee Email", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_email.bind(on_press=self.p344)
        self.add_widget(self.update_email)

        self.update_job = Button(text="Employee Job", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.update_job.bind(on_press=self.p345)
        self.add_widget(self.update_job)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee ID Update Event.
    def p341(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.lab1 = Label(text="Old ID", font_size=20,bold="True")
        self.id1 = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id1)

        self.lab2 = Label(text="Updated ID", font_size=20,bold="True")
        self.id2 = TextInput(multiline=False)

        self.add_widget(self.lab2)
        self.add_widget(self.id2)

        self.bottom_layout=GridLayout()
        self.bottom_layout.cols=3
        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p3411)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p34)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    # Employee Name Update Event.
    def p342(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.lab1 = Label(text="Employee ID", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.lab2 = Label(text="Updated Employee Name", font_size=20,bold="True")
        self.name = TextInput(multiline=False)

        self.add_widget(self.lab2)
        self.add_widget(self.name)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3
        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p3422)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p34)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    # Employee Cellphone Update Event.
    def p343(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.lab1 = Label(text="Employee ID", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.lab2 = Label(text="Updated Employee Cellphone", font_size=20,bold="True")
        self.cellphone = TextInput(multiline=False)

        self.add_widget(self.lab2)
        self.add_widget(self.cellphone)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3
        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p3433)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p34)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    # Employee Email Update Event.
    def p344(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.lab1 = Label(text="Employee ID", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.lab2 = Label(text="Updated Employee Email", font_size=20,bold="True")
        self.email = TextInput(multiline=False)

        self.add_widget(self.lab2)
        self.add_widget(self.email)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3
        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p3444)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p34)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    # Employee Job Update Event.
    def p345(self,instance):
        self.clear_widgets()
        self.cols = 2
        self.size_hint = (1, 1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.lab1 = Label(text="Employee ID", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.lab2 = Label(text="Updated Employee Job", font_size=20,bold="True")
        self.job = TextInput(multiline=False)

        self.add_widget(self.lab2)
        self.add_widget(self.job)

        self.bottom_layout = GridLayout()
        self.bottom_layout.cols = 3
        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p3455)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p34)
        self.bottom_layout.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.bottom_layout.add_widget(self.exit)
        self.add_widget(self.bottom_layout)

    # Employee ID Update Event.
    def p3411(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = (''' update Employee set Employee_ID = (?) where Employee_ID = (?) ''')
        val = (self.id2.text, self.id1.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee Name Update Event.
    def p3422(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = (''' update Employee set Employee_Name = (?) where Employee_ID = (?) ''')
        val = (self.name.text, self.id.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee Cellphone Update Event.
    def p3433(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = (''' update Employee set Cell_phone = (?) where Employee_ID = (?) ''')
        val = (self.cellphone.text, self.id.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee Email Update Event.
    def p3444(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 2
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = (''' update Employee set Email = (?) where Employee_ID = (?) ''')
        val = (self.email.text, self.id.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee Job Update Event.
    def p3455(self, instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = (''' update Employee set Job = (?) where Employee_ID = (?) ''')
        val = (self.job.text, self.id.text)
        cursor.execute(query, val)
        conn.commit()

        self.lab = Label(text="Data Updated Succesfully!", font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add_widget(self.lab)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Employee Search Event.
    def p35(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/search.webp")
        self.add_widget(self.img)

        self.lab1 = Label(text="Employee ID", font_size=20,bold="True")
        self.id = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.id)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.p351)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def p351(self,instance):
        self.clear_widgets()
        self.cols = 5
        self.spacing = 1
        self.size_hint = (1,1)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        cursor = conn.cursor()

        query = (''' select * from Employee where Employee_ID = (?) ''')
        val = (self.id.text)
        cursor.execute(query, val)

        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        arr5 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
            arr3.append(row[2])
            arr4.append(row[3])
            arr5.append(row[4])
        n = len(arr1)

        self.l1 = Label(text="ID", font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2 = Label(text="NAME", font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l3 = Label(text="CELL PHONE", font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l4 = Label(text="EMAIL", font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l5 = Label(text="JOB", font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))

        self.add_widget(self.l1)
        self.add_widget(self.l2)
        self.add_widget(self.l3)
        self.add_widget(self.l4)
        self.add_widget(self.l5)

        for i in range(0, n):
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab1)
            self.lab2 = Label(text=f'{arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab2)
            self.lab3 = Label(text=f'{arr3[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab3)
            self.lab4 = Label(text=f'{arr4[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab4)
            self.lab5 = Label(text=f'{arr5[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.lab5)
        conn.commit()

        self.ex1 = Label(text=f'{""}', color=(1, 1, 1, 1), font_size=20)
        self.add_widget(self.ex1)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.p3)
        self.add_widget(self.back)

        self.ex2 = Label(text=f'{""}', color=(1, 1, 1, 1), font_size=20)
        self.add_widget(self.ex2)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

        self.ex3 = Label(text=f'{""}', color=(1, 1, 1, 1), font_size=20)
        self.add_widget(self.ex3)

    # Customer Event.
    def customer1(self, instance):
        self.clear_widgets()
        self.cols = 1

        self.size_hint = (0.9, 0.9)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/eat.jpg")
        self.add_widget(self.img)

        self.eatables = Button(text="Eatables Menu", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.eatables.bind(on_press=self.press1)
        self.add_widget(self.eatables)

        self.drinks = Button(text="Drinks Menu", background_color=(500/255.0, 150/255.0, 199/255.0, 1), color=(1, 1, 1, 1), font_size=30,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.drinks.bind(on_press=self.press2)
        self.add_widget(self.drinks)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.cust_admin_emp)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Eatables Event.
    def press1(self, instance):
        self.clear_widgets()

        self.cols = 3
        self.spacing = 1
        self.size_hint = (1, 1)

        cursor = conn.cursor()
        cursor.execute('Select * from Eatables')
        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)
        self.l0 = Label(text="Sr no.", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l1 = Label(text="FOOD", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2 = Label(text="PRICE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.l0)
        self.add_widget(self.l1)
        self.add_widget(self.l2)

        for i in range(0, n):
            self.lab0 = Label(text=f'{i}', color=(1, 1, 1, 1), font_size=20)
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.lab2 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)

            self.add_widget(self.lab0)
            self.add_widget(self.lab1)
            self.add_widget(self.lab2)

        self.order = Button(text="Place an order", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.order.bind(on_press=self.ord0)
        self.add_widget(self.order)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.customer1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Drinks Event.
    def press2(self, instance):
        self.clear_widgets()
        self.cols = 3
        self.spacing = 1
        self.size_hint = (1, 1)
        cursor = conn.cursor()
        cursor.execute('Select * from Refreshments')
        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)

        self.l0 = Label(text="Sr no.", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                        color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l1 = Label(text="BEVERAGE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                        color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.l2 = Label(text="PRICE", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                        color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.l0)
        self.add_widget(self.l1)
        self.add_widget(self.l2)

        for i in range(0, n):
            self.lab0 = Label(text=f'{i}', color=(1, 1, 1, 1), font_size=20)
            self.lab1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.lab2 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)

            self.add_widget(self.lab0)
            self.add_widget(self.lab1)
            self.add_widget(self.lab2)

        self.order = Button(text="Place an order", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1),
                            color=(1, 1, 1, 1), font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.order.bind(on_press=self.ord2)
        self.add_widget(self.order)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.customer1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1), font_size=20,font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    # Order Placed.

    def ord0(self, instance):
        self.clear_widgets()
        self.cols=1
        self.size_hint = (0.6, 0.7)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/reciept.jpg")
        self.add_widget(self.img)

        self.lab1 = Label(text="Enter Item Name", font_size=20, bold="True")
        self.t1 = TextInput(multiline=False)

        self.lab2 = Label(text="Enter Quantity", font_size=20, bold="True")
        self.t2 = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.t1)
        self.add_widget(self.lab2)
        self.add_widget(self.t2)

        self.ex=Label(text="")
        self.add_widget(self.ex)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1),
                             color=(1, 1, 1, 1), font_size=20,
                             font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.ord1)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.customer1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)


    def ord1(self,instance):
        self.clear_widgets()
        self.cols = 4
        self.spacing = 1
        self.size_hint = (0.6, 0.6)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        cursor = conn.cursor()

        query = (''' select * from Eatables where Food = (?) ''')
        val = (self.t1.text)
        cursor.execute(query, val)

        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)

        self.label1 = Label(text="Item Name", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.label2 = Label(text="Qty", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.label3 = Label(text="Price", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.label4 = Label(text="Total Price", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.label3)
        self.add_widget(self.label4)

        self.qty=self.t2.text

        for i in range(0, n):
            self.l1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l1)
            self.l2 = Label(text=f'{self.qty}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l2)
            self.l3 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l3)
            self.l4 = Label(text=f'{"Rs. "}{int(self.t2.text)*arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l4)

        conn.commit()

        self.ex1 = Label(text="")
        self.add_widget(self.ex1)

        self.add = Button(text="Buy More ", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add.bind(on_press=self.press1)
        self.add_widget(self.add)

        self.back = Button(text="Check Out", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.checkout)
        self.add_widget(self.back)

    def ord2(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.size_hint = (0.6, 0.7)
        self.pos_hint = {"center_x": .5, "center_y": .5}

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/reciept.jpg")
        self.add_widget(self.img)

        self.lab1 = Label(text="Enter Item Name", font_size=20, bold="True")
        self.t1 = TextInput(multiline=False)

        self.lab2 = Label(text="Enter Quantity", font_size=20, bold="True")
        self.t2 = TextInput(multiline=False)

        self.add_widget(self.lab1)
        self.add_widget(self.t1)
        self.add_widget(self.lab2)
        self.add_widget(self.t2)

        self.ex = Label(text="")
        self.add_widget(self.ex)

        self.submit = Button(text="Submit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1),
                             color=(1, 1, 1, 1), font_size=20,
                             font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.submit.bind(on_press=self.ord3)
        self.add_widget(self.submit)

        self.back = Button(text="Back", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.customer1)
        self.add_widget(self.back)

        self.exit = Button(text="Exit", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)

    def ord3(self,instance):
        self.clear_widgets()
        self.cols = 4
        self.spacing = 1
        self.size_hint = (0.6, 0.6)
        self.pos_hint = {"center_x": .5, "center_y": .5}
        cursor = conn.cursor()

        query = (''' select * from Refreshments where Drinks = (?) ''')
        val = (self.t1.text)
        cursor.execute(query, val)

        arr1 = []
        arr2 = []
        for row in cursor:
            arr1.append(row[0])
            arr2.append(row[1])
        n = len(arr1)

        self.label1 = Label(text="Item Name", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                            color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.label2 = Label(text="Qty", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                            color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.label3 = Label(text="Price", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                            color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.label4 = Label(text="Total Price", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf',
                            color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1))
        self.add_widget(self.label1)
        self.add_widget(self.label2)
        self.add_widget(self.label3)
        self.add_widget(self.label4)

        self.qty = self.t2.text

        for i in range(0, n):
            self.l1 = Label(text=f'{arr1[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l1)
            self.l2 = Label(text=f'{self.qty}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l2)
            self.l3 = Label(text=f'{"Rs. "}{arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l3)
            self.l4 = Label(text=f'{"Rs. "}{int(self.t2.text) * arr2[i]}', color=(1, 1, 1, 1), font_size=20)
            self.add_widget(self.l4)

        conn.commit()

        self.ex1 = Label(text="")
        self.add_widget(self.ex1)

        self.add = Button(text="Buy More ", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1),
                          color=(1, 1, 1, 1),
                          font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.add.bind(on_press=self.press2)
        self.add_widget(self.add)

        self.back = Button(text="Check Out", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1),
                           color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.back.bind(on_press=self.checkout)
        self.add_widget(self.back)

    def checkout(self,instance):
        self.clear_widgets()
        self.cols = 1
        self.spacing = 1

        self.img = Image(source="C:/Users/Amna/OneDrive/Pictures/Saved Pictures/hands.jpg")
        self.add_widget(self.img)

        self.spacing = 1
        self.size_hint = (0.6, 0.6)

        self.label1 = Label(text="We hope you enjoyed your meal!", font_size=30, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf', color=(1, 1, 1, 1))
        self.add_widget(self.label1)

        self.exit = Button(text="GoodBye :)", background_color=(147 / 255.0, 146 / 255.0, 185 / 255.0, 1), color=(1, 1, 1, 1),
                           font_size=20, font_name='C:/Users/Amna/Downloads/pacifico/Pacifico.ttf')
        self.exit.bind(on_press=self.press4)
        self.add_widget(self.exit)
    # Back Event.
    def press3(self, instance):
        return self.cust_admin_emp(instance)

    # Exit Event.
    def press4(self, instance):
        return exit()

class Cafe_Manager(App):
    def build(self):
        return grid_layout()

if __name__ == '__main__':
    Cafe_Manager().run()