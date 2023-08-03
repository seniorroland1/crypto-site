from django.urls import path
from .views import *

urlpatterns = [
    path('deposite/',create_deposite,name="create_deposite"),
    path('update_deposite/<int:pk>/',update_deposite,name="update_deposite"),
    path('withdraw/',create_withdraw,name="create_withdraw"),
    path('update_withdraw/<int:pk>/',update_withdraw,name="update_withdraw")
]