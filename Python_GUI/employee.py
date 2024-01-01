from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
class classEmployee:
    def __init__(self, root):
        self.root=root #this is a type of a frame
        self.root.geometry("1620x780+150+130")
        self.root.title("Derma Medicals | Intelligent Inventory Management | Employee")
        self.root.config(bg="White")
        self.root.focus_force() #Auto selects this wondow on open

        #All Variables
        self.varSearchby=StringVar()
        self.varSearchText=StringVar()

        self.varEmpid=StringVar()
        self.varName=StringVar()
        self.varEmail=StringVar()
        self.varDob=StringVar()
        self.varDoj=StringVar()
        self.varContact=StringVar()
        self.varGender=StringVar()
        self.varPassword=StringVar()
        self.varUtype=StringVar()

        #Searh Frame#
        frameSearch=LabelFrame(self.root, text="Search Employee", 
                               font=("goudy old style", 12, "bold"),
                               bg="white")
        frameSearch.place(x=510, y=20, width=600,height=70)

        #Options#
        cmbSearch=ttk.Combobox(frameSearch, textvariable=self.varSearchby,
                               values=("Select", "ID", "Name","Contact"), 
                               state='readonly', justify=CENTER, 
                               font=("calibri", 12, "bold"),
                               cursor='hand2')
        cmbSearch.place(x=10,y=10,width=180)
        cmbSearch.current(0)

        txtSearch=Entry(frameSearch, textvariable=self.varSearchby,
                        font=("calibri", 15),bg='lightyellow'
                        ).place(x=200, y=3, width=200,height=35)
        buttonSearch=Button(frameSearch,text='Search', font=("calibri", 15),
                            bg='green',fg='white',
                            cursor='hand2')
        buttonSearch.place(x=410, y=5,width=180, height=30)

        #Details box
        titleDetails=Label(self.root,text="Employee Details", 
                           font=("Calibri",20,"bold"),
                           bg="papayawhip",fg="Orange"
                           ).place(x=60,y=110,width=1500)
        #Row 1
        labelEmpId=Label(self.root,text="Emp Id", 
                         font=("Calibri",20,"bold"),
                         bg="ghostwhite",fg="Orange"
                         ).place(x=250,y=155)
        
        labelGender=Label(self.root,text="Gender", 
                    font=("Calibri",20,"bold"),
                    bg="ghostwhite",fg="Orange"
                    ).place(x=700,y=155)
        
        labelContact=Label(self.root,text="Contact", 
                    font=("Calibri",20,"bold"),
                    bg="ghostwhite",fg="Orange"
                    ).place(x=1150,y=155)

        textEmpId=Entry(self.root,textvariable=self.varEmpid, 
                         font=("Calibri",20,"bold"),
                         bg="lightyellow",fg="Orange"
                         ).place(x=350,y=155, width=180)
        
        """ textGender=Entry(self.root,textvariable=self.varGender, 
                    font=("Calibri",20,"bold"),
                    bg="ghostwhite",fg="Orange"
                    ).place(x=800,y=155, width=180)"""
    
        comboGender=ttk.Combobox(self.root, textvariable=self.varGender,
                               values=("Select", "Male", "Female","Other"), 
                               state='readonly', justify=CENTER, 
                               font=("calibri", 12, "bold"),
                               cursor='hand2')
        comboGender.place(x=800,y=155, width=180, height=35)
        cmbSearch.current(0)
        
        textContact=Entry(self.root,textvariable=self.varContact, 
                    font=("Calibri",15),
                    bg="lightyellow",fg="Orange"
                    ).place(x=1250,y=155, width=180,height=35)

        #Row 2
        labelName=Label(self.root,text="Name", 
                         font=("Calibri",20,"bold"),
                         bg="ghostwhite",fg="Orange"
                         ).place(x=250,y=155)
        
        labelDob=Label(self.root,text="D.O.B", 
                    font=("Calibri",20,"bold"),
                    bg="ghostwhite",fg="Orange"
                    ).place(x=700,y=155)
        
        labelDoj=Label(self.root,text="D.O.J", 
                    font=("Calibri",20,"bold"),
                    bg="ghostwhite",fg="Orange"
                    ).place(x=1150,y=155)

        textName=Entry(self.root,textvariable=self.varName, 
                         font=("Calibri",20,"bold"),
                         bg="lightyellow",fg="Orange"
                         ).place(x=350,y=155, width=180)
        
        """ textDob=Entry(self.root,textvariable=self.varD, 
                    font=("Calibri",20,"bold"),
                    bg="ghostwhite",fg="Orange"
                    ).place(x=800,y=155, width=180)"""
    
        comboGender=ttk.Combobox(self.root, textvariable=self.varGender,
                               values=("Select", "Male", "Female","Other"), 
                               state='readonly', justify=CENTER, 
                               font=("calibri", 12, "bold"),
                               cursor='hand2')
        comboGender.place(x=800,y=155, width=180, height=35)
        cmbSearch.current(0)
        
        textDoj=Entry(self.root,textvariable=self.varContact, 
                    font=("Calibri",15),
                    bg="lightyellow",fg="Orange"
                    ).place(x=1250,y=155, width=180,height=35)        

 




if __name__ == "__main__":
    root = Tk()
    obj=classEmployee(root)
    root.mainloop() #so that window stays openmain()