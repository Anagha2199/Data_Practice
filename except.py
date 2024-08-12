'''
yob=int(input("Enter the year of birth :"))
age=2024 - yob
if age < 18:
    raise Exception(f'Entry age is below that expected, i.e {age}')
'''
def divide(x,y):
    try:
        if y==0:
            raise ZeroDivisionError("Cannot divide by zero")
        result=x/y
        return result
    except ZeroDivisionError as e:
        print("Error:",e)
    except TypeError as e:
        print("Error:String instead of integer detected in denominator")
print(divide(10,0))