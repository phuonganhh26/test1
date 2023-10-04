from tien_ban import *
Doanh_Thu = {}

month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

while(True):
    
    n = int(input("Nhập tháng: "))
    if n in month:
        value = float(input("Nhập doanh thu: "))
        Doanh_Thu[n] = value

    else:
        break


print(Doanh_Thu)
MoneySum(Doanh_Thu)
MoneyAverage(Doanh_Thu)
MoneyMaxMin(Doanh_Thu)