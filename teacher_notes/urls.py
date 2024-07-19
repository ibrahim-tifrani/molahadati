from django.urls import path
from . import views

urlpatterns = [
    path('',views.choices,name='choices'),
    path('sent_notes/',views.teachers_notes,name='upload_notes'),
    path('reply/',views.reply,name='reply'),
]
