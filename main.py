from tkinter import*
from PIL import Image,ImageTk
from employee import EmployeeClass
from category import CategoryClass
from product import ProductClass
root=Tk()
root.title("inventory management")
root.geometry("1920x1080+0+0")
def employee():
    new_win=Toplevel(root)
    new_obj=EmployeeClass(new_win)
def category():
    new_win=Toplevel(root)
    new_obj=CategoryClass(new_win)
def product():
    new_win=Toplevel(root)
    new_obj=ProductClass(new_win)


title=Label(root,text="Inventory management system",font=("Impact",30),bg="white",fg="black",padx=20).place(x=0,y=0,relwidth=1)
Button(root,text='logout',font=("impact"),bg="#010c48").place(x=1300,y=10,height=30,width=100)
#____left menu
menu_logo=Image.open("inventory.png")
resize_image=menu_logo.resize((230,200))
menu_logo=ImageTk.PhotoImage(resize_image)

LeftMenu=Frame(root,bd=2,relief=RIDGE)
LeftMenu.place(x=0,y=50,width=250,height=665)
label_menu_logo=Label(LeftMenu,image=menu_logo)
label_menu_logo.pack(side=TOP,fill=X)
label_menu=Label(LeftMenu,text='Menu',font=("impact",20),bg="#009688").pack(side=TOP,fill=X)
employee_button=Button(LeftMenu,text='<< Employee',font=("impact",20),bg="white",bd=3,cursor="hand2",command=employee).pack(side=TOP,fill=X)
supplier_button=Button(LeftMenu,text='<< Supplier',font=("impact",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
category_button=Button(LeftMenu,text='<< Category',font=("impact",20),bg="white",command=category,bd=3,cursor="hand2").pack(side=TOP,fill=X)
sales_button=Button(LeftMenu,text='<< Sales',font=("impact",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
exit_button=Button(LeftMenu,text='<< Exit',font=("impact",20),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
product_button=Button(LeftMenu,text='<< Product',font=("impact",20),command=product,bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
label_footer=Label(root,text="Inventory management system",font=("Impact",30),bg="white",fg="black",padx=20).pack(side=BOTTOM,fill=X)
label_supplier=Label(root,text="Tota suppliers",font=("Impact",18),bg="black",fg="white",padx=20,bd=5,relief="ridge").place(x=300,y=200,width=300,height=150)
label_sales=Label(root,text="sales",font=("Impact",18),bg="black",fg="white",padx=20,bd=5,relief="ridge").place(x=800,y=200,width=300,height=150)
label_category=Label(root,text="total category",font=("Impact",18),bg="black",fg="white",padx=20,bd=5,relief="ridge").place(x=1200,y=200,width=300,height=150)
label_product=Label(root,text="total product",font=("Impact",18),bg="black",fg="white",padx=20,bd=5,relief="ridge").place(x=300,y=400,width=300,height=150)
label_employee=Label(root,text="Total employee",font=("Impact",18),bg="black",fg="white",padx=20,bd=5,relief="ridge").place(x=800,y=400,width=300,height=150)









root.mainloop()
