import numpy as np
import matplotlib.pyplot as plt
import csv
import os


# rawX에서 targetValue의 인덱스 찾기
def findIndexAtValue(rawX, targetValue):
    for i in range(len(rawX)):
        if rawX[i] == targetValue:
            return i


# rawX의 문자열을 실수로. 비정형 문자열에 대한 예외처리 필요.
def strToFloat(rawX):
    floatX = []
    for i in range(len(rawX)):
        if rawX[i] != '.':
            floatX.append(float(rawX[i]))
        elif rawX[i] == '.':
            # 예외처리 문자열의 경우 0이 아니라 이전 인덱스의 값으로 대체.
            if i > 0:
                if rawX[i - 1] == '.':
                    floatX.append(float(rawX[i - 2]))
                else:
                    floatX.append(float(rawX[i - 1]))
            else:
                floatX.append(0)

    return floatX


# csv 파일 읽기
raw_date = []
raw_usd = []
raw_total = []

script_dir = os.path.dirname(__file__)
rel_path = "dataStorage/USDKRW0507.csv"
abs_file_path = os.path.join(script_dir, rel_path)

f = open(abs_file_path, 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    raw_date.append(line[0])
    raw_usd.append(line[1])
f.close()

if raw_date[0] == 'DATE':
    del raw_date[0]
if raw_usd[0] == 'DEXKOUS':
    del raw_usd[0]

# raw_total
raw_total.append(raw_date)
raw_total.append(raw_usd)

# raw_usd의 문자열을 실수로. '.' 예외처리 필요.
raw_usd = strToFloat(raw_usd)

print(findIndexAtValue(raw_date, '2015-01-01'))  # 438
print(findIndexAtValue(raw_date, '2015-12-31'))  # 698
print(findIndexAtValue(raw_date, '2018-04-27'))  # 1304

# YoY   from 2014-05-01 to 2018-04-27
yoyList = []
start = findIndexAtValue(raw_date, '2014-05-01')
end = findIndexAtValue(raw_date, '2018-04-27')

for i in range(len(raw_date)):

    if i < start:
        yoyList.append(0)
    else:
        before = i - 365
        temp = (raw_usd[i] - raw_usd[before]) / raw_usd[i]
        yoyList.append(temp)

# MoM   from 2013-06-03 to 2018-04-27
momList = []
start = findIndexAtValue(raw_date, '2013-06-03')
end = findIndexAtValue(raw_date, '2018-04-27')

for i in range(len(raw_date)):
    if i < start:
        momList.append(0)
    else:
        before = i - 30
        temp = (raw_usd[i] - raw_usd[before]) / raw_usd[i]
        momList.append(temp)

plt.plot(momList, label='momList')
plt.legend()
plt.show()

# momYield and Kelly : 1
momYield = []

j = 0

while j < len(momList) - 10:

    if momList[j] > 0.02:
        buyPrice = raw_usd[j]
        duration = j + 5
        sellPrice = raw_usd[duration]
        result = (sellPrice - buyPrice) / buyPrice
        momYield.append(result)
        j += 5
        continue

    elif momList[j] < -0.02:
        sellPrice = raw_usd[j]
        duration = j + 5
        buyPrice = raw_usd[duration]
        result = (sellPrice - buyPrice) / sellPrice
        momYield.append(result)
        j += 5
        continue

    j += 1

f = 0
fList = []
maxList = []
while f < 10:
    elog1fx = 0
    for k in range(len(momYield)):
        elog1fx += ((1 / len(momYield)) * np.log2(1 + f * momYield[k]))
    fList.append(f)
    maxList.append(elog1fx)

    f += 0.01

plt.plot(fList, maxList, label='f1')
plt.legend()
plt.show()

plt.plot(momYield, label='momYield1')
plt.legend()
plt.show()

# momYield and Kelly : 2
momYield = []

j = 0

while j < len(momList) - 30:

    if momList[j] > 0.03:
        sellPrice = raw_usd[j]
        duration = j + 30
        buyPrice = raw_usd[duration]
        result = (sellPrice - buyPrice) / sellPrice
        momYield.append(result)
        j += 30
        continue


    elif momList[j] < -0.03:
        buyPrice = raw_usd[j]
        duration = j + 30
        sellPrice = raw_usd[duration]
        result = (sellPrice - buyPrice) / buyPrice
        momYield.append(result)
        j += 30
        continue

    j += 1

f = 0
fList = []
maxList = []
while f < 10:
    elog1fx = 0
    for k in range(len(momYield)):
        elog1fx += ((1 / len(momYield)) * np.log2(1 + f * momYield[k]))
    fList.append(f)
    maxList.append(elog1fx)

    f += 0.01

plt.plot(fList, maxList, label='f2')
plt.legend()
plt.show()

plt.plot(momYield, label='momYield2')
plt.legend()
plt.show()
