from doctest import master
from email.mime import image
import customtkinter
from tkinter import *
from PIL import ImageTk, Image
from setuptools import Command
import os

from student import studentClass  



class SmartShop(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1350}x{800}+{0}+{0}")
        customtkinter.set_appearance_mode("system")
        self.title("SMART SCHOOL Dashboard")
        self.dashboard()

#========================     Dashboard 2nd Frame     ======================

    def dashboard(self):
        dashboard_frame = customtkinter.CTkFrame(
                master=self,
                width = 1020,
                height=650,
                bg_color=("#EBEBEC", "#212325"),
                fg_color=("#d2dee3", "#191919"),
                corner_radius=20
        )
        dashboard_frame.place(x=220, y=110)

        dashboard_label = customtkinter.CTkLabel(
            master = self,
            text="DASHBOARD",
            text_color=("#191919", "white"),
            text_font=("Montserrat", 15),
        )
        dashboard_label.place(x=40, y=20)

        self.student_logo = ImageTk.PhotoImage(file="images/student_logo.png")
        student_logo = customtkinter.CTkLabel(
            master= self,
            image=self.student_logo,
            bg_color=("#EBEBEC", "#212325"),
            fg_color=("#EBEBEC", "#212325"),
            corner_radius=20,
        )
        student_logo.place(x=40, y=70)


        self.singOut_icon = ImageTk.PhotoImage(file="images/sing_out.png")
        singOut_icon = customtkinter.CTkButton(
            master=self,
            image=self.singOut_icon,
            hover_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            corner_radius=90,
            text="",
            fg_color=("#EBEBEC", "#212325"),
            width=20
        )
        singOut_icon.place(x=1200, y=20)


        self.setting_icon = ImageTk.PhotoImage(file="images/setting_icon.png")
        setting_icon = customtkinter.CTkButton(
            master=self,
            image=self.setting_icon,
            hover_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            corner_radius=90,
            text="",
            fg_color=("#EBEBEC", "#212325"),
            width=20
        )
        setting_icon.place(x=1140, y=20)



    #  ==================   Company name lable in dashboard

        smart_label = customtkinter.CTkLabel(
            master = self,
            text_font=("Montserrat", 25),
            text = "Smart",
            text_color=("#011c44", "#00d8ff"),
        )
        smart_label.place(x=530, y=25)

        school_label = customtkinter.CTkLabel(
            master = self,
            text_font=("Montserrat", 25),
            text = "School",
            text_color=("#e27c04", "#ffcc00"),
        )
        school_label.place(x=650, y=25)

        version_label = customtkinter.CTkLabel(
            master = self,
            text_font=("Montserrat", 10),
            text = "Version  1.00",
            text_color=("#011c44", "#00d8ff"),
        )
        version_label.place(x=1150, y=770)



# ==================    Dashboard Buttons    ================

        self.home_icon = ImageTk.PhotoImage(file="images/home_icon.png")
        home_btn = customtkinter.CTkButton(
            master=self, 
            text="HOME                          ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            image=self.home_icon,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            compound='right'
        )
        home_btn.place(x=0, y=210)

        self.student_icon = ImageTk.PhotoImage(file="images/student_icon.png")
        student_btn = customtkinter.CTkButton(
            master=self, 
            text="STUDENTS                 ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.student_icon,
            compound="right",
            command=self.student,
        )
        student_btn.place(x=0, y=250)


        self.employee_icon = ImageTk.PhotoImage(file="images/employee_icon.png")
        employee_btn = customtkinter.CTkButton(
            master=self, 
            text="EMPLOYEE                  ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.employee_icon,
            compound="right"
        )
        employee_btn.place(x=0, y=290)

        
        self.attendence_icon = ImageTk.PhotoImage(file="images/attendence_icon.png")
        attendence_btn = customtkinter.CTkButton(
            master=self, 
            text="ATTENDENCE            ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.attendence_icon,
            compound="right",
        )
        attendence_btn.place(x=0, y=330)

        
        self.class_icon = ImageTk.PhotoImage(file="images/class_icon.png")
        class_btn = customtkinter.CTkButton(
            master=self, 
            text="CLASS                           ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.class_icon,
            compound="right"
        )
        class_btn.place(x=0, y=370)


        self.section_icon = ImageTk.PhotoImage(file="images/section_icon.png")
        section_btn = customtkinter.CTkButton(
            master=self, 
            text="SECTION                       ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.section_icon,
            compound="right"
        )
        section_btn.place(x=0, y=410)


        self.routine_icon = ImageTk.PhotoImage(file="images/routine_icon.png")
        routine_btn = customtkinter.CTkButton(
            master=self, 
            text="ROUTINE                       ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.routine_icon,
            compound="right"
        )
        routine_btn.place(x=0, y=450)


        self.message_icon = ImageTk.PhotoImage(file="images/message_icon.png")
        message_btn = customtkinter.CTkButton(
            master=self, 
            text="MESSAGES                  ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.message_icon,
            compound="right"
        )
        message_btn.place(x=0, y=490)


        self.course_icon = ImageTk.PhotoImage(file="images/course_icon.png")
        course_btn = customtkinter.CTkButton(
            master=self, 
            text="COURSE                        ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.course_icon,
            compound="right"
        )
        course_btn.place(x=0, y=530)

        self.payment_icon = ImageTk.PhotoImage(file="images/payment_icon.png")
        payment_btn = customtkinter.CTkButton(
            master=self, 
            text="PAYMENT                    ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.payment_icon,
            compound="right"
        )
        payment_btn.place(x=0, y=570)

        
        self.result_icon = ImageTk.PhotoImage(file="images/result_icon.png")
        result_btn = customtkinter.CTkButton(
            master=self, 
            text="RESULTS                       ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.result_icon,
            compound="right"
        )
        result_btn.place(x=0, y=610)

        self.idcard_icon = ImageTk.PhotoImage(file="images/idcard_icon.png")
        idCard_btn = customtkinter.CTkButton(
            master=self, 
            text="ID CARD                       ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.idcard_icon,
            compound="right"
        )
        idCard_btn.place(x=0, y=650)

        self.reports_icon = ImageTk.PhotoImage(file="images/reports_icon.png")
        reports_btn = customtkinter.CTkButton(
            master=self, 
            text="REPORTS                     ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.reports_icon,
            compound="right"
        )
        reports_btn.place(x=0, y=690)

        self.settings_icon = ImageTk.PhotoImage(file="images/settings_icon.png")
        settings_btn = customtkinter.CTkButton(
            master=self, 
            text="SETTINGS                     ",
            text_font=("Montserrat",12),
            corner_radius=10,
            border_width=0,
            width=220,
            height=30,
            hover_color=("#73e7fc", "#005f82"),
            text_color=("black", "white"),
            fg_color=("#EBEBEC", "#212325"),
            cursor="hand2",
            image=self.settings_icon,
            compound="right"
        )
        settings_btn.place(x=0, y=730)






    def student(self):
        # self.new_win= Toplevel(self)
        # self.new_obj = studentClass(self.new_win)
        os.system('python student.py')






if __name__ == "__main__":
    SmartShop = SmartShop()
    SmartShop.mainloop()