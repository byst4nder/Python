import openpyxl

wb = openpyxl.load_workbook("example.xlsx")


type(wb)

sheet = wb['Sheet1']
sh = wb.get_sheet_by_name['Sheet1']
