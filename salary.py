s_allowances={"HRA":0.4,"DA":0.3,"TA":0.15}
s_deductions={"PF":0.12,"INSURANCE":5000}

def calcAllowances(basic):
    total_allowances=0
    for key in s_allowances:
        total_allowances+=s_allowances[key]*basic
    return total_allowances

def calcDeductions(basic):
    total_deductions = 0
    for key in s_deductions:
        if type(s_deductions[key] is not int):
            total_deductions+=s_deductions[key]*basic
        else:
            total_deductions += s_deductions[key]
    return total_deductions;

def PTax(mSal):
    prof_tax=0
    if mSal>=8500 and mSal<=10000:
        prof_tax=200
    elif mSal>10000 and mSal<=30000:
        prof_tax=300
    elif mSal>300000:
        prof_tax=500
    return  prof_tax

def calculateSalary():
    bsal=int(input("Enter your basic salary:"))
    gsal = bsal + calcAllowances(bsal)
    p_tax=PTax(gsal)
    nsal=gsal-calcDeductions(bsal)-p_tax
    print("",bsal)
    print("",calcAllowances(bsal) )
    print("",calcDeductions(bsal) )
    print("",PTax(bsal) )
    print("", gsal)
    print("", nsal)

calculateSalary();