from customtkinter import *
import tkinter
from PIL import Image
from database import loadDatabase
from CTkScrollableDropdown import *
import pandas as pd
from CTkTable import CTkTable
from time import strftime
 

medicineDf = loadDatabase()
medSuggestionList = medicineDf['Name'].tolist()

class clientWindow:
    def __init__(self, master):
        self.master = master
        master.title("Medicine Quantity Checker")

        # Sidebar Frame
        self.sidebar_frame = SidebarFrame(master)
        self.sidebar_frame.pack_propagate(0)
        self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        # Main View Frame
        self.main_view = ClientMainViewFrame(master)
        self.main_view.pack_propagate(0)
        self.main_view.pack(side="left")

class SidebarFrame(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
        self.pack_propagate(0)

        # Logo
        self.logoLabel = CTkLabel(master=self, text="", image=self.logoImg)
        self.logoLabel.pack(pady=(38, 0), anchor="center")

        # Buttons
        self.opButton = self.create_button("OP Register", "plus_icon.png")
        #self.ordersButton = self.create_button("Orders", "package_icon.png")
        self.ordersListButton = self.create_button("Orders", "list_icon.png")
        self.returnsButton = self.create_button("Returns", "returns_icon.png")
        self.settingsButton = self.create_button("Settings", "settings_icon.png")
        self.accountButton = self.create_button("Account", "person_icon.png", pady=(160, 0))

    def create_button(self, text, image_filename, pady=(16, 0)):
        img_data = Image.open(f"Python_GUI\\ctk\\{image_filename}")
        img = CTkImage(dark_image=img_data, light_image=img_data)
        return CTkButton(master=self, image=img, text=text, fg_color="transparent", font=("Arial Bold", 14),
                         hover_color="#207244", anchor="w").pack(anchor="center", ipady=5, pady=pady)

    @property
    def logoImg(self):
        return CTkImage(dark_image=Image.open("Python_GUI\\ctk\\logo.png"),
                        light_image=Image.open("Python_GUI\\ctk\\logo.png"), size=(77.68, 85.42))

class ClientMainViewFrame(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, fg_color="#fff", width=680, height=650, corner_radius=0)
        self.pack_propagate(0)



        def addToTable():
            
            global currentClientName
            global currentClientPhone
            self.warningLabel.configure(text = "")
            currentClientName = self.clientNameEntry.get()
            currentClientPhone = self.clientPhoneEntry.get()
            currentOPProc = self.clientOPCbox.get()

            numRows=self.opTable.rows                            
            print(currentClientName, currentClientPhone )  

            if len(currentClientName)==0:
                self.warningLabel.configure(text = "Warning: Invalid Name")
            
            elif len (currentClientPhone) != 10:
                self.warningLabel.configure(text = "Warning: Phone number needs 10 digits")

            else:
                self.opTable.add_row(index=numRows, values=[currentClientName, currentClientPhone, self.clientGenderCbox.get(), self.clientAgeEntry.get(), self.clientOPCbox.get(), self.clientAmountEntry.get()])

            
        
        # New Sale Section
        self.titleLabel = CTkLabel(master=self, text="New Bill", font=("Arial Black", 25), text_color="#2A8C55")
        self.titleLabel.pack(anchor="w", pady=(29, 0), padx=27)


        self.timeLabel = CTkLabel(master=self, font=("Arial Black", 17), text_color="#2A8C55" )
        self.timeLabel.pack(anchor="e", pady=(0, 0), padx=27)
        def get_time():
            string = strftime('%H:%M:%S %p')
            self.timeLabel.configure(text=string)
            self.timeLabel.after(1000, get_time)
        get_time()
        # Client Section
        self.clientGrid = CTkFrame(master=self, fg_color="transparent")
        self.clientGrid.pack(fill="both", padx=27, pady=(31, 0))
        
        self.clientNameLabel = CTkLabel(master=self.clientGrid, text="Patient Name", 
                                        font=("Arial Bold", 17), text_color="#52A476", 
                                        justify="left")
        self.clientNameLabel.grid(row=0, column=0, sticky="w") 
        self.clientNameEntry = CTkEntry(master=self.clientGrid, 
                                        fg_color="#F0F0F0", border_width=0, 
                                        width=285, height=40)
        self.clientNameEntry.grid(row=1, column=0, sticky='w', padx = (0,30))
        
        
        self.clientPhoneLabel = CTkLabel(master=self.clientGrid, 
                                      text="Phone No:", font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left")
        self.clientPhoneLabel.grid(row=0, column=1, sticky="w") 
        self.clientPhoneEntry = CTkEntry(master=self.clientGrid, 
                                         fg_color="#F0F0F0", 
                                         border_width=0, width=285, height=40)
        self.clientPhoneEntry.grid(row=1, column=1, sticky='w')                          


        self.clientdetGrid = CTkFrame(master=self, fg_color="transparent")
        self.clientdetGrid.pack(fill="both", padx=27, pady=(20, 0))
        self.clientGenderLabel  = CTkLabel(master=self.clientdetGrid,
                                           text = "Gender",font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left" )
        self.clientGenderLabel.grid(row=0, column=0, sticky="w")
        self.clientGenderCbox = CTkComboBox(master=self.clientdetGrid, 
                                            values=("Male", "Female", "Other"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=157, height=40, cursor='hand2')
        self.clientGenderCbox.grid(row=1, column=0,sticky="w", padx = (0,30))
                          
        self.clientAgeLabel  = CTkLabel(master=self.clientdetGrid,
                                           text = "Age",font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left" )
        self.clientAgeLabel.grid(row=0, column=1, sticky="w")
        self.clientAgeEntry = CTkEntry(master=self.clientdetGrid, 
                                         fg_color="#F0F0F0", 
                                         border_width=0, width=95, height=40)
        self.clientAgeEntry.grid(row=1, column=1, sticky='w',padx = (0,30)) 

        self.clientOPLabel  = CTkLabel(master=self.clientdetGrid,
                                           text = "OP/Proc",font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left" )
        self.clientOPLabel.grid(row=0, column=2, sticky="w")
        self.clientOPCbox = CTkComboBox(master=self.clientdetGrid, 
                                            values=("OP", "Procedure"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=157, height=40, cursor='hand2')
        self.clientOPCbox.grid(row=1, column=2,sticky="w", padx = (0,30))


        self.clientAmountLabel  = CTkLabel(master=self.clientdetGrid,
                                           text = "Amount",font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left" )
        self.clientAmountLabel.grid(row=0, column=4, sticky="w")
        self.clientAmountEntry = CTkEntry(master=self.clientdetGrid, 
                                         fg_color="#F0F0F0", 
                                         border_width=0, width=95, height=40)
        self.clientAmountEntry.grid(row=1, column=4, sticky='w',padx = (0,30)) 


        #Table section
        self.opTableFrame = CTkScrollableFrame(master=self, fg_color="transparent")
        self.opTableFrame.pack(expand=True, fill="both", padx=27, pady=20)

        self.confirmDetailsButton = CTkButton(master=self.opTableFrame, text="Confirm Details",
                                       font=("Arial Bold", 17), 
                                      hover_color="#207244", fg_color="#2A8C55", 
                                      text_color="#fff", 
                                      height=20,  
                                      command=addToTable)
        self.confirmDetailsButton.pack(side="top",  anchor = "ne" ,pady=(0,10))
        

        self.warningLabel = CTkLabel(master=self.opTableFrame,
                                           text = "",font=("Arial Bold", 17), 
                                      text_color="#52A476" )
        self.warningLabel.pack(side="top",  anchor = "c" ,pady=(0,30))

        self.opTable = CTkTable(master=self.opTableFrame, 
                                  values=[["Patient Name", "Phone No.", "Gender", "Age", "OP/Proc", "Amount"]], 
                                  colors=["#E6E6E6", "#EEEEEE"], 
                                  header_color="#2A8C55", hover_color="#B4B4B4")
        self.opTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        self.opTable.pack(expand=True)

        self.billTotalLabel = CTkLabel(master=self.opTableFrame, text="Bill Total: 0",
                                       font=("Arial Bold", 17), 
                                        text_color="#52A476", justify="right"
                                        )
        self.billTotalLabel.pack(anchor="ne", side="right")



if __name__ == "__main__":
    root = CTk()
    obj = clientWindow(root)
    root.mainloop()