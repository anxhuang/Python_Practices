import numpy as np
import matplotlib.pyplot as plt

salaries = np.genfromtxt("208-15.csv", delimiter=',', skip_header=1, encoding="UTF-8", usecols=2)

print("經常性薪資最大值:", np.max(salaries))
print("經常性薪資最小值:", np.min(salaries))
print("經常性薪資平均值:", np.mean(salaries))
print("經常性薪資中位數:", np.median(salaries))
print("經常性薪資位於90%的值:", np.percentile(salaries, 90))
print("經常性薪資位於80%的值:", np.percentile(salaries, 80))
print("經常性薪資位於75%的值:", np.percentile(salaries, 75))
print("經常性薪資位於50%的值:", np.percentile(salaries, 50))
print("經常性薪資位於25%的值:", np.percentile(salaries, 25))

plt.figure(figsize=(8, 5))
plt.plot(salaries)
plt.xlabel('Catalogs')
plt.ylabel('Salary')
plt.show()



