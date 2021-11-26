from django.forms import ModelForm, TextInput, widgets, forms
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'city_ name': TextInput(
            attrs={'class': 'form-control input h-75', 'placeholder': 'Add City'})}

    def clean_city_name(self):
        cities_name = self.cleaned_data.get['name']
        for instance in City.objects.all():
            if instance.name == cities_name:
                raise forms.ValidationError(' is has been added')
        return cities_name
