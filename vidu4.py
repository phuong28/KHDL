# import pandas as pd
# from pandas import ExcelFile
# Cars_Path = '/Users/Admin/OneDrive/Documents/vidu.xlsx'
# DF = pd.read_excel(Cars_Path)

# print(DF)

import openpyxl
import pprint
wb = openpyxl.load_workbook('/Users/Admin/OneDrive/Documents/vidu.xlsx')
sheet =wb['Sheet1']
cells_tuple=sheet['A1:H30']
for i in range(1,30):
    if(int(cells_tuple[i][2].value)<18 or int(cells_tuple[i][3].value)>25  ):
        print(str(i)+" : sai tuoi ")
for i in range (1,30)  :
    if(int(cells_tuple[i][5].value)<5 or int(cells_tuple[i][5].value)>10) :
        print(str(i)+": điểm phải nằm trong khoảng 5 đến 10")
for i in range (1,30)  :
    if(int(cells_tuple[i][6].value)<1 or int(cells_tuple[i][6].value)>10 or int(cells_tuple[i][7].value)<1 or int(cells_tuple[i][7].value)>10 ) :
        print(str(i)+": điểm phải nằm trong khoảng 1 đến 10")