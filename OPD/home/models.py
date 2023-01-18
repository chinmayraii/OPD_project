from django.db import models
from django.contrib.auth.models import User


class Doctors_name(models.Model):
    dname=models.CharField(max_length=50) 
    def __str__(self) -> str:
        return self.dname       

class Patient(models.Model):
    doctors=models.ForeignKey(Doctors_name,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=50)
    date=models.DateField(auto_now=False)
    notes=models.TextField()
    def __str__(self) -> str:
        return self.patient_name

class Doctor(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    medicines=models.CharField(max_length=50)
    causes=models.CharField(max_length=50)
    symptoms=models.CharField(max_length=50)
    file=models.FileField(upload_to='files')
    comments=models.TextField() 
    def __str__(self) -> str:
        return self.patient.patient_name       

