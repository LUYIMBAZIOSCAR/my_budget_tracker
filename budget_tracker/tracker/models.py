from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Transaction(models.Model):
    TRANCATION_TYPES=[
        ('income','Income'),
        ('expense','Expense')
    ]
    TRANCATION_CATERGORY=[
        ('salary','Salary'),
        ('donation','Donation'),
        ('food','Food'),
        ('transport','Transport'),
        ('airtime','Airtime')
    ]

    user=models.ForeignKey(User,models.CASCADE)
    type=models.CharField(max_length=10,choices=TRANCATION_TYPES)
    catergory=models.CharField(max_length=10,choices=TRANCATION_CATERGORY)
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    note=models.CharField(max_length=255,blank=True,null=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.type} -  {self.amount}'

