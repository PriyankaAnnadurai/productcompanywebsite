from django.shortcuts import render


def home(request):
     return render(request, "companyapp/home.html")
def contactus(request):
     return render(request, "companyapp/contactus.html")
def people(request):
     return render(request, "companyapp/people.html")
def products(request):
     return render(request, "companyapp/products.html")