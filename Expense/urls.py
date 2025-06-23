from django.urls import path
from .views import ExpenseListView, AddExpenseView, DeleteExpenseView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),  # expense list
    path('add/', AddExpenseView.as_view(), name='add_expense'),  # Add expense page
    path('delete/<int:pk>/', DeleteExpenseView.as_view(), name='delete_expense'),  # Delete expense page
]