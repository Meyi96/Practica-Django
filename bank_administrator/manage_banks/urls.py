from django.urls import path
from . import views

app_name="manage_banks"
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:client_id>/', views.detail, name='detail'),
    path('bank/<int:bankaccount_id>/', views.detail_bankAccount, name='detail_bankAccount'),
    path('update/<int:bankaccount_id>/', views.charge_money,name='charge_money')

]