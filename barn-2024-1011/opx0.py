import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open('data2.csv') as f:
    reader = csv.reader(f, delimiter=',') # changed to ,
    for row in reader:
        ws.append(row)

wb.save('data2_x.xlsx')
