
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms




class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254)
    password2= None

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['username'].help_text = False
        self.fields['username'].widget.attrs['placeholder'] = 'USERNAME'

        self.fields['email'].label = False
        self.fields['email'].widget.attrs['placeholder'] = 'EMAIL'

        self.fields['password1'].label = False
        self.fields['password1'].help_text = False
        self.fields['password1'].widget.attrs['placeholder'] = 'PASSWORD'        

class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = False
        self.fields['username'].widget.attrs['placeholder'] = 'USERNAME'
        self.fields['password'].label = False
        self.fields['password'].widget.attrs['placeholder'] = 'PASSWORD'


