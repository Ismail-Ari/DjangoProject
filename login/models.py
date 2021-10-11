from django.db import models
from django.db.models import Model
from django.db import connections 


class EmpInsert(models.Model):
    hyva = models.CharField(max_length=1000)
    huono = models.CharField(max_length=1000)
    country = models.CharField(max_length=10000)
    aihe =  models.CharField(max_length=100000)
    arvosana = models.IntegerField()
    paivamaara = models.DateTimeField(auto_now=True, auto_now_add=False)
  
    
    class Meta:
        db_table="newemployeetable"
