from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Expense(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)  # Expense name
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Amount of the expense
    date = models.DateField(default=timezone.now)  # Date of the expense

    def _str_(self):
        return f"{self.name} - {self.amount}"