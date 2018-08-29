import numpy as np

(close, volume) = np.genfromtxt("208-14.csv", delimiter=',', skip_header=1, usecols=(4, 5), unpack=True)
print("收盤價最大值: ", np.max(close))  # 同close.max()
print("收盤價最小值: ", np.min(close))  # 同close.min()
print("收盤價平均值: ", np.mean(close))  # 同close.mean()
print("收盤價中位數: ", np.median(close))
print("收盤價加權平均值: ", np.average(close, weights=volume))

input("Enter to exit")

