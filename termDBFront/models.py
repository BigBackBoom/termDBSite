from django.db import models


from datetime import datetime 

# Create your models here.

class Plan(models.Model):
    plan_name = models.CharField(max_length=32);
    one_week_price = models.IntegerField(default=0)
    one_month_price = models.IntegerField(default=0)
    three_month_price = models.IntegerField(default=0)
    one_year_price = models.IntegerField(default=0)

    def __str__(self):
        return self.plan_name


class Customer(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    salt = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    plan_joined = models.ForeignKey(Plan, on_delete=models.CASCADE, default=1)
    plan_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return (self.first_name + " " + self.last_name)

