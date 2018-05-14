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

# 2015 ~ 2018
volList = []
start = findIndexAtValue(raw_date, '2015-01-02')
end = findIndexAtValue(raw_date, '2015-12-31')
start2 = findIndexAtValue(raw_date, '2016-01-04')
end2 = findIndexAtValue(raw_date, '2018-04-27')

for i in range(len(raw_date)):
    if i < 30:
        volList.append(0)
    else:
        before = i - 30
        temp = (raw_usd[i] - raw_usd[before]) / raw_usd[i]
        volList.append(temp)

# volList check
nonZeroCount = 0
for i in range(len(volList)):
    if volList[i] != 0:
        nonZeroCount += 1
print("raw_date length " + str(len(raw_date)))
print("volList length " + str(len(volList)))
print("nonZeroCount " + str(nonZeroCount))

plt.plot(volList, label="volList")
plt.legend()
plt.show()

# yield
yieldList = []

j = 0

while j < len(volList) - 40:

    if j >= start and volList[j] < -0.02 and j < end + 1:
        buyPrice = raw_usd[j]
        duration = j + 40
        sellPrice = raw_usd[duration]
        result = (sellPrice - buyPrice) / sellPrice
        yieldList.append(result)
        j += 40
        continue
    elif j >= start2 and volList[j] > 0.02 and j < end2 + 1:
        sellPrice = raw_usd[j]
        duration = j+40
        buyPrice = raw_usd[duration]
        result = (sellPrice - buyPrice) / sellPrice
        yieldList.append(result)
        j += 40
        continue

    j += 1

# fraction
f = 0
fList = []
sumList = []

while f < 20:
    elog1fx = 0

    for k in range(len(yieldList)):
        elog1fx += ((1 / len(yieldList)) * np.log2(1 + f * yieldList[k]))

    fList.append(f)
    sumList.append(elog1fx)

    f += 0.01

plt.plot(fList, sumList, label='f1')
plt.legend()
plt.show()


# compound interest
seed = 100
seedlist = []
for i in range(len(yieldList)):
    seed *= (1 + 5 * yieldList[i])
    seedlist.append(seed)

plt.plot(seedlist,label='compound interest growth')
plt.legend()
plt.show()

plt.plot(yieldList,label='yield distribution')
plt.legend()
plt.show()
