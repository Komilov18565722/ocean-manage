import time
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)

    def save(self, commit = True):
        user = super().save(commit)
        
        if user.password:
            user.set_password(user.password)
            user.save()
        return user

    class Meta:
        model = User
        fields = [
            'phone_number', 
            'email',
            'password',
            'first_name',
            'last_name',
            'type',

            ]