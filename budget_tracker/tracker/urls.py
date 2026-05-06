from django.urls import path
from .views import dashboard,add_transaction,view_transactions,edit_transaction


urlpatterns=[
    path('dashboard/',dashboard,name='dashboard'),
    path('add_transaction',add_transaction,name='add_transaction'),
    path('transactions/',view_transactions,name='transactions'),
    path('edit_transaction/<int:transaction_id>',edit_transaction,name='edit_transaction')

]