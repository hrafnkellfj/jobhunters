from django.db import models

# Create your models here.


class Company(models.Model):
    """"This class contains all the variables and methods that a user of type Company will need"""
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    logo = models.CharField(max_length=999, blank=True, default='https://img.freepik.com/free-vector/green-glowing-background_1035-3301.jpg?w=740&t=st=1715254207~exp=1715254807~hmac=a7440325379fbd7737e8bd2d645f9a37eee46c00daf28062cad5a09bb36191e0')
    coverImage = models.CharField(max_length=999, blank=True, default='https://img.freepik.com/free-vector/modern-abstract-green-background-with-elegant-elements-vector-illustration_361591-3639.jpg?w=1480&t=st=1715253786~exp=1715254386~hmac=7eef35b858a1aa123ff1c191f92151b030229f9468e78d242e22c77faa75284a')
    description = models.CharField(max_length=500)




    
