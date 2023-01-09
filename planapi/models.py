from django.db import models

# Create your models here.

# Creating company model


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, choices=(
        ('Reliance Jio', 'Reliance Jio'), ('Airtel', 'Airtel'), ('Vi', 'Vi'), ('BSNL', 'BSNL')))
    owenership = models.CharField(max_length=50)
    about = models.TextField()
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
# creating plan api


class GetPlans(models.Model):
    name = models.CharField(max_length=50)
    plan = models.CharField(max_length=50)
    validity = models.CharField(max_length=50)
    data = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=50, choices=(
        ('Preapaid', 'Prepaid'), ('Postpaid', 'Postpaid')))
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
