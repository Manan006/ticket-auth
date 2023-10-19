

# import Http Response from django
from django.shortcuts import render
  
# create a function
def home(request):
    return render(request, "home.html")
