from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TransactionForm
from .models import Transaction

# Create your views here.

# view function for the dashboard
@login_required
def dashboard(request):
    return render(request,'tracker/dashboard.html')

# view function for adding a transaction
def add_transaction(request):
    if request.method=='POST':
        form=TransactionForm(request.POST)
        if form.is_valid():
            transaction=form.save(commit=False)
            transaction.user=request.user
            transaction.save()
            return redirect('dashboard')
    else:
        form=TransactionForm()


    return render(request,'tracker/add_transaction.html',{'form':form})

# view transaction for transactions
def view_transactions(request):
    transactions=Transaction.objects.all()
    return render(request,'tracker/view_transactions.html',{'transactions':transactions})

#view function to edit a transaction
def edit_transaction(request,transaction_id):
    transaction=get_object_or_404(Transaction,user=request.user,id=transaction_id)
    if request.method=='POST':
        form=TransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transactions')
    else:
        form=TransactionForm(instance=transaction)


    return render(request,'tracker/edit_transaction.html',{'form':form,'transaction':transaction})
    