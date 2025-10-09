# Ex02 Django ORM Web Application
## Date: 23/09/25

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

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


admin.py

from django.contrib import admin
from .models import(Car_db,Car_dbAdmin)
admin.site.register(Car_db,Car_dbAdmin)

```

## OUTPUT

![alt text](<Screenshot 2025-10-09 082728.png>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
