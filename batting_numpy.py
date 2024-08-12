import numpy as np
batting_average = np.array([
    [50,30,70,10],
    [20,60,90,70],
    [100,90,100,80],
    [40,30,20,0]
])
print("Size of the array : ",batting_average.shape)
print("Maximum Average : ",batting_average.max())
print("Maximum Average Column : ",batting_average.max(axis=0)) #rowwise max values from each
print("Maximum Average Row : ",batting_average.max(axis=1))#columnwise max values from each