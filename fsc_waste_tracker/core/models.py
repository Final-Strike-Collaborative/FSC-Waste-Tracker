from django.db import models


class Material(models.Model):
    UNIT_OF_MEASURE_CHOICES = {
        "lbs": "pounds",
        "oz": "ounces",
        "bdft": "boardfeet",
        "count": "count",
        "feet": "feet",
    }
    quantity = models.DecimalField(decimal_places=2, max_digits=24)
    price = models.DecimalField(decimal_places=2, max_digits=24)
    unit_of_measure = UNIT_OF_MEASURE_CHOICES
    note = models.CharField()

class Receipt(models.Model):
    note = models.CharField()
    grand_total = models.DecimalField(decimal_places=2, max_digits=24)

