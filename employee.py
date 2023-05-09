# -------Importing Modules
from tkinter import *
import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3
from PIL import Image
from datetime import datetime


class employeeClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1250x600+200+148")
        self.root.title("UA")
        self.root.focus_force()
        self.root.resizable(False, False)

        # ============ All variables ===========
        self.var_searchby = StringVar(value="Select")
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar(value="Select")
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()  # Date of Birth
        self.var_doj = StringVar()  # Date of joining
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()  # User Type
        self.var_salary = StringVar()

        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        # ===== Style =====
        style = ttk.Style(self.root)

        # ====== Title =======
        self.title = ctk.CTkLabel(self.root, text="Return Products", font=("Brush Script MT", 50, "bold"))
        self.title.pack(side=TOP, fill=X)

        # ====== Search Frame ======
        self.SearchFrame = ctk.CTkFrame(self.root)
        self.SearchFrame.place(x=390, y=70, width=570, height=70)

        # ====== Options ======
        cmb_search = ctk.CTkComboBox(self.SearchFrame, variable=self.var_searchby,
                                  values=("Select", "Email", "Name", "Contact"), justify=CENTER,
                                  font=("goudy old style", 20))
        cmb_search.place(x=10, y=12, width=180)

        self.txtSearch = ctk.CTkEntry(self.SearchFrame, textvariable=self.var_searchtxt, font=("goudy old style", 20))
        self.txtSearch.place(x=170, y=12, height=40)

        btn_search = ctk.CTkButton(self.SearchFrame, text="Search", command=self.search, font=("goudy old style", 20),
                                   cursor="hand2").place(x=320, y=12, width=150, height=40)

        # ====== Title ======
        title = ctk.CTkLabel(self.root, text="Employee Details", font=("Brush Script MT", 35, 'bold'), fg_color="#2463aa")
        title.pack(pady=70, fill=X)

        self.lblEmpId = ctk.CTkLabel(self.root, text="Emp Id", font=("goudy old style", 25))
        self.lblEmpId.place(x=90, y=200)

        self.lblGender = ctk.CTkLabel(self.root, text="Gender", font=("goudy old style", 25))
        self.lblGender.place(x=420, y=200)

        self.lblContact = ctk.CTkLabel(self.root, text="Contact", font=("goudy old style", 25))
        self.lblContact.place(x=780, y=200)

        self.txtEmpId = ctk.CTkEntry(self.root, textvariable=self.var_emp_id, font=("goudy old style", 25))
        self.txtEmpId.place(x=210, y=200, width=180, height=40)

        cmb_gender = ctk.CTkComboBox(self.root, variable=self.var_gender,
                                  values=("Select", "Male", "Female", "Other"), justify=CENTER,
                                  font=("goudy old style", 15))
        cmb_gender.place(x=550, y=200, width=180, height=40)

        self.txtContact = ctk.CTkEntry(self.root, textvariable=self.var_contact, font=("goudy old style", 25))
        self.txtContact.place(x=900, y=200, width=180, height=40)

        # ====== Row 2 ======
        self.lblName = ctk.CTkLabel(self.root, text="Name", font=("goudy old style", 25))
        self.lblName.place(x=90, y=240)

        self.lblDob = ctk.CTkLabel(self.root, text="D.O.B", font=("goudy old style", 25))
        self.lblDob.place(x=420, y=240)

        self.lblDoj = ctk.CTkLabel(self.root, text="D.O.J", font=("goudy old style", 25))
        self.lblDoj.place(x=780, y=240)

        self.txtName = ctk.CTkEntry(self.root, textvariable=self.var_name, font=("goudy old style", 25))
        self.txtName.place(x=210, y=240, width=180, height=40)

        self.txtDob = ctk.CTkEntry(self.root, textvariable=self.var_dob, font=("goudy old style", 25))
        self.txtDob.place(x=550, y=240, width=180, height=40)

        self.txtDoj = ctk.CTkEntry(self.root, textvariable=self.var_doj, font=("goudy old style", 25))
        self.txtDoj.place(x=900, y=240, width=180, height=40)

        # ====== Row 3 ======
        self.lblEmail = ctk.CTkLabel(self.root, text="Email", font=("goudy old style", 25))
        self.lblEmail.place(x=90, y=280)

        self.lblPass = ctk.CTkLabel(self.root, text="Password", font=("goudy old style", 25))
        self.lblPass.place(x=420, y=280)

        self.lblUtype = ctk.CTkLabel(self.root, text="User Type", font=("goudy old style", 25))
        self.lblUtype.place(x=780, y=280)

        self.txtEmail = ctk.CTkEntry(self.root, textvariable=self.var_email, font=("goudy old style", 25))
        self.txtEmail.place(x=210, y=280, width=180)

        self.txtPass = ctk.CTkEntry(self.root, textvariable=self.var_pass, font=("goudy old style", 25))
        self.txtPass.place(x=550, y=280, width=180)

        cmb_utype = ctk.CTkComboBox(self.root, variable=self.var_utype,
                                 values=("Admin", "Employee"), justify=CENTER,
                                 font=("goudy old style", 25))
        cmb_utype.place(x=900, y=280, width=180)

        # ====== Row 4 ======
        self.lblAddress = ctk.CTkLabel(self.root, text="Address", font=("goudy old style", 25))
        self.lblAddress.place(x=90, y=330)

        self.lblSalary = ctk.CTkLabel(self.root, text="Salary", font=("goudy old style", 25))
        self.lblSalary.place(x=470, y=330)

        self.txtAddress = ctk.CTkTextbox(self.root, font=("goudy old style", 25))
        self.txtAddress.place(x=210, y=330, width=300, height=60)

        self.txtSalary = ctk.CTkEntry(self.root, textvariable=self.var_salary, font=("goudy old style", 25))
        self.txtSalary.place(x=550, y=330, width=180)

        # ====== Buttons ======
        btnFrame = ctk.CTkFrame(self.root)
        btnFrame.place(x=700, y=320, width=570, height=70)

        self.addIcon = ctk.CTkImage(light_image=Image.open("images/add.png"), size=(32, 32))
        self.btn_add = ctk.CTkButton(btnFrame, text="Add", image=self.addIcon, font=("Agency FB", 20),
                                     cursor="hand2", compound=LEFT, width=80, height=25, border_width=0,
                                     corner_radius=8)
        self.btn_add.place(x=10, y=5, width=130, height=50)
        self.btn_add.bind("<Return>", self.add)
        self.btn_add.bind("<ButtonRelease-1>", self.add)

        self.updateIcon = ctk.CTkImage(light_image=Image.open("images/update.png"), size=(32, 32))
        self.btn_update = ctk.CTkButton(btnFrame, text="Update", image=self.updateIcon,
                                        font=("Agency FB", 20),
                                        cursor="hand2", compound=LEFT, width=80, height=25, border_width=0,
                                        corner_radius=8)
        self.btn_update.place(x=120, y=5, width=130, height=50)
        self.btn_update.bind("<Return>", self.update)
        self.btn_update.bind("<ButtonRelease-1>", self.update)

        self.deleteIcon = ctk.CTkImage(light_image=Image.open("images/delete.png"), size=(32, 32))
        self.btn_delete = ctk.CTkButton(btnFrame, text="Delete", image=self.deleteIcon,
                                        font=("Agency FB", 20),
                                        cursor="hand2", compound=LEFT, width=80, height=25, border_width=0,
                                        corner_radius=8)
        self.btn_delete.place(x=230, y=5, width=130, height=50)
        self.btn_delete.bind("<Return>", self.delete)
        self.btn_delete.bind("<ButtonRelease-1>", self.delete)

        self.clearIcon = ctk.CTkImage(light_image=Image.open("images/clear.png"), size=(32, 32))
        self.btn_clear = ctk.CTkButton(btnFrame, text="Clear All", image=self.clearIcon,
                                       font=("Agency FB", 20),
                                       cursor="hand2", compound=LEFT, width=80, height=25, border_width=0,
                                       corner_radius=8)
        self.btn_clear.place(x=340, y=5, width=130, height=50)
        self.btn_clear.bind("<Return>", self.clear)
        self.btn_clear.bind("<ButtonRelease-1>", self.clear)

        # ====== Employee Details ======
        emp_frame = ctk.CTkFrame(self.root)
        emp_frame.place(x=0, y=400, relwidth=1, height=250)

        style.configure("Treeview", background="#333333", foreground="white", fieldbackground="#333333", rowheight=30,
                        font=("Arial", 18))
        style.map("Treeview", background=[("selected", "#0078D7")])
        style.configure("Treeview.Heading", font=('Constantia', 18))
        style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders

        self.EmployeeTable = ttk.Treeview(emp_frame, style='Treeview', columns=(
            "eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"))

        for column in self.EmployeeTable["columns"]:
            self.EmployeeTable.column(column, anchor=CENTER)

        scrolly = ctk.CTkScrollbar(emp_frame, orientation=VERTICAL, command=self.EmployeeTable.yview)
        scrolly.pack(side=RIGHT, fill=Y)
        self.EmployeeTable.configure(yscrollcommand=scrolly.set)

        scrollx = ctk.CTkScrollbar(emp_frame, orientation=HORIZONTAL, command=self.EmployeeTable.xview)
        scrollx.pack(side=BOTTOM, fill=X)
        self.EmployeeTable.configure(xscrollcommand=scrollx.set)

        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B")
        self.EmployeeTable.heading("doj", text="D.O.J")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")

        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=60, minwidth=60)
        self.EmployeeTable.column("name", width=140, minwidth=140)
        self.EmployeeTable.column("email", width=200, minwidth=200)
        self.EmployeeTable.column("gender", width=140, minwidth=140)
        self.EmployeeTable.column("contact", width=140, minwidth=140)
        self.EmployeeTable.column("dob", width=140, minwidth=140)
        self.EmployeeTable.column("doj", width=140, minwidth=140)
        self.EmployeeTable.column("pass", width=140, minwidth=140)
        self.EmployeeTable.column("utype", width=140, minwidth=140)
        self.EmployeeTable.column("address", width=140, minwidth=140)
        self.EmployeeTable.column("salary", width=140, minwidth=140)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def add(self, e):
        con = sqlite3.connect(database=r'hpd.db')
        cur = con.cursor()
        try:
            self.addDate = datetime.now().strftime("%m/%d/%Y")
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try different", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO employee (eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",
                        (
                            self.var_emp_id.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txtAddress.get('1.0', END),
                            self.var_salary.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()

                cur.execute("SELECT expDesc FROM shopExpenses WHERE expDesc=?", ("Salary",))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This name is not in the list of shop expenses page", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO shopExpenses (expDesc, expPrice, expDate) values(?,?,?)",
                        (
                            self.var_name.get(),
                            self.var_salary.get(),
                            self.addDate
                        ))
                    con.commit()
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'hpd.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for row in rows:
                self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def get_data(self, ev):
        try:
            f = self.EmployeeTable.focus()
            content = (self.EmployeeTable.item(f))
            row = content['values']
            self.var_emp_id.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_contact.set(row[4])
            self.var_dob.set(row[5])
            self.var_doj.set(row[6])
            self.var_pass.set(row[7])
            self.var_utype.set(row[8])
            self.txtAddress.delete('1.0', END),
            self.txtAddress.insert(END, row[9]),
            self.var_salary.set(row[10])
        except (Exception,):
            pass

    def update(self, e):
        con = sqlite3.connect(database=r'hpd.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? WHERE eid=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_gender.get(),
                            self.var_contact.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                            self.txtAddress.get('1.0', END),
                            self.var_salary.get(),
                            self.var_emp_id.get()
                        ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def delete(self, e):
        con = sqlite3.connect(database=r'hpd.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error", "Employee Id Must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Invalid Employee ID", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op == True:
                        cur.execute("DELETE FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear(e)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self, e):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txtAddress.delete('1.0', END)
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")

        self.show()

    def search(self):
        con = sqlite3.connect(database=r'hpd.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select Search By Option", parent=self.root)
            elif self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Select input should be required", parent=self.root)
            else:
                cur.execute(
                    "SELECT * FROM employee WHERE " + self.var_searchby.get() + " LIKE '%" + self.var_searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for row in rows:
                        self.EmployeeTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = ctk.CTk()
    obj = employeeClass(root)
    root.mainloop()
