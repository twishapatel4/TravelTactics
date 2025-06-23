from django import forms
from .models import Itinerary, TouristLocation

class ItineraryForm(forms.ModelForm):
    state = forms.ChoiceField(required=True, label="Select State")

    class Meta:
        model = Itinerary
        fields = ['title', 'state', 'start_date', 'end_date', 'notes']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ItineraryForm, self).__init__(*args, **kwargs)
        states = TouristLocation.objects.values_list('state', flat=True).distinct()
        self.fields['state'].choices = [('','-- Select State --')] + [(state, state) for state in states]

class LocationSelectionForm(forms.Form):
    locations = forms.ModelMultipleChoiceField(
        queryset=TouristLocation.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        itinerary = kwargs.pop('itinerary', None)
        super(LocationSelectionForm, self).__init__(*args, **kwargs)

        if itinerary:
            self.fields['locations'].queryset = TouristLocation.objects.filter(state=itinerary.state)
