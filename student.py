from doctest import master
from email.mime import image
import customtkinter
from tkinter import *
from PIL import ImageTk, Image  



class studentClass(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1030}x{640}+{222}+{135}")
        customtkinter.set_appearance_mode("system")
        self.title("SMART SCHOOL Student Management")


        self.title_lbl = customtkinter.CTkLabel(
            master = self,
            text = "SMART SCHOOL Student Management",
            text_color=("black", "white"),
            text_font= ("Montserrat", 10),

        )
        self.title_lbl.place(x=10, y=20)







if __name__ == "__main__":
    SmartShop = studentClass()
    SmartShop.mainloop()