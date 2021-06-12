from django import forms

class SearchForm(forms.Form):
    Category = forms.CharField(max_length=100)
    # Variety = forms.CharField(widget=forms.Textarea)
    # Country = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)