from tkinter import *
from datetime import date

# This is going to be a program to create invoices for a childminder (ie Sarah). 
# It will run off of calculations and a database. ie. It will store information
# about standard hours for each child, standard cost per hour and when any extra
# hours were, when any extra or reduced costs were. Then by inputting a date range
# it will return the charge for that period.You will also be able to return a
# list of any extras that have been applied to any child account
#
# I need to be able to enter information into attributes of a 'child' class. The 
# 'child' class would need to have attributes representing the hours they are in
# possibly one attribute for each day of the week, or a total weekly hours. Other
# would be name; DOB; contact number, stuff like that maybe. So adding a child to
# to the system would create a new instance of the child class, and add the info 
# to the database. And attributes could be added and changed at any time.

# Screens: There needs to be a place to create a new child and enter details.
# There needs to be a screen for entering the parameters of the invoice. 
# There needs to be a screen on which the invoice is returned in a printable format.
# Maybe it should actually return a .txt file - that would be printable!

# I realise the information will need to be stored somewhere - so a text file, or 
# database will be necessary. I think it can be happily done with just a csv file. 
#
# Pip pip!
#

### GLOBAL VARIABLES ###

std_fees = 4

### FUNCTIONS ### 

# ---- Nav Buttons at top

def addChild(): # shows the add child frame and hides the others when the add child button is clicked
    add_exception.grid_remove()
    create_invoice.grid_remove()
    add_child.grid(row=1, column=0, sticky=W)
    return

def addException(): # shows the add exception frame and hides the others when the add child button is clicked
    add_child.grid_remove()
    create_invoice.grid_remove()
    add_exception.grid(row=1, column=0, sticky=W)
    return

def createInvoice(): # shows the create invoice frame and hides the others when the add child button is clicked
    add_child.grid_remove()
    add_exception.grid_remove()
    create_invoice.grid(row=1, column=0, sticky=W)

# ---- Data writing functions

def writeChild(): # this function writes the child data to file
    child = {}
    child['name'] = entName.get()
    child['dob'] = entDob.get()
    child['mon'] = entMon.get()
    child['tue'] = entTue.get()
    child['wed'] = entWed.get()
    child['thu'] = entThu.get()
    child['fri'] = entFri.get()
    child_data = open("inv_data.txt","a")
    child_data.write(str(child)+"\n")
    child_data.close()
    print(child) # only print for testing.

def writeException(): # this function writes the date exceptions to file. This will be a list with a child-specific object name
    pass

def checkExceptions(): # this function checks whether the queried date range includes any of the date exceptions and returns how many. Obviously needs to look up child against data held. I imagine this will be a matter of 'for line in file, make that the dict. If dict contains child name, do the thing, if not move onto the next line
    pass

def calcDays(): # counts the number of days in the queried date range and substracts the return value of checkExceptions()
    sd_str = entStartDate.get()
    ed_str = entEndDate.get()
    sd_date = date(int(sd_str[6:10]), int(sd_str[3:5]), int(sd_str[0:2]))
    ed_date = date(int(ed_str[6:10]), int(ed_str[3:5]), int(ed_str[0:2]))
    days_diff = ed_date - sd_date
    return days_diff.days + 1

def calcFees(): # multiplies the return value of calcDays() by the recorded fees level (need to work out where to store this)
    '''
    
    '''
    fees = entHourlyRate.get()
    days = calcDays()
    return days * int(fees)
    print(days * int(fees))

def displayInvoice():
    pass

def writeInvoice():
    fees = entHourlyRate.get()
    print(calcFees()) #this is just for testing, to make sure i can call a function within a function properly. And i can!

def displayChild():
    pass



### GUI ###

app = Tk()

app.title('Invoicer')

app.geometry('800x300+100+500')

menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=app.quit)
filemenu.add_command(label="Help") # need to add command in
menubar.add_cascade(label="File", menu=filemenu)
app.config(menu=menubar)

    ### toolbar frame

toolbar = Frame(app)

a = Button(toolbar, text="Add child", command=addChild)
a.pack(side=LEFT, padx=2, pady=2)
b = Button(toolbar, text="Add exception", command=addException)
b.pack(side=LEFT, padx=2, pady=2)
c = Button(toolbar, text="Create invoice", command=createInvoice)
c.pack(side=LEFT, padx=2, pady=2)

toolbar.grid(row=0, column=0, columnspan=2)

    ### Other frames: text_display; add_child; add_exception; create_invoice

text_display = Frame(app)

mess = Label(text_display, text="this is the text display area").grid(padx=2, pady=2, sticky=N)

text_display.grid(row=1, column=2)

# add child

add_child = Frame(app)

lName = Label(add_child, text='name').grid(row=1, column=0, sticky=E)

entName = Entry(add_child)
entName.grid(row=1, column=1)

lDob = Label(add_child, text='D.O.B.').grid(row=2, column=0, sticky=E)

entDob = Entry(add_child)
entDob.grid(row=2, column=1)

lMon = Label(add_child, text='Monday hours').grid(row=3, column=0, sticky=E)

entMon = Entry(add_child)
entMon.grid(row=3, column=1)

lTue = Label(add_child, text='Tuesday hours').grid(row=4, column=0, sticky=E)

entTue = Entry(add_child)
entTue.grid(row=4, column=1)

lWed = Label(add_child, text='Wednesday hours').grid(row=5, column=0, sticky=E)

entWed = Entry(add_child)
entWed.grid(row=5, column=1)

lThu = Label(add_child, text='Thursday hours').grid(row=6, column=0, sticky=E)

entThu = Entry(add_child)
entThu.grid(row=6, column=1)

lFri = Label(add_child, text='Friday hours').grid(row=7, column=0, sticky=E)

entFri = Entry(add_child)
entFri.grid(row=7, column=1)

bOk = Button(add_child, text = 'ok', command=writeChild).grid(row=10, column=1, sticky=E)
bCancel = Button(add_child, text = 'cancel').grid(row=11, column=1, sticky=E)

# add exception

add_exception = Frame(app)

exDate = Label(add_exception, text = 'Date').grid(row=1, column=0)
entDate = Entry(add_exception)
entDate.grid(row=1, column=1)

exDetails = Label(add_exception, text = 'Details').grid(row=2, column=0)
entDetails = Listbox(add_exception, height=4, borderwidth=0)
entDetails.insert(0, "My holiday")
entDetails.insert(1, "Child holiday")
entDetails.insert(2, "My absense")
entDetails.insert(3, "Child absense")
entDetails.grid(row=2, column=1)

bSaveEx = Button(add_exception, text = 'Save', command=writeException).grid(row=3, column=1, sticky=E)
bCancelEx = Button(add_exception, text = 'Cancel').grid(row=4, column=1, sticky=E)

# create invoice

create_invoice = Frame(app)

childName = Label(create_invoice, text='Name of child').grid(row=1, column=0, sticky=E)

entChildName = Entry(create_invoice)
entChildName.grid(row=1, column=1)

startDate = Label(create_invoice, text='Start date (dd/mm/yyyy)').grid(row=2, column=0, sticky=E)

entStartDate = Entry(create_invoice)
entStartDate.grid(row=2, column=1)

endDate = Label(create_invoice, text='End date (dd/mm/yyyy)').grid(row=3, column=0, sticky=E)

entEndDate = Entry(create_invoice)
entEndDate.grid(row=3, column=1)

hourlyRate = Label(create_invoice, text="Hourly rate in £").grid(row=4, column=0, sticky=E)
entHourlyRate = Entry(create_invoice)
entHourlyRate.grid(row=4, column=1)

bCreateInvoice = Button(create_invoice, text = 'Create invoice', command=calcFees).grid(row=5, column=1, sticky=E)
bCancelInvoice = Button(create_invoice, text = 'Cancel').grid(row=6, column=1, sticky=E)

app.grid_columnconfigure(2,minsize=300)

app.mainloop()
