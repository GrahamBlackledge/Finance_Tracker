from django import path
from . import views

urlpatterns = [
    path('transactions/', views.TransactionListView.as_view(), name="transaction_list"),
    path('transactions/create', views.TransactionCreateView.as_view(), name="transaction_create"),
    path('transactions/update/<int:pk>/', views.TransactionUpdateView.as_view(), name="transaction_update"),
    path('transactions/delete/<int:pk>/', views.TransactionDeleteView.as_view(), name="transaction_delete"),

]