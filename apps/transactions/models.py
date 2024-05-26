from django.db import models
from django.contrib.auth.models import User
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta


class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    frequency = models.CharField(max_length=50,
                                 choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'),
                                          ('yearly', 'Yearly')], blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.amount} - {self.date}"

    def get_next_occurrence(self):
        return calculate(self.date, self.frequency) if self.is_recurring else None


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    frequency = models.CharField(max_length=50,
                                 choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly'),
                                          ('yearly', 'Yearly')], blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.amount} - {self.date}"

    def get_next_occurrence(self):
        return calculate(self.date, self.frequency) if self.is_recurring else None


def calculate(start_date, frequency):
    if frequency == 'daily':
        return start_date + timedelta(days=1)
    elif frequency == 'weekly':
        return start_date + timedelta(weeks=1)
    elif frequency == 'monthly':
        return start_date + relativedelta(months=1)
    elif frequency == 'yearly':
        return start_date + relativedelta(years=1)
    return None
