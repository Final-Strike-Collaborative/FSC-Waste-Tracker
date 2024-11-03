from django.db import models


class Material(models.Model):
    UNIT_OF_MEASURE_CHOICES = {
        "lbs": "pounds",
        "oz": "ounces",
        "bdft": "boardfeet",
        "count": "count",
        "feet": "feet"
    }
    quantity = models.DecimalField()
    price = models.DecimalField()
    unit_of_measure = UNIT_OF_MEASURE_CHOICES
    note = models.CharField()
