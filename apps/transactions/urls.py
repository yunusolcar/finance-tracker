from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import IncomeViewSet, ExpenseViewSet, MonthlyProfitLoss, AnnualProfitLoss

router = DefaultRouter()
router.register(r'incomes', IncomeViewSet, basename='incomes')
router.register(r'expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),
    path('monthly-profit-loss/', MonthlyProfitLoss.as_view(), name='monthly-profit-loss-api'),
    path('annual-profit-loss/', AnnualProfitLoss.as_view(), name='annual-profit-loss-api'),

]
