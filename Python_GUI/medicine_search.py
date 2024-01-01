from tkinter import*
from PIL import Image,ImageTk 
from employee import classEmployee
import customtkinter as ctk
class IMS:
    def __init__(self, root):
        self.root=root #this is a type of a frame
        self.root.geometry("1920x1080+0+0")
        ctk.set_default_color_theme("Python_GUI\\themes\Sweetkind.json")
        self.root.title("Derma Medicals | Intelligent Inventory Management")
        self.root.config(bg="White")

        # Define title
        self.iconTitle=ctk.CTkImage(light_image=Image.open('Python_GUI\Images\Logo1.png'),
                                     size=(70,70))
        title=ctk.CTkLabel( self.root,text="Intelligent Inventory Management",
                            height=70, corner_radius=8, 
                            image=self.iconTitle,compound=LEFT, #set title image
                            font=("Calibri",40,"bold")
                            #text_color="orange", bg_color="papayawhip", #set title font and bg
                            #fg_color=("papayawhip")
                            ).place(relwidth=1)
        
        # Log out button
        buttonLogout=ctk.CTkButton(self.root, text = "Logout",
                          font=("Calibri",20,"bold"),
                          #fg_color="silver", text_color="black",
                          cursor="hand2" #changes cursor to hand
                          ).pack(side=TOP,anchor='e',padx=30,pady=15,ipadx=20, ipady=5)#place(x=1180,y=10,height=50,width=150)
        
        # Define clock        
        self.labelClock=ctk.CTkLabel(self.root,text="Welcome to Intelligent Inventory Management\t\t Date: DD-MM-YYYY \t\t Time: HH:mm:SS",
                    font=("Calibri",20),#fg_color="ghostwhite",text_color="Orange",
                    height=30) #set title font and bg
        self.labelClock.place(x=0, y=70, relwidth=1)    

        #Left Menu
        self.leftMenuIcon=ctk.CTkImage(light_image=Image.open("Python_GUI\Images\menu.png"),
                                       size=(20,20))
        #self.leftMenuIcon=self.leftMenuIcon.resize((200,100),Image.LANCZOS)
        #self.leftMenuIcon=ImageTk.PhotoImage(self.leftMenuIcon)

        leftMenu=ctk.CTkFrame(self.root,#fg_color="#8D6F3A",
                              border_width=2, #border_color="#FFCC70",
                              corner_radius=8,
                              width=200,height=565) 
        leftMenu.place( x=0.5, y=300)

        """labelMenuLogo=ctk.CTkLabel(leftMenu,image=self.leftMenuIcon)
        labelMenuLogo.pack(side=TOP,fill=X)"""

        buttonNewSale=ctk.CTkButton(master=leftMenu,text="New Sale")
        buttonNewSale.pack(anchor='w', expand=True, padx=30, pady=15 )
        


if __name__ == "__main__":
    root = ctk.CTk()
    obj=IMS(root)
    root.mainloop() #so that window stays openmain()