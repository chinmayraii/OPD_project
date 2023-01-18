from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('signup',views.signup),
    path('signin',views.signin),
    path('patients',views.patients),
    path('dashboard',views.dashboard),
    path('bookappointment',views.bookappointment),
    path('doc_dashboard',views.doc_dashboard),
    path('checkup',views.checkup),
    path('lgout',views.lgout)
]