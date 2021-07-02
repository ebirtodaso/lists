from django import forms
from .models import listItem

class doneForm(forms.Form):
  isDone = forms.BooleanField(required=False)

  class Meta:
    model = listItem
    exclude = ['item']

class addItemForm(forms.Form):

  class Meta:
    model = listItem
    fields = ('item')