import numpy as np
"""
temp = np.array([24,23,30,12,13,23,29,27,17,27,18,15]).reshape(2,2,3)
print(temp)
print("\n")
print(temp.reshape(4,3))

temp = np.array([1,2,3,4,5,6,7,8,9,10,11,12]).reshape(4,3)
print(temp)
#print(temp.reshape(4,3))
print("*************************8")
print(np.swapaxes(temp,0,1))

num = np.linspace(2,34,7,dtype=int)
print(num)
nums = np.arange(32).reshape(4,8)
print(nums)

arr1 = np.arange(10,100,5,dtype=int).reshape(6,3)
print(arr1)

square = np.array([
    [16,3,2,13],
    [5,10,11,8],
    [9,6,7,12],
    [4,15,14,1]
])
for i in range(4):
    print(square[:,i].sum()==34)
    print(square[i,:].sum()==34)
print(square[:2]) #out:[[16  3  2 13] [ 5 10 11  8]]
print("*"*50)
print(square[:2,:2]) #out:[[16  3][ 5 10]]
print("*"*50)
print(square[2:,2:]) #out:[[ 7 12][14  1]]

num = np.linspace(5,50,24,dtype=int).reshape(4,6)
print(num)
print(num[num%2==0])
print(num.T)
print("Horizontal Sorting : \n",np.sort(num,axis=0))
print("Vertical Sorting : \n",np.sort(num,axis=1))

arr = np.array([
    [2,3,2],
    [3,5,7],
    [9,1,5]
])
print("Max Value :",np.max(arr))
print("Column wise max Value :",np.max(arr,axis=0))
print("Row wise max Value :",np.max(arr,axis=1))
print("Column wise min Value :",np.min(arr,axis=0))
print("Row wise min Value :",np.min(arr,axis=1))
print("Simple Sort(Row wise by default",np.sort(arr)) # sorts each row
print("Column wise sort : \n",np.sort(arr,axis=0)) # sorts column wise
print("Row wise sort : \n",np.sort(arr,axis=1)) # sorts row wise
print(np.mean(arr))
"""
list = [
    np.array([3,2,8,9]),
    np.array([4,12,34,25,78]),
    np.array([23,12,67])
]
result=[]
for i in range(len(list)):
    result.append(np.mean(list[i]))
print(result)
