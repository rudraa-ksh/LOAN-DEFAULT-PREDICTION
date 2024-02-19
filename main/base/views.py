from django.shortcuts import render
import pickle
import numpy as np

model=pickle.load(open('Model/file.pkl','rb'))
# Create your views here.

def predict(request):
    if request.method == 'GET':
        return render(request, 'base/Home.html')
    elif request.method == 'POST':
        age = int(request.POST['age'])
        RevolvingUtilizationOfUnsecuredLines = float(request.POST['RevolvingUtilizationOfUnsecuredLines'])
        DebtRatio = float(request.POST['DebtRatio'])
        MonthlyIncome = float(request.POST['MonthlyIncome'])
        NumberOfOpenCreditLinesAndLoans = int(request.POST['NumberOfOpenCreditLinesAndLoans'])
        NumberRealEstateLoansOrLines = int(request.POST['NumberRealEstateLoansOrLines'])
        NumberOfDependents = float(request.POST['NumberOfDependents'])
        final = np.array([[DebtRatio, MonthlyIncome, RevolvingUtilizationOfUnsecuredLines, age, NumberOfOpenCreditLinesAndLoans, NumberRealEstateLoansOrLines, NumberOfDependents]])
        result = model.predict(final)
        if(result[0] == 1):
            result ="Borrower will Fail to repay the loan"
        else:
            result = "Borrower will be able to repay the loan"
        return render(request, 'base/Home.html',{'result':result})