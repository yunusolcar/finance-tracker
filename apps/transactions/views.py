from datetime import timedelta

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.utils import timezone
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Income, Expense
from .serializer import IncomeSerializer, ExpenseSerializer


class IncomeListPageView(LoginRequiredMixin, TemplateView):
    template_name = 'transactions/income.html'


class ExpenseListPageView(LoginRequiredMixin, TemplateView):
    template_name = 'transactions/expense.html'


class IncomeViewSet(ModelViewSet):
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class ExpenseViewSet(ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class MonthlyProfitLoss(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = timezone.now()
        start_date = today.replace(day=1)
        next_month = (start_date.replace(day=28) + timedelta(days=4)).replace(day=1)

        incomes = Income.objects.filter(user=user, date__gte=start_date, date__lt=next_month).aggregate(
            total_income=Sum('amount'))['total_income'] or 0

        expenses = Expense.objects.filter(user=user, date__gte=start_date, date__lt=next_month).aggregate(
            total_expense=Sum('amount'))['total_expense'] or 0

        monthly_profit_loss = incomes - expenses
        return Response({'monthly_profit_loss': monthly_profit_loss})
