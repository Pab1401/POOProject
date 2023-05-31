#dictionary = {pd.read_excel('C:\Docs\Super Smash Bros. Ultimate Patch 13.1 Frame Data - 01 - Mario.csv')}

import pandas as pd
import numpy as np
from pandastable import Table, TableModel
from tkinter import *
from tksheet import *

#df1 = pd.read_excel('C:\Docs\Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx', sheet_name='01 - Mario', index_col=0)
#df2 = pd.read_excel('C:\Docs\Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx', sheet_name='61 - Cloud', index_col=0)

# , columns=['Startup','Shieldstun', 'Landing Lag', 'Base Damage', 'Shieldlag', 'Shieldstun']

#ColumnData = pd.DataFrame(df1, columns=['Startup','Shieldstun', 'Landing Lag', 'Base Damage', 'Shieldlag', 'Shieldstun'])
#Chars = list()
# filename = 'C:\Docs\Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx'
# thing = pd.read_excel(filename, engine='openpyxl')
# sheet_names = thing.sheet_names()
# print(sheet_names)
# thing = pd.read_excel('C:\Docs\Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx', sheet_name=None, index_col=0)
all_sheets = []
xls = pd.ExcelFile('C:\Docs\Super Smash Bros. Ultimate Patch 13.1 Frame Data.xlsx')
names = xls.sheet_names

# def Importer():
#     for items in range(81):
#         sheet = pd.read_excel(xls, sheet_name=items+1, index_col=0)
#         ColumnData = pd.DataFrame(sheet, columns=['Startup','Shieldstun', 'Landing Lag', 'Base Damage', 'Shieldlag', 'Shieldstun'])
#         ColumnData.fillna("-", inplace=True)
#         all_sheets.append(ColumnData)
#     return all_sheets

# print(all_sheets[15])

#FullList = Importer()

#print(FullList[4])

# class TestApp(Frame):
#         """Basic test frame for the table"""
#         def __init__(self, parent=None):
#             self.parent = parent
#             Frame.__init__(self)
#             self.main = self.master
#             self.main.geometry('600x400+200+100')
#             self.main.title('Table app')
#             f = Frame(self.main)
#             f.pack(fill=BOTH,expand=1)
#             self.table = pt = Table(f, dataframe=ColumnData,
#                                     showtoolbar=True, showstatusbar=True)
#             pt.show()
#             return

#     app = TestApp()
#     #launch the app
#     app.mainloop() 




def retrieve_input():
    input = menu.get()
    sheet = pd.read_excel(xls, sheet_name=input, index_col=0)
    ColumnData = pd.DataFrame(sheet, columns=['Startup','Shieldstun', 'Landing Lag', 'Base Damage', 'Shieldlag', 'Shieldstun'])
    ColumnData.fillna("-", inplace=True)
    print(ColumnData)
    rootCharacter = Tk()
    rootCharacter.geometry('800x600')
    rootCharacter.title(input)
    f = Frame(rootCharacter)
    f.pack(fill=BOTH, expand=1)
    rootCharacter.table = pt = Table(f, dataframe=ColumnData)
    pt.show()
    # USE GRID
    # rootTest = Tk()
    # sheet = Sheet(rootTest, show_table=True) 
    # sheet.set_sheet_data(data=ColumnData.to_dict(), 
    #                      reset_col_positions= True,
    #                      reset_row_positions= True,
    #                      redraw=True,
    #                      verify=False,
    #                      reset_highlights=False
        
    # )
    # sheet.grid()
    rootCharacter.mainloop()



def end():
    root.destroy()


root = Tk()
root.config(width=1000, height=500)

menu = StringVar()
menu.set("Select the Character")
drop = OptionMenu(root, menu, *names[1:],command= retrieve_input)
drop.place(x=100, y=100)



#entry = Entry()
#entry.place(x=100, y = 100)
button = Button(root, text="send", command=(retrieve_input))
button.place(x=100, y=200)
exit = Button(root, text="exit", command=end)
exit.place(x=200, y=200)


root.mainloop()
# print(all_sheets[5])

# print(all_sheets[0])

#RowData= df.iloc[1:38,:1]
# StartUpData = df.iloc[0:28,1:4]
# MoveData = pd.DataFrame(df, columns=['A'])
# TotalFramesData = pd.DataFrame(df, 1)

# ColumnData.set_index(RowData[1,1])
# dfMario = pd.read_csv('C:\Docs\Super Smash Bros. Ultimate Patch 13.1 Frame Data - 01 - Mario.csv', index_col=0)
#df1['Startup'] = np.where(df1['Startup'] == '', 'N/A')
#df1['Total Frames'] = np.where(df1['Total Frames'] == '', 'N/A')
#df1['Landing Lag'] = np.where(df1['Landing Lag'] == '', 'N/A')
#df1['Shieldstun'] = np.where(df1['Shieldstun'] == '', 'N/A')

#print('Mario', "\n", df1)
#   ColumnData.fillna("-", inplace=True)
#   print(ColumnData)
#print('Cloud', "\n", df2)

#print(ColumnData)
#print(RowData)  
