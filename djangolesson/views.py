from django.shortcuts import render
from django.http import HttpResponse


def main(request):
   return render(request, "main.html", {})
   
def exOne(request, firstParameter, secondParameter):
	return render(request, "ex1.html", { 'firstParameter' : firstParameter, 'secondParameter' : secondParameter})