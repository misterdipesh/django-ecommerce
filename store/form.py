from django.forms import ModelForm
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django import forms

class AccountRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = Account
        fields = (
            'email', 'address', 'first_name', 'last_name', 'contact', 'username'
        )

        def save(self, commit = True):
            user = super(AccountRegistrationForm, self).save(commit= False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.username = self.cleaned_data['username']
            user.address=self.cleaned_data['address']

            if commit:
                user.save()

                return User





