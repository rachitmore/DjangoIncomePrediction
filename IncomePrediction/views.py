from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from Pipeline.prediction.income_prediction import IncomePrediction
from Pipeline.app_tracking.exception import AppException
import sys

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'index1.html')

def option(request):
    return render(request, 'index2.html')

@csrf_protect
def options(request):
    if request.method == 'POST':
        source = request.POST.get("Income Prediction") or request.POST.get("Wafer Fault Prediction") or request.POST.get("Credit Card Defaulters Prediction")
        
        if source == "Income Prediction":
            return render(request, 'index3.html')      
        
        else:
            result = "Something went wrong contact us  .."
            return render(request, 'index6.html', {'message': result})     

    else:          
        result = "Something went wrong contact us  .."
        return render(request, 'index4.html', {'message': result})

@csrf_protect
def predicts(request):
    if request.method == 'POST':
        try:
            age = float(request.POST['Age'])
            workclass = request.POST['Workclass']
            fnlwgt = float(request.POST['FNLWGT'])
            education = request.POST['Education']
            marital_status = request.POST['Marital Status']
            occupation = request.POST['Occupation']
            relationship = request.POST['Relationship']
            race = request.POST['Race']
            sex = float(request.POST['Sex'])
            capital_gain = float(request.POST['Capital Gain'])
            capital_loss = float(request.POST['Capital Loss'])
            hours_per_week = float(request.POST['Hours/Week'])
            country = request.POST['Country']

            data = [age, workclass, fnlwgt, education, marital_status,
                    occupation, relationship, race, sex, capital_gain,
                    capital_loss, hours_per_week, country]

            predict_object = IncomePrediction(data=data)
            result = predict_object.prediction()
            return render(request, "index3.html", {'result': result})
        
        except Exception as e:
            return render(request, "index3.html", {'result': "Oops! Something Went Wrong.. Please train the model first else Contact me"})
            raise AppException(e, sys) from e
    else:  
        return render(request, "index3.html", {'result': "Something went wrong contact us  .."})

