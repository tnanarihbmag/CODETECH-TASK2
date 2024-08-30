from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox,END
import sqlite3
# root=Tk()
# root.title("inventory management")
# root.geometry("1920x1080+0+0")
# title=Label(root,text="Inventory management system",font=("Impact",30),bg="white",fg="black",padx=20).place(x=0,y=0,relwidth=1)




class EmployeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x800+220+130")
        self.root.title("inventory management system")
        self.root.config(bg='white')
        self.root.focus_force()
        #==============
        #all variables
        self.searchby=StringVar()
        self.searchtext = StringVar()
        self.var_empid=StringVar()
        self.var_name_= StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_password = StringVar()
        self.var_contact = StringVar()
        self.var_DOB= StringVar()
        self.var_utype= StringVar()
        self.var_DOJ=StringVar()
        self.var_salary=StringVar()
        self.var_address=StringVar()








        SearchFrame=LabelFrame(root,text="Search Employee",bg="white",fg="black",bd=2,relief="ridge")
        SearchFrame.place(x=250,y=20,width=600,height=70)

        combobox_search=ttk.Combobox(SearchFrame,values=("select","email","Empid","contact","name"),textvariable=self.searchby,state="readonly",justify="center")
        combobox_search.place(x=10,y=10,width=180)
        combobox_search.current(0)
        txt_search=Entry(SearchFrame,bg="lightyellow",fg="black",textvariable=self.searchtext).place(x=200,y=10,width=180)
        search=Button(SearchFrame,text="search", bg="green", fg="black",bd=5).place(x=400, y=10, width=100)
        #======title===
        employeedetails=Label(root,text="employee details",fg="black",bg="blue").place(x=50,y=100,width=1000)
        employeeid=Label(root,text="employee id",fg="black",bg="white").place(x=0,y=200)
        employeegender = Label(root, text="gender", fg="black",bg="white").place(x=340, y=200)
        employeecontact = Label(root, text="contact", fg="black",bg="white").place(x=600, y=200)

        employeeid = Entry(root, fg="black", bg="white",textvariable=self.var_empid).place(x=150, y=200,width=150)
        # employeegender = Entry(root, text="gender", fg="black", bg="white",textvariable=self.var_gender).place(x=400, y=200,width=150)

        combobox_gender= ttk.Combobox(root, values=("select", "male", "female", "other", ),
                                       textvariable=self.var_gender, state="readonly", justify="center")
        combobox_gender.place(x=400, y=200, width=180)
        combobox_gender.current(0)
        employeecontact = Entry(root, text="contact", fg="black", bg="white", textvariable=self.var_contact).place(
            x=700, y=200, width=150)

#  row 2
        employeename = Label(root, text="name", fg="black", bg="white").place(x=0, y=300)
        employeedob = Label(root, text="D.O.B", fg="black", bg="white").place(x=340, y=300)
        employeedoj = Label(root, text="D.O.J", fg="black", bg="white").place(x=600, y=300)

        name = Entry(root, textvariable=self.var_name_, fg="black", bg="yellow").place(x=150, y=300,width=150)
        dateofbirth = Entry(root, textvariable=self.var_DOB, fg="black", bg="yellow").place(x=400, y=300,width=150)
        dateofjoining = Entry(root, textvariable=self.var_DOJ, fg="black", bg="yellow").place(x=700, y=300,width=150)


#row3

        employeeemail = Label(root, text="email", fg="black", bg="white").place(x=0, y=350)
        employeepass = Label(root, text="pass", fg="black", bg="white").place(x=340, y=350)
        employeeutype = Label(root, text="U-type", fg="black", bg="white").place(x=600, y=350)

        email = Entry(root, textvariable=self.var_email, fg="black", bg="yellow").place(x=150, y=350, width=150)
        password = Entry(root, textvariable=self.var_password, fg="black", bg="yellow").place(x=400, y=350, width=150)
        combobox_utype = ttk.Combobox(root, values=("select", "admin", "employee"),
                                       textvariable=self.var_utype, state="readonly", justify="center")
        combobox_utype.place(x=700 ,y=350, width=180)
        combobox_utype.current(0)



        label_address = Label(root, text="address", fg="black", bg="white").place(x=0, y=400)
        label_salary = Label(root, text="salary", fg="black", bg="white").place(x=500, y=400)

        txt_address = Entry(root,  fg="black", bg="yellow",textvariable=self.var_address).place(x=150, y=400, width=250,height=100)
        txt_salary =  Entry(root,  fg="black", bg="yellow",textvariable=self.var_salary).place(x=600, y=400, width=150)

        # buttons

        button_add=Button(root,text="save",command=self.add, bg="green", fg="black",bd=5).place(x=600, y=450, width=50)
        button_add=Button(root,text="update", bg="green", fg="black",bd=5).place(x=650, y=450, width=50)
        button_add=Button(root,text="delete", bg="green", fg="black",bd=5).place(x=700, y=450, width=50)
        button_add=Button(root,text="clear", bg="green", fg="black",bd=5).place(x=760, y=450, width=50)

        #employee details
        emp_frame=Frame(self.root,bd=3,relief=RIDGE,bg="grey")
        emp_frame.place(x=0,y=600,relwidth=1,height=200)
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("emp_id","name","email","gender","contact","salary","address","pass","utype","dob","doj"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.heading("emp_id" ,text="empid")
        self.EmployeeTable.heading("name"   ,text= "name"  )
        self.EmployeeTable.heading("email"  ,text= "email" )
        self.EmployeeTable.heading("utype"  ,text="utype" )
        self.EmployeeTable.heading("contact",text="phnno")
        self.EmployeeTable.heading("salary", text="salary")
        self.EmployeeTable.heading("address",text="address")
        self.EmployeeTable.heading("gender" ,text="gender")
        self.EmployeeTable.heading("pass",text="pass")
        self.EmployeeTable.heading("dob" ,text="dob")
        self.EmployeeTable.heading("doj",text="doj")
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("emp_id",width=90)
        self.EmployeeTable.column("name" ,width=90)
        self.EmployeeTable.column("email" ,width=90)
        self.EmployeeTable.column("utype",width=90)
        self.EmployeeTable.column("contact",width=90 )
        self.EmployeeTable.column("salary", width=90)
        self.EmployeeTable.column("address",width=90)
        self.EmployeeTable.column("gender",width=90 )
        self.EmployeeTable.column("pass" ,width=90)
        self.EmployeeTable.column("dob",width=90 )
        self.EmployeeTable.column("doj",width=90 )
        # self.EmployeeTable["show"] = "column"
        # self.EmployeeTable.bind("<But     tonRelease-1>",self.get_data)

        self.show()
        # root.show()
    def add(self):
        con=sqlite3.connect(database=r"ims.db")
        cur=con.cursor()

        try:
            if self.var_empid.get()=="":
                messagebox.showerror("error","emplyee id must be required",parent=self.root)
            else:
                cur.execute("select * from employee where eid=?",(self.var_empid.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("error", "this employee id already registered",parent=self.root)
                else:
                    cur.execute("Insert into employee(eid,name,email,gender,contact,salary,address,pass,utype,dob,doj)values(?,?,?,?,?,?,?,?,?,?,?)",(
                    self.var_empid.get(),
                    self.var_name_.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_contact.get(),
                    self.var_salary.get(),
                    self.var_address.get(),
                    self.var_password.get(),
                    self.var_utype.get(),
                    self.var_DOB.get(),
                    self.var_DOJ.get(),

                    ))
                    con.commit()
                    messagebox.showinfo("success","emploee addedd",parent=self.root)

                    self.show()




        except Exception as ex:
            messagebox.showerror("error",f"error due to: {str(ex)}")

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            print(rows)
            for row in rows:
                self.EmployeeTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"error due to :{str(ex)}",parent=self.root)

    # def get_data(self,ev):
    #     f=self.EmployeeTable.focus()
    #     content=(self.EmployeeTable.item(f))
    #     row=content['values']
    #     print(row)

root=Tk()
obj1=EmployeeClass(root)
root.mainloop()
