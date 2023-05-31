from tksheet import Sheet
from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from pandastable import Table, TableModel
import os

#gets your current directory
dirname = os.path.dirname(__file__)

#concatenates your current directory with your desired subdirectory
results = os.path.join(dirname, r'Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx')

global final
# Creates a variable with the Excel file's directory in the computer
xls = pd.ExcelFile(results)
# Gets the names of all the sheets in the excel and stores them in a variable as a list
names = xls.sheet_names

# Creating a class that modifies and uses all the values necesary to create the TK sheet from the library and to display the information
class demo(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(650, weight = 1)
        self.frame = Frame(self)
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.data = (final)
        self.sheet = Sheet(self.frame,
                           data = self.data,
                           theme = "dark",
                           height = 400,
                           width = 840)
        self.sheet.enable_bindings("copy",
                                   "rc_select",
                                   "arrowkeys",
                                   "double_click_column_resize",
                                   "column_width_resize",
                                   "column_select",
                                   "row_select",
                                   "drag_select",
                                   "single_select",
                                   "select_all")
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
        self.sheet.headers(newheaders = ['Startup','Shieldstun', 'Landing Lag', 'Base Damage', 'Shieldlag', 'Shieldstun'])
        self.sheet.row_index(newindex = indexData)

# Function to get the data frame from the selected character
def retrieve_input():
    input = menu.get() # Gets the text from the stringvar menu which was selected in the dropdown menu
    sheet = pd.read_excel(xls, sheet_name=input, index_col=0) # adds the sheet from the selected character to a variable by using the name of the sheet
    ColumnData = pd.DataFrame(sheet, columns=['Startup','Shieldstun', 'Landing Lag', 'Base Damage', 'Shieldlag', 'Shieldstun']) # Filters data in the original excel sheet to have only the desired information
    ColumnData.fillna(" ", inplace=True) # replaces all 'Na' values with '-'
    global indexData # creates a global variable indexData
    indexData = sheet.index.tolist() # transforms the index of the sheet into a list for later use in tk sheet
    cols, rows = (ColumnData.columns, len(ColumnData)) # gets the columns and the rows of the data frame and assigns them to the values cols and rows respectively
    global final
    final = ColumnData.values.tolist() # Makes the values from the entire data frame into a list for later use in the tk sheet
    app = demo() # calls for the tk sheet creating class which uses the final and
    app.mainloop()

# Destroys the root window 
def end():
    root.destroy()

# Creates a window called root with the specified dimensions
root = Tk()
root.config(width=1000, height=500)

# Creates a drop down menu with a obtainable value with the stringvar and places it in the button inside the window previously created
menu = StringVar()
menu.set("Select the Character")
# Uses the list of all the sheet names from before as all the possible options in the drop down menu
drop = ttk.Combobox(root, textvariable = menu, values = names[1:])
drop.place(x=100, y=100)


def NewFunction():
    input = menu.get() # Gets the text from the stringvar menu which was selected in the dropdown menu
    sheet = pd.read_excel(xls, sheet_name=input, index_col=0) # adds the sheet from the selected character to a variable by using the name of the sheet
    print({0} if sheet['Start Up'] == 0 else 'no')

# Creates 2 buttons, a button to trigger the Data obtaining command and a button to end the main window
button = Button(root, text="Get Data", command=retrieve_input)
button.place(x=100, y=200)
button3 = Button(root, text='test', command=NewFunction)
exit = Button(root, text="Exit", command=end)
exit.place(x=200, y=200)

root.mainloop()
