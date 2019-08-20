import numpy as np

import time
t1 = time.time()
arr = np.array([(2, 3, 5), (6, 8, 9)])
arrEmp = np.empty((5, 4))
arrOnes = np.ones((5, 4), dtype=np.int_)
np.random.seed(666)
arrRandom = np.random.randint(0, 10000, size=(500, 400))
aSum = arrRandom.max(axis=0)
arrMax = np.argmax(arrRandom)
t2 = time.time()

a = np.random.rand(5)
idx = np.array([1, 1, 2, 3])
print(a[idx])
