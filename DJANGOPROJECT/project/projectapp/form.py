from django import forms

from projectapp.models import Users
class makeform(forms.ModelForm):
    class Meta:
        model=Users
        fields=("Firstname","Lastname","Email","Subject","Message")