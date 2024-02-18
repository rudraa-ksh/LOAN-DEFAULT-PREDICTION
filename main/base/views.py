from django.shortcuts import render
import pickle
import numpy as np
import os
import sys

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
            result ="Your Loan will not be approved"
        else:
            result = "Your Loan will be approved"
        return render(request, 'base/Home.html',{'result':result})