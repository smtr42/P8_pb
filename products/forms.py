from django import forms


class SearchForm(forms.Form):
    product = forms.CharField(max_length=100, required=False,)
