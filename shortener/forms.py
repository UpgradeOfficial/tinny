from django import forms
from .models import User, URLShortener, Record
from django.contrib.auth.forms import UserCreationForm
from django.utils.crypto import get_random_string
import re


def unique_url_id():
    id = get_random_string(10)
    if URLShortener.objects.filter(unique_id=id).exists():
        return unique_id()
    return id
    
def urlify(s):

    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", '', s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", '-', s)

    return s


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    class Meta:
        model = User
        fields = ('first_name','last_name',"username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user

class URLShortenerForm(forms.ModelForm):
    class Meta:
        model = URLShortener
        fields = ( 'name', 'url', 'description', 'unique_id')
        widget={"unique_id": forms.TextInput(attrs={'required': False}),
        }
        
    def clean_unique_id(self):
        unique_id = self.cleaned_data['unique_id']
        
        #print(unique_id)
        if len(unique_id) <= 5:
            unique_id = unique_url_id()
        unique_id=unique_id.lower()
        #print(unique_id)
        unique_id=urlify(unique_id)
        print(unique_id)
        return unique_id
        
 
   
            
        
'''  
    def save(self, commit=True):
        url_form = super(URLShortenerForm, self).save(commit=False)
        url_form.unique_id = unique_url_id()
        if commit:
            url_form.save()
        return url_form
'''
        
