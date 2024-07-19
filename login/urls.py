from django.urls import path
from . import views

urlpatterns = [
    path('',views.log_in),
    path('sign/',views.sign,name='sign'),
    path('note/',views.sent,name='sent'),
]
