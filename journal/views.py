from django.views.generic import CreateView, ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import TravelJournalEntry
from .forms import JournalEntryForm

class JournalEntryCreateView(LoginRequiredMixin, CreateView):
    model = TravelJournalEntry
    form_class = JournalEntryForm
    template_name = 'journal/upload.html'
    success_url = reverse_lazy('view_journal')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JournalEntryListView(LoginRequiredMixin, ListView):
    model = TravelJournalEntry
    template_name = 'journal/view.html'
    context_object_name = 'entries'
    ordering = ['-created_at']

    def get_queryset(self):
        return TravelJournalEntry.objects.filter(user=self.request.user).order_by('-created_at')
    
class JournalEntryDeleteView(DeleteView):
    model = TravelJournalEntry
    template_name = 'journal/confirm_delete.html'
    success_url = reverse_lazy('view_journal')