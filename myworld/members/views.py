from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render




def home(request):
    
    return render(request, "home.html")

def calc(request):


    user_input = int(request.GET["num1"])
    metric = request.GET["metric"]
    if metric == "Feet":
        value1 = user_input / 3.281
        value1 = round(value1,2)
        return render(request, "feet.html", {"result":metric, "result2":value1})
    elif metric == "Inches":
        value1 = user_input * 2.54
        value1 = round(value1,2)
        return render(request, "inches.html", {"result":metric, "result2":value1})
    elif metric == "Fahrenheit":
        value1 = (user_input - 32) * (5/9)
        value1 = round(value1,2)
        return render(request, "fahrenheit.html", {"result":metric, "result2":value1})
    else:
        value1 = 15
        return render(request, "result.html", {"result":metric, "result2":value1})

def back(request):
    return render(request, "home.html" )