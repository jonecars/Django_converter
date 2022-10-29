# Overview

My web app takes input from the user and converts it into metric.  They will choose Fahrenheit, inches, or feet to convert.
I wrote this software to learn more about what a web app is.  I was interested to see how Django interacts with python.

[Software Demo Video](https://youtu.be/3aD5HXRO1oQ)

# Web Pages
I created 4 pages.  Each page takes uses the same base.html.  This means that when I change the format of the page in the base it will update on all pages.

The home page is where the user will select and enter their input.  When they click the submit button it will open one of three pages.  I will go to Fahrenheit, feet, or inches.

Each of the result pages prints the variable with the converted result and adds proper labels after.  Each result page has a back button to return to the input page.

Django navigates through the pages by using urls to find views.  I have a function or view set up to navigate between pages.  When the submit or back buttons are pressed then Django calls the view which returns us back to the desired page.  

The main calc view takes the user input to determine which type of calculation to perform.  It then calls the correct result page.



# Development Environment
I used Django and Python inside of Visual Studio Code to create this software.

Django handles the interactions between html/css and the saved app.
# Useful Websites

* [W3Schools](https://www.w3schools.com/django/django_getstarted.php)
* [Youtube](https://www.youtube.com/)

# Future Work

* I would like to add better html and css to the program.
* I want to add a few more conversions.
* Add another app that converts metric to imperial.