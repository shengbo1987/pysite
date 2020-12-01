

import json


from django.shortcuts import HttpResponse

def hello(request):
    return HttpResponse("Hello world! ")

def info(request):
    if request.method == "GET":
        name = request.GET.get("user")
        if(name=='xiaokuo'):
            data = {'name': 'xiaokuo', 'pwd': '123456'};
        else:
            data = {'error':'No information was found'};

        print(json.dumps(data))
    return HttpResponse(json.dumps(data))

def google(request):
    data=[{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}
    ,{'date':'2015-12-31','high':'26.75749969482422','low':'26.204999923706055','open':'26.752500534057617','close':'26.315000534057617','volume':'163649200.0','adj_close':'24.182106018066406','action_x':'','value_x':'','action_y':'','value_y':''}]

    return HttpResponse(json.dumps(data))