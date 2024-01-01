from tkinter import*
from PIL import Image,ImageTk 
from employee import classEmployee
import customtkinter as ctk
class IMS:
    def __init__(self, root):
        self.root=root #this is a type of a frame
        self.root.geometry("1920x1080+0+0")
        self.root.title("Derma Medicals | Intelligent Inventory Management")
        self.root.config(bg="White")

        # Define title
        self.icon_title=PhotoImage(file='Python_GUI\Images\Logo1.png')
        title=Label(self.root,text="Intelligent Inventory Management",
                    image=self.icon_title,compound=LEFT, #set title image
                    font=("Calibri",40,"bold"),bg="papayawhip",fg="Gold", #set title font and bg
                    ).place(x=0, y=0, relwidth=1,height=70)
        
        # Log out button
        buttonLogout=Button(self.root, text = "Logout",
                          font=("Calibri",15,"bold"),bg="silver",
                          cursor="hand2" #changes cursor to hand
                          ).pack(side=TOP,anchor='ne',padx=30,pady=10,ipadx=20, ipady=5)#place(x=1180,y=10,height=50,width=150)
        
        # Define clock        
        self.labelClock=Label(self.root,text="Welcome to Intelligent Inventory Management\t\t Date: DD-MM-YYYY \t\t Time: HH:mm:SS",
                    font=("Calibri",15),bg="ghostwhite",fg="Orange") #set title font and bg
        self.labelClock.place(x=0, y=70, relwidth=1,height=30)        

        #Left Menu
        self.leftMenuIcon=Image.open("Python_GUI\Images\menu.png")
        self.leftMenuIcon=self.leftMenuIcon.resize((200,100),Image.LANCZOS)
        self.leftMenuIcon=ImageTk.PhotoImage(self.leftMenuIcon)

        leftMenu=Frame(self.root,bd=2,relief=RIDGE,bg="ghostwhite")
        leftMenu.place(x=0,y=302,width=200,height=565)

        labelMenuLogo=Label(leftMenu,image=self.leftMenuIcon)
        labelMenuLogo.pack(side=TOP,fill=X)

        # Menu buttons
        labelMenu=Label(leftMenu, text = "Menu",
                          font=("Calibri",20,"bold"),bg="papayawhip",fg="Gold"                          
                          ).pack(side=TOP,fill=X)
              
        buttonEmployee=Button(leftMenu, text = "Employee",
                          font=("Calibri",20,"bold"),
                          bg="ghostwhite",fg="Gold",bd=3,padx=5,
                          cursor="hand2",
                          command=self.employee
                          ).pack(side=TOP,fill=X)
        buttonSupplier=Button(leftMenu, text = "Supplier",
                          font=("Calibri",20,"bold"),
                          bg="ghostwhite",fg="Gold",bd=3,padx=5,
                          cursor="hand2"
                          ).pack(side=TOP,fill=X) 
        buttonCategory=Button(leftMenu, text = "Category",
                          font=("Calibri",20,"bold"),
                          bg="ghostwhite",fg="Gold",bd=3,padx=5,
                          cursor="hand2"
                          ).pack(side=TOP,fill=X) 
        buttonProduct=Button(leftMenu, text = "Product",
                          font=("Calibri",20,"bold"),
                          bg="ghostwhite",fg="Gold",bd=3,padx=5,
                          cursor="hand2"
                          ).pack(side=TOP,fill=X) 
        buttonSales=Button(leftMenu, text = "Sales",
                          font=("Calibri",20,"bold"),
                          bg="ghostwhite",fg="Gold",bd=3,padx=5,
                          cursor="hand2"
                          ).pack(side=TOP,fill=X) 
        buttonExit=Button(leftMenu, text = "Exit",
                          font=("Calibri",20,"bold"),
                          bg="ghostwhite",fg="Gold",bd=3,padx=5,
                          cursor="hand2"
                          ).pack(side=TOP,fill=X)                  

        #Footer
        labelFooter=Label(self.root,text="Welcome to Intelligent Inventory Management\t\t\t\t Date: DD-MM-YYYY Time: HH:mm:SS",
                    font=("Calibri",15),bg="ghostwhite",fg="Orange").pack(side=BOTTOM,fill=X)
        #self.labelClock.pack(x=0, y=70, relwidth=1,height=30)

        #Main Body
        self.labelEmployee=Label(self.root,text="Employee\n [ 0 ]",bd=5,relief=RIDGE,
                                 bg="blue",fg="white", font=("goudy old style", 30, "bold"))
        self.labelEmployee.place(x=300, y= 200, height=200, width=300)

        self.labelSupplier=Label(self.root,text="Supplier\n [ 0 ]",bd=5,relief=RIDGE,
                                 bg="blue",fg="white", font=("goudy old style", 30, "bold"))
        self.labelSupplier.place(x=700, y= 200, height=200, width=300)

        self.labelCategory=Label(self.root,text="Category\n [ 0 ]",bd=5,relief=RIDGE,
                                 bg="blue",fg="white", font=("goudy old style", 30, "bold"))
        self.labelCategory.place(x=1100, y= 200, height=200, width=300)

        self.labelProduct=Label(self.root,text="Product\n [ 0 ]",bd=5,relief=RIDGE,
                                 bg="blue",fg="white", font=("goudy old style", 30, "bold"))
        self.labelProduct.place(x=450, y= 500, height=200, width=300)

        self.labelSales=Label(self.root,text="Sales\n [ 0 ]",bd=5,relief=RIDGE,
                                 bg="blue",fg="white", font=("goudy old style", 30, "bold"))
        self.labelSales.place(x=850, y= 500, height=200, width=300)

#++++++++++++++++++++++++++++++#
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=classEmployee(self.new_win) 



if __name__ == "__main__":
    root = ctk.CTk()
    obj=IMS(root)
    root.mainloop() #so that window stays openmain()
