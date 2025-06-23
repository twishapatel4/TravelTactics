from django.urls import path
from .views import JournalEntryCreateView, JournalEntryListView, JournalEntryDeleteView

urlpatterns = [
    path('delete/<int:pk>/', JournalEntryDeleteView.as_view(), name='delete_journal'),
    path('upload/', JournalEntryCreateView.as_view(), name='upload_journal'),
    path('view/', JournalEntryListView.as_view(), name='view_journal'),
]