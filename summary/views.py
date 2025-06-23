from django.views.generic import TemplateView, View
from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
import tempfile

from PackingList.models import Task
from iti.models import Itinerary
from Expense.models import Expense
from journal.models import TravelJournalEntry

class TripSummaryView(TemplateView):
    template_name = 'summary/trip_summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['tasks'] = Task.objects.filter(user=user)
        context['itineraries'] = Itinerary.objects.filter(user=user)
        context['expenses'] = Expense.objects.filter(user=user)
        context['journals'] = TravelJournalEntry.objects.filter(user=user)
        return context

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        context = {
            'tasks': Task.objects.filter(user=user),
            'itineraries': Itinerary.objects.filter(user=user),
            'expenses': Expense.objects.filter(user=user),
            'journals': TravelJournalEntry.objects.filter(user=user),
        }

        html_string = render_to_string('summary/trip_summary.html', context)
        html = HTML(string=html_string)
        result = html.write_pdf()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=travel_summary.pdf'
        response.write(result)
        return response
