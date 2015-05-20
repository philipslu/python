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

