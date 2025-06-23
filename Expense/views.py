from django.shortcuts import get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Expense
from .forms import ExpenseForm

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expenses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_amount'] = sum(expense.amount for expense in self.object_list)
        return context

class AddExpenseView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'addexpense.html'
    success_url = reverse_lazy('expense_list')  

class DeleteExpenseView(DeleteView):
    model = Expense
    template_name = 'expense_confirm_delete.html'  # Fixed template name
    success_url = reverse_lazy('expense_list')
