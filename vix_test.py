# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class dataInformation:
    def findIndexOfDate(self, dfLength, dataframe, targetDate):
        target_index = 0
        for i in range(dfLength):
            tempStr = str(dataframe.iloc[i:i + 1, 0:1])
            if tempStr is not targetDate:
                target_index = target_index + 1
            else:
                break
        return target_index


# csv 파일 읽기
rawdata = pd.read_csv('VIXCLS0414.csv')
# print(rawdata.index)
# print(rawdata.info())

# 2018-01-01 부터 출력
print(rawdata.iloc[1225:, 0:2])
raw_date = rawdata.iloc[1225:, 0:1]
raw_vix = rawdata.iloc[1225:, 1:2]

plt.plot(raw_date,raw_vix)
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
plt.show()

# https://stackoverflow.com/questions/4805048/how-to-get-different-colored-lines-for-different-plots-in-a-single-figure


