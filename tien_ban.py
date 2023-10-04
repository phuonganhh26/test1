def MoneySum(Doanh_Thu):
    list1 = []
    value = Doanh_Thu.values()
    list1 = value
    sumMoney = sum(list1)
    print("Tổng số tiền bán: ", sumMoney)

def MoneyAverage(Doanh_Thu):
    list1 = []
    value = Doanh_Thu.values()
    list1 = value
    avr = sum(list1)/len(list1)
    print("Số tiền bình quân mỗi tháng là: ", avr)

def MoneyMinMax(Doanh_Thu):
    list1 = []
    value = Doanh_Thu.values()
    list1 = value
    DSMaxMin = [min(list1), max(list1)]
    print(DSMaxMin)

