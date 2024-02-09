from django import forms

class SearchForm(forms.Form):
    attrs={'class': 'search-input',
           'type': 'text',
           'placeholder': 'Search',
           'name': 'search',
           'size': '80px',
           }
    query = forms.CharField(max_length=100,label=False,error_messages={'required': ''},
                            widget=forms.TextInput(attrs=attrs))
                        