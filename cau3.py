dsNums[]
n = int(input("Nhap so luong so duong: "))
for i in range (1, n+1)
    num = int(input("Nhap so: "))
    if num == 0:
        break
    dsNums.append(num)
print(dsNums)
for num in dsNums:
    if num % 2 == 0:
    print (dsNums[num])