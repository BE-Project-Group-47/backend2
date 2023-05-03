from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Banking(models.Model):
    age = models.IntegerField(default=18)
    income = models.IntegerField(default=20000)
    employment_length = models.FloatField(default=3)
    loan_amount = models.IntegerField(default=50000)
    loan_intent = models.TextField(default='education')
    loan_grade = models.CharField(max_length=1, default='B')
    loan_intrest = models.FloatField(default=12)
    loan_status = models.IntegerField(default=0)
    loan_percent_income = models.FloatField(default=20.1) 
    cb_person_default_on_file = models.CharField(max_length=1,default='N')
    cb_credit_history_len = models.IntegerField(default=5)

    # def __str__(self):
    #     return self.title