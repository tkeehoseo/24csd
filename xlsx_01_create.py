import openpyxl
def create_example_excel(file_path):
    wb = openpyxl.Workbook()
    ws1 = wb.active
    ws1.title = "Sheet1"
    ws1.append(['데이터1', '데이터2', '데이터3'])
    ws1.append(['데이터4', '데이터5', '데이터6'])
    ws2 = wb.create_sheet(title="Sheet2")
    ws2.append(['값1', '값2'])
    wb.save(file_path)
file_path = 'example.xlsx'
create_example_excel(file_path)
print(f"{file_path} 파일이 생성되었습니다.")
