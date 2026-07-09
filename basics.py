
import numpy as np
"""
arr=numpy.array([1,2,3])
print(arr)
print(type(arr))

#0d array
arr=np.array(42)
print(arr)

#1D array
arr=np.array([1,2,3])
print(arr)

#2D ARRAY
arr=np.array([[1,2,3],[1,4,5]])
print(arr)

#3d array
arr=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(arr)

#to check the number of dimensions
arr=np.array([[1,2,3],[3,4,5]])
print(arr.ndim)

#higher dimensions
arr=np.array([1,2,3],ndmin=5)
print(arr)

#Indexing
arr=np.array([1,2,3])
print(arr[0]+arr[1])

#2D array indexing

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr[0,1])

#3d array indexing
arr=np.array([[1,2,3],[3,4,5],[6,7,8]])
print(arr[2,0])

#3d array indexing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

#negative indexing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print(arr[0,1,-1])

#slicing
arr=np.array([1,2,3])
print(arr[0:1])

#to print data type of an array
arr=np.array([1,2,3])
print(arr.dtype)

# converting array datatype to another type
arr=np.array([1.1,2.2,3.4])
arr=arr.astype('i')
print(arr)

#shape of anarray
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr.shape)

#iteration
arr=np.array([1,2,3])
for x in arr:
    print(x)
    

#2d array iteration
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
for x in arr:
    for y in x:
        print(y)

#concatenation
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr3=np.concatenate((arr1,arr2))
print(arr3)

#matplotlib
# graph
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 4, 6, 8]

plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

#bargraph
import matplotlib.pyplot as plt
language=["english","Mathematics","science"]
marks=[50,30,20]
plt.bar(language,marks)
plt.show()

#scatterplot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [5, 4, 6, 8]
plt.scatter(x,y)
plt.show()

#piechart
import matplotlib.pyplot as plt
language=["english","Mathematics","science"]
marks=[50,30,20]
plt.pie(marks,labels=language)
plt.show()


#histogram
import matplotlib.pyplot as plt

x = [10,20,30,40]
plt.hist(x)
plt.show()
"""
#grid
import matplotlib.pyplot as plt

x = [10,20,30,40]
plt.grid(x)
plt.show()