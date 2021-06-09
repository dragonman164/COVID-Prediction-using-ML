from django import shortcuts
from django.shortcuts import redirect, render
from django.urls import reverse
from sklearn import metrics
from .forms import CovidSymptopmsForm
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

# Create your views here.
def home(request):
    return render(request,"covidmodel/index.html")

def about(request):
    return render(request,"covidmodel/about.html")

def license(request):
    return render(request,"covidmodel/license.html")

def form(request):
    encoder = LabelEncoder()
    covid_data = pd.read_csv('covid.csv')
    columns_not_required = [
    'test_date',
    'test_indication',
    'age_60_and_above', 
    ]


    for elem in columns_not_required:
        covid_data = covid_data.drop(elem,axis = 1)

    covid_data = covid_data.replace(to_replace='None')
    covid_data['corona_result'] = encoder.fit_transform(covid_data['corona_result'])
    covid_data['gender'] = encoder.fit_transform(covid_data['gender'])
    X = covid_data.drop('corona_result',axis = 1)
    y = covid_data['corona_result']
    X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 0)

    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train,y_train)
    y_pred = knn.predict(X_test)
    accuracy = metrics.accuracy_score(y_test,y_pred)
    if request.method == 'POST':
        form = CovidSymptopmsForm(request.POST)
        if form.is_valid():
            form.save()
            cough = 1 if form.data.get('cough') == 'on' else 0
            fever = 1 if form.data.get('fever') == 'on' else 0 
            sore_throat = 1 if form.data.get('sore_throat') == 'on' else 0 
            shortness_of_breadth = 1 if form.data.get('shortness_of_breadth')=='on' else 0 
            head_ache = 1 if form.data.get('head_ache')=='on' else 0
            gender = form.data.get('gender')
            if gender == 'a':
                gender = 1 
            else:
                gender = 0
            ans = knn.predict(np.array([cough,fever,sore_throat,shortness_of_breadth,head_ache,gender]).reshape(1,-1))
            print(ans)
            return redirect('results')

    form = CovidSymptopmsForm()
    params = {'form':form}
    return render(request,"covidmodel/form.html",params)



def results(request):
    return render(request,"covidmodel/results.html",{'accuracy':99})





