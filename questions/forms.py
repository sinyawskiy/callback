# coding=utf-8
from django import forms
from questions.models import Callback


class CallbackForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'Имя'}), label=u'Представьтесь')
    phone = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': u'+7 (', 'class': u'form-control masked_input_mobile'}), required=False, label=u'Телефон')

    class Meta:
        model = Callback
        fields = ['name', 'phone', 'email']