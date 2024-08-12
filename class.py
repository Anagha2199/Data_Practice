class Employee:
    is_Married = True
    empcount = 0
    def __init__(self,fname,lname,designation,yob):
        self._fname = fname;
        self._lname = lname;
        self._designation = designation;
        self._yob = yob;
        Employee.empcount+=1
    def getEmpDetails(self):
        print("Fullname : ",self._fname," ",self._lname)
        print("Year of Birth : ", self._yob)

e1 = Employee("Anu","K","HR",1990)
e2 = Employee("Ben","sunny","Developer",1998)

e1.getEmpDetails()
e1.is_Married = False
e2.getEmpDetails()