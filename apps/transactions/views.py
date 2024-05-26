from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import Income, Expense
from .serializer import IncomeSerializer, ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.db.models import Sum
from django.utils import timezone
from rest_framework.response import Response
from datetime import timedelta


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
        end_date = start_date + timedelta(days=32)  # To include the whole month
        incomes = Income.objects.filter(user=user, date__gte=start_date, date__lt=end_date).aggregate(
            total_income=Sum('amount'))['total_income'] or 0
        expenses = Expense.objects.filter(user=user, date__gte=start_date, date__lt=end_date).aggregate(
            total_expense=Sum('amount'))['total_expense'] or 0
        monthly_profit_loss = incomes - expenses
        return Response({'monthly_profit_loss': monthly_profit_loss})
