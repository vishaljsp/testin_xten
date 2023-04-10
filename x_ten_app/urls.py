from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    # path('crear',views.crear,name="crear"),
    path('about-us',views.about,name="about"),
    # path('contact-us',views.contact,name="contact"),
    # path('gellary',views.gellary,name="gellary"),
    path('our-values',views.ourvalue,name="ourvalue"),
    # path('plantevent',views.plantevent,name="plantevent"),
    path('service',views.service,name="service"),
    # path('testimonial',views.testimonial,name="testimonial"),
    path('weding',views.weding,name="weding"),




]