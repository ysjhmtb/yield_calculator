'''
한번의 거래에서 100%의 확률로 5%의 수익률이 보장되는 상품과
한번의 거래에서 30%의 확률로 -5%의 수익률이 기대되거나 70%의 확률로 10%의 수익률이 기대되는 상품.

편의상 전자를 pOne, 후자를 pTwo라고 지칭.

1,000번의 거래를 반복하면
pOne : (1.05)^1000 의 수익이 기대되고
pTwo : (0.95)^(300) * (1.1)*(700) 의 수익이 기대된다.

지수를 항의 앞으로 내리기 위해 로그를 취한다.

pOne : 1000 * log(1.05)
pTwo : 300 * log(0.95) + 700 * log(1.1)

'''

import numpy as np
import matplotlib.pyplot as plt

# 가장 적합한 로그 함수를 사용한 것이 아니기 때문에 계산 오차 발생.

pOne = 1000 * np.log2(1.05)
pTwo = 300 * np.log2(0.95) + 700 * np.log2(1.1)

# 우선 전액을 베팅하는 상황을 가정.

pOne = 1000 * np.log2(1 + 1 * 0.05)
pTwo = 300 * np.log2(1 + 1 * (-0.05)) + 700 * np.log2(1 + 1 * (0.1))

print(pOne) # 70.389327891398
print(pTwo) # 74.05229219182144

# 위의 결과를 통해 두 번째 상품이 더 적합함을 알 수 있다.
# 이제 베팅 두 상품의 베팅 비율을 조정해 보자.




fractionList = []
pOneF = []
pTwoF = []

f = 0.0
while f < 5:
    pOne = 1000 * np.log2(1 + f * 0.05)
    pTwo = 300 * np.log2(1 + f * (-0.05)) + 700 * np.log2(1 + f * (0.1))

    fractionList.append(f)
    pOneF.append(pOne)
    pTwoF.append(pTwo)

    f += 0.01


plt.plot(fractionList,pOneF, label='pOneF')
plt.plot(fractionList,pTwoF,label='pTwoF')
plt.legend()
fig = plt.gcf()
plt.show()
fig.savefig('KellyExample.PNG')


# 그래프를 그려보면 1배 전액베팅 시에는 처음의 계산처럼 후자가 전자보다 더 높은 수익률을 보인다.
# 하지만 레버리지를 3배 이상 키우게 되면 전자의 수익률이 더 높음을 알 수 있다.
# 무엇보다 고무적인 것은 두 상품 모두 5배 이상의 레버리지가 권장된다는 것이다.
