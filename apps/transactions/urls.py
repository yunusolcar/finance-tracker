from django.urls import path, include
from .views import IncomeViewSet, ExpenseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'incomes', IncomeViewSet, basename='incomes')
router.register(r'expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('', include(router.urls)),
]
