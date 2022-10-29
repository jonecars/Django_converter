from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render




def home(request):
    return render(request, "home.html")





def calc(request):
    """
    Determine which calc to return based on input.  Call the correct results page.
    """
    # Get user input from typing box
    user_input = int(request.GET["num1"])
    # Get user input from select circles
    metric = request.GET["metric"]
    # Metric feet
    if metric == "Feet":
        value1 = user_input / 3.281
        value1 = round(value1,2)
        return render(request, "feet.html", {"result":metric, "result2":value1})
    # Metric inches
    elif metric == "Inches":
        value1 = user_input * 2.54
        value1 = round(value1,2)
        return render(request, "inches.html", {"result":metric, "result2":value1})
    # Metric Fahrenheit
    elif metric == "Fahrenheit":
        value1 = (user_input - 32) * (5/9)
        value1 = round(value1,2)
        return render(request, "fahrenheit.html", {"result":metric, "result2":value1})
    
    else:
        value1 = 0
        return render(request, "result.html", {"result":metric, "result2":value1})

# Go back to the home page.
def back(request):
    return render(request, "home.html" )