from .models import Expenses
from .forms import ExpenseForm,ApprovalForm,UserForm
from django.shortcuts import render_to_response, get_object_or_404, redirect, render


def index(request):

    if request.method=="GET":
        items = Expenses.objects.all()
        return render_to_response('sample.html', {'items': items})

    if request.method=="POST":
        items = Expenses.objects.all()
        expenses = get_object_or_404(Expenses, pk=1)
        form = ApprovalForm({'status': 'APPROVED'}, instance=expenses)
        if form.is_valid():
            form.save()
            return render_to_response('sample.html', {'items': items})
        return render_to_response('sample.html', {'items': items})


def addExpense(request):

    if request.method=="POST":
        form=ExpenseForm(request.POST)
        if form.is_valid():
            model_instance=form.save(commit=False)
            model_instance.save()
            return render_to_response('indexB.html',{'form':form})

    if request.method=="GET":
        form=ExpenseForm()
        return render_to_response('indexB.html', {'form': form})
    else:
        form=ExpenseForm()
        return render_to_response('indexB.html',{'form':form})

def signin(request):

    if request.method=="GET":
        form=UserForm()
        return render_to_response('index.html', {'form': form})

    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return render_to_response('index.html', {'form': form})

def login(request):

    if request.method=="GET":
        form=UserForm()
        return render_to_response('Add-Expense.html',{'form': form})

    if request.method=="POST":
        form=UserForm()
        if request.POST['username']=="deepak":
            form=ExpenseForm()
            return render_to_response('indexB.html', {'form': form})
        else:
            items = Expenses.objects.all()
            return render_to_response('sample.html', {'items': items})
