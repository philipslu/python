#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Function:
Author:     Philip Lu
Version:    2015-04-18
"""

import csv
import xlwt 

with open('c:/Sheet1.csv','rb') as csvfile:
        reader = csv.reader(csvfile)
        for i,rows in enumerate(reader):
                if i == 1:
                        row = rows
print row

csvfile=file('c:/Sheet1.csv','wb')    
writer = csv.writer(csvfile)
writer.writerow(['site','data','total','totalsold','memo'])
data = [row]
writer.writerows(data)
csvfile.close()

wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet1')
with open('c:/Sheet1.csv', 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, val in enumerate(row):
                ws.write(r, c, val)
wb.save('Sheet1' + '.xls')