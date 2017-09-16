from django import forms
from .models import *



class addContactedForm(forms.ModelForm):

    name = forms.CharField(label='Name', max_length=30, widget=forms.TextInput(attrs={'required':'required','name':'name','class':'form-control'}))
    subject  = forms.CharField(label='Subject', max_length=30, widget=forms.TextInput(attrs={'required':'required','name':'subject','class':'form-control'}))
    email      = forms.EmailField(label='Email', max_length=30, widget=forms.TextInput(attrs={'required':'required','name':'email','class':'form-control'}))
    comments   = forms.CharField(label='Description', widget=forms.Textarea(attrs={'required':'required','name':'email','class':'form-control'}))

    class Meta:
        model = contacted
        fields = ['name','email','subject','comments']



