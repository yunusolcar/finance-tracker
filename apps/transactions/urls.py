from django.urls import path, include
from .views import IncomeViewSet, ExpenseViewSet, MonthlyProfitLoss
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'incomes', IncomeViewSet, basename='incomes')
router.register(r'expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),
    path('monthly-profit-loss/', MonthlyProfitLoss.as_view(), name='monthly-profit-loss-api'),

]
