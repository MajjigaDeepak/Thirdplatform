from django.forms import ModelForm
from .models import Expenses,Users

class ExpenseForm(ModelForm):

    class Meta:
        model=Expenses
        fields={'id','employee_Name','Category','Date','Ammount'}

class ApprovalForm(ModelForm):

    class Meta:
        model=Expenses
        fields={'id','status'}

class UserForm(ModelForm):

    class Meta:
        model=Users
        fields={'username','password'}


