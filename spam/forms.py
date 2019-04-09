from django import forms

class DetectForm(forms.Form):
    msg = forms.CharField(label='msg', max_length=100)


