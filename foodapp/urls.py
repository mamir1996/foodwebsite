from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('menu',views.menu,name='menu'),
    path('service',views.service,name='service'),
    path('contact',views.contact,name='contact'),
]
