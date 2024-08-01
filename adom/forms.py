from django import forms

class HymnSearchForm(forms.Form):
    query = forms.CharField(label='Search Hymns', max_length=100)
