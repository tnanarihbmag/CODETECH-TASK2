from tkinter import*
from PIL import  Image,ImageTk
from tkinter import ttk,messagebox,END
import sqlite3
class ProductClass:
    def __init__(self,root):
    # self.root=root
        self.root=root
        self.root.geometry("1200x800+220+130")
        self.root.title("inventory management system")
        self.root.config(bg="white")
        self.root.focus_force()
        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.var_qty=StringVar()
        self.status=StringVar()
        self.var_name=StringVar()
        self.price=StringVar()
        self.searchby = StringVar()
        self.searchtext = StringVar()
        self.var_pid=StringVar()

        self.cat_list=[]

        self.fetch_data()



        product_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_frame.place(x=10,y=10,height=450,width=450)
        # col 1
        title=Label(product_frame,text="product details",fg="black",bg="blue",font=("",20)).pack(side=TOP,fill=X)
        lbl_category=Label(product_frame,text="category",fg="black",bg="yellow",font=("",20)).place(x=30,y=60)

        lbl_supplier = Label(product_frame, text="supplier", fg="black", bg="yellow", font=("", 20)).place(x=30,
                                                                                                              y=100)

        lbl_name = Label(product_frame, text="name", fg="black", bg="yellow", font=("", 20)).place(x=30,y=150)

        lbl_price= Label(product_frame, text="price", fg="black", bg="yellow", font=("", 20)).place(x=30, y=190)

        lbl_price = Label(product_frame, text="quantity", fg="black", bg="yellow", font=("", 20)).place(x=30, y=250)

        lbl_quantity = Label(product_frame, text="status", fg="black", bg="yellow", font=("", 20)).place(x=30, y=320)

    #col2
        combobox_cat = ttk.Combobox(product_frame, values=self.cat_list,
                                       textvariable=self.var_cat, state="readonly", justify="center")
        combobox_cat.place(x=130, y=60, width=180)
        combobox_cat.current(0)

        txt_supplier = Entry(product_frame, textvariable=self.var_sup).place(x=130, y=100, width=180)




        txt_name = Entry(product_frame,textvariable=self.var_name).place(x=130, y=150, width=180)

        txt_price = Entry(product_frame, textvariable=self.price).place(x=130, y=190, width=180)

        txt_qty = Entry(product_frame, textvariable=self.var_qty).place(x=130, y=250, width=180)


        txt_status = Entry(product_frame, textvariable=self.status).place(x=130, y=320, width=180)



        button_add = Button(product_frame, text="save", bg="green", fg="black", bd=5,command=self.add).place(x=0, y=350, width=50,height=40)
        button_update = Button(product_frame, text="update", bg="green", fg="black", bd=5).place(x=60, y=350, width=50,height=40)
        button_delete = Button(product_frame, text="delete", bg="green", fg="black", bd=5,command=self.delete).place(x=130, y=350, width=50,height=40)
        button_clear = Button(product_frame, text="clear", bg="green", fg="black", bd=5,command=self.clear).place(x=190, y=350, width=50,height=40)

        search_frame=LabelFrame(self.root,text="search employee",font=("",12),background="white",foreground="black")
        search_frame.place(x=480,y=10,width=600,height=130)

        combobox_search = ttk.Combobox(search_frame, values=("select","category","supplier","name"),
                                     state="readonly", justify="center",textvariable=self.searchby)
        combobox_search.place(x=10, y=10, width=180)
        combobox_search.current(0)
        txt_search = Entry(search_frame,textvariable=self.searchtext)
        txt_search.place(x=200,y=10,width="180")

        txt_searchbutton =  Button(search_frame, text="search",command=self.search).place(x=350,y=10,width="100")
    #treeveiw------------------
        product_frame = Frame(self.root, bd=3, relief=RIDGE, bg="grey")
        product_frame.place(x=480, y=100, width=700, height=400)
        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)
        self.product_table = ttk.Treeview(product_frame, columns=(
        "pid", "category", "supplier", "price", "quantity", "status","name"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)


        self.product_table.heading("pid", text="pid")

        self.product_table.heading("category", text="supplier")
        self.product_table.heading("supplier", text="category")
        self.product_table.heading("price", text="name")
        self.product_table.heading("quantity", text="price")

        self.product_table.heading("name", text="status")

        self.product_table.heading("status", text="qyt")

        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("category",width=90   )
        self.product_table.column("supplier",width=90  )
        self.product_table.column("price"   ,width=90 )
        self.product_table.column("quantity",width=90  )
        self.product_table.column("status"  ,width=90 )

        self.product_table.column("name"    ,width=90  )

        self.product_table.pack(fill=BOTH, expand=1)

        # self.product_table["show"] = "column"
        self.product_table.bind("<ButtonRelease-1>",self.get_data)

        self.show()






    #     functions



    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            if  self.var_cat.get()=="empty":
                messagebox.showerror("Error", "all field is is required", parent=self.root)
                return  # Exit if the name is empty

            # Check if the category name already exists
            cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "This name is already registered", parent=self.root)
            else:
                # Insert the new category into the database
                cur.execute("INSERT INTO product (category,supplier,price,quantity,status,name) VALUES (?,?,?,?,?,?)", (

                self.var_cat  .get(),
                self.var_sup .get(),
                self.price.get(),
                self.var_qty .get(),
                self.status.get(),
                self.var_name.get()
                ))
                con.commit()  # Commit the transaction to save changes
                messagebox.showinfo("Success", "Product added", parent=self.root)
                self.show()  # Update the view to reflect the new data


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()  # Ensure the connection is closed


    def fetch_data(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat = cur.fetchall()
            self.cat_list.append("empty")
            print(cat)

            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("select")

                for i in cat:
                    self.cat_list.append(i[0])



        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

        finally:
            con.close()



    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            print(rows)
            for row in rows:
                self.product_table.insert('', END, values=row)
                print(rows)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()  # Ensure the connection is closed

    def get_data(self,ev):
        f=self.product_table.focus()
        content=(self.product_table.item(f))
        row=content['values']
        self.var_pid.set(row[0])
        self.var_cat.set(row[2])
        self.var_sup.set(row[1])
        self.price.set(row[3])
        self.var_qty.set(row[4])
        self.status.set(row[5])
        self.var_name.set(row[6])


    # def update(self):




    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","please select product name from the list",parent=self.root)
            else:
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("delete","product deleted successfully",parent=self.root)
                        self.clear()


        except Exception as ex:
            messagebox.showerror("error",f"error due to:{str(ex)}",parent=self.root)

    def clear(self):
        self.var_cat.set("select")
        self.var_sup.set("select")
        self.price.set("select")
        self.var_qty.set("select")
        self.status.set("select")
        self.var_name.set("select")
        self.show()

    import sqlite3
    from tkinter import messagebox, END

    def search(self):
        con = sqlite3.connect('ims.db')
        cur = con.cursor()

        try:
            search_by = self.searchby.get()
            search_text = self.searchtext.get()

            if search_by == "select":
                messagebox.showerror("Error", "Search criteria should be selected", parent=self.root)
                return

            if search_text == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
                return

            query = f"SELECT * FROM product WHERE {search_by} LIKE ?"
            cur.execute(query, ('%' + search_text + '%',))
            rows = cur.fetchall()

            if len(rows) != 0:
                self.product_table.delete(*self.product_table.get_children())
                for row in rows:
                    self.product_table.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

            # self.show()  # Make sure this function is defined elsewhere

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()







root=Tk()
obj1=ProductClass(root)
root.mainloop()
