from django.db import models
from django.contrib import admin
class Car_db(models.Model):
    Car_id=models.IntegerField(primary_key=True)
    Brand=models.CharField(max_length=10)
    Model_car=models.CharField(max_length=10)
    Purchase_date=models.DateField()
    Mileage=models.FloatField()
class Car_dbAdmin(admin.ModelAdmin):
    list_display=["Car_id","Brand","Model_car","Purchase_date","Mileage"]