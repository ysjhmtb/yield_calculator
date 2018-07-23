class RowObject:
    def __init__(self, name, date, longshort, price, amount):
        self.name = name
        self.date = date
        self.longshort = longshort
        self.price = price
        self.amount = amount


# 평균 매수 가격
def getAverageLongPrice(rowlist):
    pmula = 0
    amount_sum = 0
    for i in range(len(rowlist)):
        if (rowlist[i].longshort == "long"):
            amount_sum = amount_sum + rowlist[i].amount
            inserted_result = rowlist[i].price * rowlist[i].amount
            pmula = pmula + inserted_result

    result = pmula / amount_sum
    print("총 매수 자금 : " + str(pmula))
    return result


# KODEX 레버리지
kodex_leverage_list = []

kodex_leverage_list.append(RowObject("KODEX레버리지", "2017/12/04/MON", "long", 17610, 16))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2017/12/05/TUE", "long", 17850, 2))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2017/12/20/WED", "long", 17620, 27))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2017/12/21/THU", "long", 16875, 30))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2017/12/26/TUE", "long", 17030, 58))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2018/02/06/TUE", "long", 16415, 91))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2018/04/25/WED", "long", 16230, 123))

kodex_leverage_list.append(RowObject("KODEX레버리지", "2018/06/18/MON", "long", 15330, 110))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2018/06/18/MON", "long", 15325, 110))
kodex_leverage_list.append(RowObject("KODEX레버리지", "2018/06/18/MON", "long", 15315, 110))

# KODEX 미국달러선물인버스2X


# KODEX 미국달러선물레버리지
dollar_leverage_list = []
dollar_leverage_list.append(RowObject("KODEX미국달러선물레버리지", "2018/07/23/MON", "long", 8930, 100))
dollar_leverage_list.append(RowObject("KODEX미국달러선물레버리지", "2018/07/23/MON", "long", 8935, 100))
dollar_leverage_list.append(RowObject("KODEX미국달러선물레버리지", "2018/07/23/MON", "long", 8935, 20))

# KODEX 레버리지 평균 매입 가격
print(getAverageLongPrice(kodex_leverage_list))
# 총 매수 자금 : 10833945
# 16002.872968980797

# KODEX 미국달러선물레버리지 평균 매입 가격
print(getAverageLongPrice(dollar_leverage_list))
# 총 매수 자금 : 1965200
# 8932.727272727272

