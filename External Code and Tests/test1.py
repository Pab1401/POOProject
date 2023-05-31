from tksheet import Sheet
from tkinter import *
import pandas as pd
import numpy as np
from pandastable import Table, TableModel


#region Main


# class demo(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         self.grid_columnconfigure(0, weight = 1)
#         self.grid_rowconfigure(0, weight = 1)
#         self.frame = Frame(self)
#         self.frame.grid_columnconfigure(0, weight = 1)
#         self.frame.grid_rowconfigure(0, weight = 1)
#         self.data = ([["3", "c", "z"],
#                       ["1", "a", "x"],
#                       ["1", "b", "y"],
#                       ["2", "b", "y"],
#                       ["2", "c", "z"]])
#         self.sheet = Sheet(self.frame,
#                            data = self.data,
#                            theme = "dark",
#                            height = 700,
#                            width = 1100)
#         self.sheet.enable_bindings("copy",
#                                    "rc_select",
#                                    "arrowkeys",
#                                    "double_click_column_resize",
#                                    "column_width_resize",
#                                    "column_select",
#                                    "row_select",
#                                    "drag_select",
#                                    "single_select",
#                                    "select_all")
#         self.frame.grid(row = 0, column = 0, sticky = "nswe")
#         self.sheet.grid(row = 0, column = 0, sticky = "nswe")
        
#         self.sheet.create_header_dropdown(c = 0,
#                                             values = ["all", "1", "2", "3"],
#                                             set_value = "all",
#                                             selection_function = self.header_dropdown_selected)
#         self.sheet.create_header_dropdown(c = 1,
#                                             values = ["all", "a", "b", "c"],
#                                             set_value = "all",
#                                             selection_function = self.header_dropdown_selected)
#         self.sheet.create_header_dropdown(c = 2,
#                                             values = ["all", "x", "y", "z"],
#                                             set_value = "all",
#                                             selection_function = self.header_dropdown_selected)

#     def header_dropdown_selected(self, event = None):
#         hdrs = self.sheet.headers()
#         # this function is run before header cell data is set by dropdown selection
#         # so we have to get the new value from the event
#         hdrs[event.column] = event.text
#         if all(dd == "all" for dd in hdrs):
#             self.sheet.set_sheet_data(self.data,
#                                       reset_col_positions = False,
#                                       reset_row_positions = False)
#         else:
#             self.sheet.set_sheet_data([row for row in self.data if all(row[c] == e or e == "all" for c, e in enumerate(hdrs))],
#                                       reset_col_positions = False,
#                                       reset_row_positions = False)
    
# app = demo()
# app.mainloop()

#endregion

rows, cols = (10, 5)
# arr = [[0]*cols]*rows
# print(arr, "before")

# arr[0][0] = 1 # update only one element
# print(arr, "after")
list = [['' for x in range(rows)] for i in range(cols)]
print(list)
for i in range(cols):
     for j in range(rows):
        list[i][j] = 'Number i: ' + str(i) + ', Number j:' + str(j)
print(list) 