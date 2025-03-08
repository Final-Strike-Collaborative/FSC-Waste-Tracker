from django.db import models


class Material(models.Model):
    label = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    unit = models.CharField(max_length=10)
    order = models.ForeignKey(Question, on_delete=models.CASCADE) 

class Order(models.Model):
    label = models.CharField(max_length=200)
    purchase_date = models.DateTimeField("date published")
