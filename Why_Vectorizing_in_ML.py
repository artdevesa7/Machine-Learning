import numpy as np 
import time 

a = np.random.rand(1000000)
b = np.random.rand(1000000)

start = time.time()
c = np.dot(a,b)
end = time.time()

#1 second is equal to 1000000 microseconds
print("Time taken for Vectorized version: " + str(1000*(end-start)) + "ms")

start = time.time()

c = 0

for i in range(1000000):
	c += a[i]*b[i]

end = time.time()

print("Time taken for loop version: " + str(1000*(end-start)) + "ms")

"""
As you see above the time taken to perform a dot product using vectors took around 1.239 ms, 
hereas to perform the same operation using FOR LOOPS took around 640ms. 
The vectorized version is around 500 times faster than the non vectorized version.

In machine learning era, we often perform operation on large datasets. 
And so, its important the code must run very quickly because otherwise, 
if its running on a big dataset your code might take a very long time to run. 
Its the difference between your code taking maybe one minute to run versus taking 
lets say five hours to run.
"""