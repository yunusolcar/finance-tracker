from django.urls import path, include
from .views import IncomeViewSet, ExpenseViewSet, IncomeListPageView, ExpenseListPageView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'income', IncomeViewSet, basename='income')
router.register(r'expense', ExpenseViewSet, basename='expense')

urlpatterns = [
    path('incomes/', IncomeListPageView.as_view(), name='income-list'),
    path('expenses/', ExpenseListPageView.as_view(), name='expense-list'),
    path('', include(router.urls)),
]
