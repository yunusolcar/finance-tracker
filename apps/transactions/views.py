from rest_framework import viewsets
from .models import Income, Expense
from .serializer import IncomeSerializer, ExpenseSerializer


class IncomeViewSet(viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)
