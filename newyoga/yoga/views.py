from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import pickle
import os


def home(request):
    return render(request, "index.html")


test_data_preprocessed = pd.read_csv('test_preprocessed.csv')


def models(request):
    if 'gNB' in request.POST:
        gaussian = pickle.load(open('gNB.sav', 'rb'))
        y_pred = gaussian.predict(test_data_preprocessed)
        output = pd.DataFrame(y_pred)
        output.to_csv('gaussianNB.csv')

        filename = 'gaussianNB.csv'
        response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'gaussianNB.csv'
        return response

    if 'lg' in request.POST:
        multi = pickle.load(open('lg.sav', 'rb'))
        y_pred = multi.predict(test_data_preprocessed)
        output = pd.DataFrame(y_pred)
        output.to_csv('lg.csv')

        filename = 'lg.csv'
        response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'lg.csv'
        return response

    if 'rfc' in request.POST:
        rf = pickle.load(open('rfc.sav', 'rb'))
        y_pred = rf.predict(test_data_preprocessed)
        output = pd.DataFrame(y_pred)
        output.to_csv('rfc.csv')

        filename = 'rfc.csv'
        response = HttpResponse(open(filename, 'rb').read(), content_type='text/csv')
        response['Content-Length'] = os.path.getsize(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % 'rfc.csv'
        return response
