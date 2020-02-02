# Feigenbaum growth equation

from matplotlib import pyplot as plt
import numpy as np

X = np.zeros(200)
r = np.arange(0, 4, 0.0001)
res1 = np.zeros(len(r))
res2 = np.zeros(len(r))
res3 = np.zeros(len(r))
res4 = np.zeros(len(r))
res5 = np.zeros(len(r))
res6 = np.zeros(len(r))
res7 = np.zeros(len(r))
res8 = np.zeros(len(r))
res9 = np.zeros(len(r))

# to generate the function  x = np.arange(-100,100,1)
# plotting the function plt.plot(2.6*x*(1-x))


for j in range(0, (len(r) - 1)):
    for i in range(len(X) - 2):
        X[0] = 0.5
        X[i + 1] = r[j] * X[i] * (1 - X[i])
        X[i + 2] = X[i + 1]
        res1[j] = X[-1]
        res2[j] = X[-2]
        res3[j] = X[-3]
        res4[j] = X[-4]
        res5[j] = X[-5]
        res6[j] = X[-6]
        res7[j] = X[-7]
        res8[j] = X[-8]
        res9[j] = X[-9]

# print(X)
# print(res)

Fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(r, res1, color='blue', label='res1')
ax.plot(r, res2, color='blue', label='res2')
ax.plot(r, res3, color='blue', label='res3')
ax.plot(r, res4, color='blue', label='res4')
ax.plot(r, res5, color='blue', label='res5')
ax.plot(r, res6, color='blue', label='res6')
ax.plot(r, res7, color='blue', label='res7')
ax.plot(r, res8, color='blue', label='res8')
ax.plot(r, res9, color='blue', label='res9')
plt.show()
