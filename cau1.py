danh_sach_tu = []
n = int(input("Nhập số lượng từ: "))
for i in range(1, n+1):
    tu = input("Nhập từ: ")
    if tu.lower() == 'exit':
        break
    danh_sach_tu.append(tu)

print(' '.join(danh_sach_tu).title()) 