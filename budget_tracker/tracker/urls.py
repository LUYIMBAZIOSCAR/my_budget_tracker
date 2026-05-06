from django.urls import path
from .views import dashboard,add_transaction,view_transactions


urlpatterns=[
    path('dashboard/',dashboard,name='dashboard'),
    path('add_transaction',add_transaction,name='add_transaction'),
    path('transactions/',view_transactions,name='transactions')

]