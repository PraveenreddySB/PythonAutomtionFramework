import xlrd
import xlwt

workbook = xlrd.open_workbook("C:/Users/pbangari/PycharmProjects/AutomationFramework/TestData/TestDataFile.xls")
sheet = workbook.sheet_by_name("UserCredencials")

rowcount = sheet.nrows
colcount = sheet.ncols

print(rowcount)
print(colcount)

result_data = []
for curr_row in range(1, rowcount, 1):
    row_data = []
    for curr_col in range(1, colcount - 1, 1):
        data = sheet.cell_value(curr_row, curr_col)
        print(data)
        row_data.append(data)

    result_data.append(row_data)




