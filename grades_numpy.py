import numpy as np

CURVE_CENTER = 80
grades = np.array([72,35,64,88,51,90,74,12])
average =  grades.mean();
#print(average)
change = CURVE_CENTER - average
print(change)

def curves(grades):
    average = grades.mean();
    print(average)
    change = CURVE_CENTER - average
    new_grades = grades + change #vectorization
    return np.clip(new_grades,grades,100)
print (curves(grades))