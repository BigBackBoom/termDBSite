from django.db import models


from datetime import datetime 
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE


# Create your models here.

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.tag_name

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.company_name

class TermData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=512, default='タイトルを入力')
    content = HTMLField()
    
    def __str__(self):
        return self.title

class Term(models.Model):
    id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=512)
    date_published = models.DateField()
    date_update = models.DateField()
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE)
    term_path = models.ForeignKey(TermData, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.service_name

    
'''
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
'''
