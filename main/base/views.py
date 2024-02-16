from django.shortcuts import render
import pickle
model=pickle.load(open('./Model/file.pkl','rb'))
# Create your views here.
def home(request):
    return render(request,'base/home.html')

def predict(request):
    age = request.GET['age']
    RevolvingUtilizationOfUnsecuredLines = request.GET['RevolvingUtilizationOfUnsecuredLines']
    DebtRatio =request.GET['DebtRatio']
    MonthlyIncome = request.GET['MonthlyIncome']
    NumberOfOpenCreditLinesandLoans = request.GET['NumberOfOpenCreditLinesAndLones']
    NumberofRealEstateLoansOrLines = request.GET['NumberOfRealEstateLoansOrLones']
    NumberofDependents = request.GET['NumberOfDependents']
    result = model.predict_proba(['DebtRatio', 'MonthlyIncome', 'RevolvingUtilizationOfUnsecuredLines','age', 'NumberOfOpenCreditLinesAndLoans','NumberRealEstateLoansOrLines', 'NumberOfDependents'])
    return render(request, 'base/Result.html',{'result':result})