from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
from employee import employeeClass
from product import productClass
from category import categoryClass
from billing import BillClass
from summary import allSummary
# from locations import locationClass


class pharmacy:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1425x700+50+20")
        self.root.title("Hassan Pharmacy")

        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        # ===== Background Image =====
        self.bgFrame = Frame()
        self.bgFrame.place(relwidth=1, relheight=1)
        self.bg = Image.open("images/2.jpg")
        self.bg = self.bg.resize((1920, 1080), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(self.bg)
        self.bgImage = Label(self.bgFrame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ====== Title =======
        title = ctk.CTkLabel(self.root, text="Hassan Pharmacy", font=("Andalus", 70, "bold"), fg_color=("#33444b"), text_color="#fff").pack(side=TOP, fill=X)

        # ===== Menu Bar =====
        lbl_menu = Frame(bg="#29373F")
        lbl_menu.pack(side=TOP, fill=X, ipady=17)

        btnEmployee = ctk.CTkButton(lbl_menu, text="EMPLOYEE", command=self.employee,
                                     font=("Dungeon", 17, "bold"), fg_color="#29373F", hover_color="#09757f",
                                     cursor="hand2")
        btnEmployee.place(x=2, y=2, width=138, height=30)

        btn_category = ctk.CTkButton(lbl_menu, text="CATEGORY", command=self.category,
                                     font=("Dungeon", 17, "bold"), fg_color="#29373F", hover_color="#09757f",
                                     cursor="hand2")
        btn_category.place(x=115, y=2, width=138, height=30)

        # btn_location = ctk.CTkButton(lbl_menu, text="LOCATIONS", command=self.location, font=("Dungeon", 17, "bold"),
        #                              fg_color="#29373F", hover_color="#09757f", cursor="hand2")
        # btn_location.place(x=227, y=2, width=145, height=30)

        btn_product = ctk.CTkButton(lbl_menu, text="PRODUCT", command=self.product, font=("Dungeon", 17, "bold"),
                                    fg_color="#29373F", hover_color="#09757f", cursor="hand2")
        btn_product.place(x=227, y=2, width=125, height=30)

        btn_billing = ctk.CTkButton(lbl_menu, text="BILLING", command=self.billing, font=("Dungeon", 17, "bold"),
                                    fg_color="#29373F", hover_color="#09757f", cursor="hand2")
        btn_billing.place(x=330, y=2, width=110, height=30)

        btn_summary = ctk.CTkButton(lbl_menu, text="SUMMARY", command=self.summary, font=("Dungeon", 17, "bold"),
                                    fg_color="#29373F", hover_color="#09757f", cursor="hand2")
        btn_summary.place(x=420, y=2, width=140, height=30)

    def employee(self):
        self.emp_win = ctk.CTkToplevel(self.root)
        self.emp_obj = employeeClass(self.emp_win)

    def category(self):
        self.cat_win = ctk.CTkToplevel(self.root)
        self.cat_obj = categoryClass(self.cat_win)

    # def location(self):
    #     self.loc_win = ctk.CTkToplevel(self.root)
    #     self.loc_obj = locationClass(self.loc_win)

    def product(self):
        self.prod_win = ctk.CTkToplevel(self.root)
        self.prod_obj = productClass(self.prod_win)

    def billing(self):
        self.bill_win = ctk.CTkToplevel(self.root)
        self.bill_obj = BillClass(self.bill_win)

    def summary(self):
        self.summary_win = ctk.CTkToplevel(self.root)
        self.summary_obj = allSummary(self.summary_win)


if __name__ == "__main__":
    root = ctk.CTk()
    obj = pharmacy(root)
    root.mainloop()

# Software By Usman Amjad(UA)
