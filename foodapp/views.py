from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'foodapp/home.html')
def menu(req):
    return render(req,'foodapp/menu.html')
def service(req):
    return render(req,'foodapp/service.html')
def contact(req):
    return render(req,'foodapp/contact.html')