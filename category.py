
from tkinter import*
from PIL import  Image,ImageTk
from tkinter import ttk,messagebox,END
import sqlite3
class CategoryClass:
    def __init__(self,root):
    # self.root=root
        self.root=root
        self.root.geometry("1200x800+220+130")
        self.root.title("inventory management system")
        self.root.config(bg="white")
        self.root.focus_force()

        self.catid=StringVar()
        self.name=StringVar()


        label_title=Label(self.root,text="Manage product category",font=(30),bg="#184a45",fg="white").pack(side=TOP,fill=X,padx=2,pady=20)
        label_name=Label(self.root,text="Enter category name",font=("",40),fg="black",bg="white").place(x=50,y=100)
        enter_name=Entry(self.root,font=("", 20),textvariable=self.name, fg="black", bg="light yellow").place(x=50, y=200)

        button_add = Button(self.root,text="ADD", command=self.add,font=("", 20), fg="black", bg="green").place(x=50, y=250,width=100)

        button_delete = Button(self.root, text="delete", font=("", 20),command=self.delete, fg="black", bg="green").place(x=170, y=250, width=100)

        cat_frame = Frame(self.root, bd=3, relief=RIDGE,bg="lightgrey")
        cat_frame.place(x=380, y=200, width=450, height=350)
        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.categorytable = ttk.Treeview(cat_frame, columns=("cid", "name"), show="headings",
        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.categorytable.xview)
        scrolly.config(command=self.categorytable.yview)

        self.categorytable.heading("cid", text='Cid')
        self.categorytable.heading("name", text='Name')

        self.categorytable["show"] = "headings"
        self.categorytable.pack(fill=BOTH, expand=1)
        self.categorytable.column("cid",width=90)
        self.categorytable.column("name", width=90)
        self.categorytable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    import sqlite3
    from tkinter import messagebox

    def add(self):
        con = sqlite3.connect(database=r"ims.db")
        cur = con.cursor()

        try:
            if self.name.get() == "":
                messagebox.showerror("Error", "Category name is required", parent=self.root)
                return  # Exit if the name is empty

            # Check if the category name already exists
            cur.execute("SELECT * FROM category WHERE name=?", (self.name.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "This name is already registered", parent=self.root)
            else:
                # Insert the new category into the database
                cur.execute("INSERT INTO category (name) VALUES (?)", (self.name.get(),))
                con.commit()  # Commit the transaction to save changes
                messagebox.showinfo("Success", "Category added", parent=self.root)
                self.show()  # Update the view to reflect the new data


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()  # Ensure the connection is closed


    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            self.categorytable.delete(*self.categorytable.get_children())
            print(rows)
            for row in rows:
                self.categorytable.insert('', END, values=row)
                print(rows)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()  # Ensure the connection is closed

    def get_data(self,ev):
        f=self.categorytable.focus()
        content=(self.categorytable.item(f))
        row=content['values']
        self.catid.set(row[0])
        self.name.set(row[1])


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.catid.get()=="":
                messagebox.showerror("Error","please select or enter category name from the list",parent=self.root)
            else:
                cur.execute("Select * from category where cid=?",(self.catid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("error","please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("confirm","do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from category where cid=?",(self.catid.get(),))
                        con.commit()
                        messagebox.showinfo("delete","category deleted successfully",parent=self.root)
                        self.show()
                        self.name.set("")
                        self.catid.set('')
        except Exception as ex:
            messagebox.showerror("error",f"error due to:{str(ex)}",parent=self.root)










root=Tk()
obj1=CategoryClass(root)
root.mainloop()
