import xlrd
import matplotlib.pyplot as plt
file_location = "values.xls"
workbook = xlrd.open_workbook(file_location)
first_sheet = workbook.sheet_by_index(0)
x = [first_sheet.cell_value(i, 0) for i in range(first_sheet.ncols)]
y = [first_sheet.cell_value(i, 1) for i in range(first_sheet.ncols)]
plt.plot(x,y)
plt.show()