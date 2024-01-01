from customtkinter import *
import tkinter
from PIL import Image
from database import loadDatabase
from CTkScrollableDropdown import *
import pandas as pd
from CTkTable import CTkTable
from time import strftime
from new_client import ClientMainViewFrame


medicineDf = loadDatabase()
medSuggestionList = medicineDf['Name'].tolist()

class MedicineApp:
    def __init__(self, master, target_frame):
        self.master = master
        master.title("Pranith Pharmacy")
    


        # Sidebar Frame
        self.sidebar_frame = SidebarFrame(master)
        #self.sidebar_frame.pack_propagate(0)
        #self.sidebar_frame.pack(fill="y", anchor="w", side="left")

        # Main View Frame
        self.main_view = target_frame(master)
        #self.main_view.pack_propagate(0)
        #self.main_view.pack(side="left")

    def clientWindow():
        root = CTk()
        app = MedicineApp(root,ClientMainViewFrame)
        root.mainloop()



class SidebarFrame(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, fg_color="#2A8C55", width=176, height=650, corner_radius=0)
        self.pack_propagate(0)


        # Logo
        self.logoLabel = CTkLabel(master=self, text="", image=self.logoImg)
        self.logoLabel.pack(pady=(38, 0), anchor="center")

        # Buttons
        self.opButton = self.create_button("OP Register", "plus_icon.png", command= clientWindow)
        #self.ordersButton = self.create_button("Orders", "package_icon.png")
        self.ordersListButton = self.create_button("Orders", "list_icon.png")
        self.returnsButton = self.create_button("Returns", "returns_icon.png")
        self.settingsButton = self.create_button("Settings", "settings_icon.png") 
        self.accountButton = self.create_button("Account", "person_icon.png", pady=(160, 0))

    def create_button(self, text, image_filename, pady=(16, 0), command = None):
        img_data = Image.open(f"Python_GUI\\ctk\\{image_filename}")
        img = CTkImage(dark_image=img_data, light_image=img_data)
        return CTkButton(master=self, image=img, text=text, fg_color="transparent", font=("Arial Bold", 14),
                         hover_color="#207244", anchor="w",command = command).pack(anchor="center", ipady=5, pady=pady )

    @property
    def logoImg(self):
        return CTkImage(dark_image=Image.open("Python_GUI\\ctk\\logo.png"),
                        light_image=Image.open("Python_GUI\\ctk\\logo.png"), size=(77.68, 85.42))
    


class MainViewFrame(CTkFrame):
    def __init__(self, master=None):
        super().__init__(master, fg_color="#fff", width=680, height=650, corner_radius=0)
        self.pack_propagate(0)

        def clearBillTable():
            
            numRows = self.billTable.rows
            self.billTable.delete_rows(range(1,numRows))
            self.billTotalLabel.configure(text = "Bill Total: 0")
            
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

        self.clientGenderLabel  = CTkLabel(master=self.clientGrid,
                                           text = "Gender",font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left" )
        self.clientGenderLabel.grid(row=2, column=0, sticky="w")
        
        self.clientGenderCbox = CTkComboBox(master=self.clientGrid, 
                                            values=("Male", "Female", "Other"), state='readonly', 
                                            justify=CENTER, font=("calibri", 12, "bold"), 
                                            width=157, height=40, cursor='hand2')
        self.clientGenderCbox.grid(row=3, column=0,sticky="w")
        # Search Section
        self.searchGrid = CTkFrame(master=self, fg_color="transparent")
        self.searchGrid.pack(fill="both", padx=27, pady=(31, 0))

        self.itemNameLabel = CTkLabel(master=self.searchGrid, 
                                      text="Item Name", font=("Arial Bold", 17), 
                                      text_color="#52A476", justify="left")
        self.itemNameLabel.grid(row=0, column=0, sticky="w")

        self.itemNameEntry = CTkEntry(master=self.searchGrid, 
                                      fg_color="#F0F0F0", 
                                      border_width=0, width=285, height=40)
        self.itemNameEntry.grid(row=1, column=0, sticky='w', padx = (0,20))

        self.medicineDropDown = CTkScrollableDropdown(self.itemNameEntry, 
                                                      values=medSuggestionList, 
                                                      command=lambda e: fillSelectedValue(e), 
                                                      autocomplete=True)
    
        # Fill the entry with selected drop down value    
        def fillSelectedValue(value):
            
            currentEntry = len(self.itemNameEntry.get())
            self.itemNameEntry.delete(0,currentEntry)
            self.itemNameEntry.insert(0,value)
            currentMedQty = medicineDf.loc[medicineDf["Name"] == value]["Quantity"].tolist()           
            self.qtyInStockLabel.configure(text="Quantity in Stock:"+ str(currentMedQty[0]))
        # Get the details of the selected medicine from the dropdown value
        
        def getMedDetails():
            global currentMedQty 
            global currentMedPrice
            global currentMedType 
            global currentMedName
            global billTotal 
            
            currentMedName = self.itemNameEntry.get()
            currentSaleQty = self.qtySaleEntry.get()
            currentMedQty = int(medicineDf.loc[medicineDf["Name"] == currentMedName]["Quantity"].iloc[0])
            currentMedPrice = int(medicineDf.loc[medicineDf["Name"] == currentMedName]["Price"].iloc[0])
            currentMedType = str(medicineDf.loc[medicineDf["Name"] == currentMedName]["Type"].iloc[0])
            
            totalSalePrice = int(currentSaleQty)*currentMedPrice
            
            numRows=self.billTable.rows
  
            self.billTable.add_row(index=numRows, values=[currentMedName, currentMedType, currentMedQty, currentMedPrice, currentSaleQty, totalSalePrice])
            self.itemNameEntry.delete(0,len(currentMedName))
            #print("number of rows:",self.billTable.rows)
            if self.billTable.rows == 2: #If there is one entry in table
                billTotal = totalSalePrice
            elif self.billTable.rows > 2: #If there are multiple entries in table
                billTotal = billTotal+totalSalePrice
            self.billTotalLabel.configure(text= "Bill Total: " + str(billTotal))
            #print(type(currentMedType), type(currentMedName), type(currentMedQty), type(currentMedPrice), type(currentSaleQty), type(totalSalePrice))
            
            
            #print("Bill Total:",billTotal)
        
        def clearBillTable():
            numRows = self.billTable.rows
            self.billTable.delete_rows(range(1,numRows))

        self.addToBillButton = CTkButton(master=self.searchGrid, text="Add to Bill", 
                                      font=("Arial Bold", 17), 
                                      hover_color="#207244", fg_color="#2A8C55", 
                                      text_color="#fff", height=40, 
                                      command=getMedDetails)
        self.addToBillButton.grid(row=1, column=2, sticky='e', padx=15)


        quantity_frame = CTkFrame(master=self.searchGrid, fg_color="transparent")
        quantity_frame.grid(row=1, column=1, padx=(10,0), pady=(0,0), sticky="w")
        def quantityIncrease():
            currentEntry = self.qtySaleEntry.get()
            #print("type is ", type(currentEntry))
            if currentEntry == "":
                currentEntry = 0
                self.qtySaleEntry.insert(0,1)
            else: currentEntry = int(self.qtySaleEntry.get())
            if currentEntry > 0 :
                print(currentEntry)
                self.qtySaleEntry.delete(0,currentEntry)         
                self.qtySaleEntry.insert(0,currentEntry+1)
        def quantityDecrease():
            currentEntry = self.qtySaleEntry.get()
            #print("type is ", type(currentEntry))
            if currentEntry == "":
                currentEntry = 0
            else: currentEntry = int(self.qtySaleEntry.get())
            if currentEntry > 1 :
                self.qtySaleEntry.delete(0,currentEntry)
                self.qtySaleEntry.insert(0,currentEntry-1)
                    

        
        self.qtyDecreaseButton = CTkButton(master=quantity_frame, text="-", 
                                            width=25, fg_color="#2A8C55", 
                                            hover_color="#207244", font=("Arial Black", 16),
                                            command=quantityDecrease
                                            )
        self.qtyDecreaseButton.pack(side="left", anchor="w")
        self.qtySaleEntry = CTkEntry(master=quantity_frame, #placeholder_text=0,
                                       text_color="#2A8C55", font=("Arial Black", 16),
                                       width=60
                                        )
        self.qtySaleEntry.pack(side="left", anchor="w", padx=10)
        self.qtyIncreaseButton = CTkButton(master=quantity_frame, text="+", width=25,  
                                           fg_color="#2A8C55",hover_color="#207244", 
                                           font=("Arial Black", 16),
                                           command=quantityIncrease
                                           )
        self.qtyIncreaseButton.pack(side="left", anchor="w")
        
        #self.detailsFrame = CTkFrame(master=self.searchGrid, fg_color="transparent")
        self.qtyInStockLabel = CTkLabel(master=self.searchGrid, text = "Quantity in Stock: 0",
                                        font=("Arial Bold", 17), 
                                        text_color="#52A476", justify="left",
                                        pady=30)
        self.qtyInStockLabel.grid(row=3, column=0, sticky="w")

        billTableFrame = CTkScrollableFrame(master=self, fg_color="transparent")
        billTableFrame.pack(expand=True, fill="both", padx=27, pady=21)

        self.newSaleButton = CTkButton(master=billTableFrame, text="Clear Table",
                                       font=("Arial Bold", 17), 
                                      hover_color="#207244", fg_color="#2A8C55", 
                                      text_color="#fff", 
                                      height=20,  
                                      command=clearBillTable)
        self.newSaleButton.pack(side="top",  anchor = "ne")

        self.billTable = CTkTable(master=billTableFrame, 
                                  values=[["Name", "Type", "Stock", "MRP", "Quantity", "Total Price"]], 
                                  colors=["#E6E6E6", "#EEEEEE"], 
                                  header_color="#2A8C55", hover_color="#B4B4B4")
        self.billTable.edit_row(0, text_color="#fff", hover_color="#2A8C55")
        self.billTable.pack(expand=True)

        self.billTotalLabel = CTkLabel(master=billTableFrame, text="Bill Total: 0",
                                       font=("Arial Bold", 17), 
                                        text_color="#52A476", justify="right"
                                        )
        self.billTotalLabel.pack(anchor="ne", side="right")


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
    app = MedicineApp(root,MainViewFrame)
    root.mainloop()
