from django.shortcuts import render, redirect
import pandas as pd
import pickle, os, random

# Create your views here.

def Voice(request):
    results = None
    if request.method == 'POST':
        if request.POST.get('voice_button'):
            name = request.POST['Person Name']
            sd = request.POST['sd']
            median = request.POST['median']
            Q25 = request.POST['Q25']
            Q75 = request.POST['Q75']
            IQR = request.POST['IQR']
            Skew = request.POST['skew']
            spent = request.POST['spent']
            Mode = request.POST['mode']
            Centroid = request.POST['centroid']
            meanfun = request.POST['meanfun']
            minfun = request.POST['minfun']
            maxfun = request.POST['maxfun']
            mindom = request.POST['mindom']
            maxdom = request.POST['maxdom']
            modindx = request.POST['modindx']

            results = Finder(name, sd, median, Q25, Q75, IQR, Skew, spent, Mode, Centroid, meanfun, minfun, maxfun, mindom, maxdom, modindx)
            results = results[0]
            print(results)

        else:
            print('Not Working')

    else:
        results = None

    return render(request, 'mainpage.html' ,{'result':results})

def Finder(name, sd, median, Q25, Q75, IQR, Skew, spent, Mode, Centroid, meanfun, minfun, maxfun, mindom, maxdom, modindx):

    if name != "":
        data = pd.DataFrame(columns = ['sd', 'median', 'Q25', 'Q75', 'IQR', 'skew', 'sp.ent', 'mode', 'centroid', 'meanfun', 'minfun', 'maxfun', 'mindom', 'maxdom', 'modindx'])
        data1={'sd':float(sd),'median':float(median),'Q25':float(Q25),'Q75':float(Q75),'IQR':float(IQR),'skew':float(Skew),'sp.ent':float(spent),'mode':float(Mode),'centroid':float(Centroid),'meanfun':float(meanfun),'minfun':float(minfun),'maxfun':float(maxfun),'mindom':float(mindom),'maxdom':float(maxdom),'modindx':float(modindx)}
        
        data = data.append(data1, ignore_index=True)

        filename = r'voice/Gender_prediction.pickle'
        loaded_model = pickle.load(open(filename,'rb'))
        res = loaded_model.predict(data)

        return res
    else:
        return None
