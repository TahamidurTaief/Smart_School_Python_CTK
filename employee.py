from doctest import master
from email.mime import image
import customtkinter
from tkinter import *
from PIL import ImageTk, Image  



class EmployeeClass(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1030}x{640}+{222}+{135}")
        customtkinter.set_appearance_mode("system")
        self.title("SMART SCHOOL Employee Management")










if __name__ == "__main__":
    SmartShop = EmployeeClass()
    SmartShop.mainloop()