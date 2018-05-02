
import matplotlib.pyplot as plt

# 이동평균선 그래프
def drawAvgLine(rawX, rawValue, startIndex, endIndex, averageDay):
    avgLine = []
    for i in range(len(rawX)):
        # 60일선이라면 인덱스 58까지는 0, 인덱스 59부터 충족.
        if i < averageDay - 1:
            avgLine.append(0)
        else:
            tempSum = 0
            for j in range(i - 59, i):
                tempSum += rawValue[j]
            tempResult = tempSum / averageDay
            avgLine.append(tempResult)

    plt.plot(rawX[startIndex:endIndex], avgLine[startIndex:endIndex])
    plt.plot(rawX[startIndex:endIndex], rawValue[startIndex:endIndex])
    plt.show()