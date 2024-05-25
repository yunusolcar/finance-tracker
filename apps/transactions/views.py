from rest_framework.viewsets import ModelViewSet
from .models import Income, Expense
from .serializer import IncomeSerializer, ExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


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
